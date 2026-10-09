#!/usr/bin/env python3
"""Flag common AI-writing tells in a piece of text.

Usage:
    python3 check.py FILE        # check a file
    python3 check.py -           # read from stdin
    python3 check.py FILE --json # machine-readable output

This is a lint pass, not a detector. It catches mechanical habits (stock
vocabulary, em dashes, sentence templates, formatting density, uniform rhythm).
It can't judge whether the text actually says anything, which matters more.
"""

import json
import re
import statistics
import sys

# Each rule: (category, label, regex). Matched case-insensitively per line.
RULES = [
    # Openers / closers
    ("opener", "sycophantic opener",
     r"^\s*(great|excellent|fantastic|good) question\b|^\s*(certainly|absolutely|of course|sure thing)[!.,]"),
    ("opener", "happy-to-help opener", r"\bI'?d be (happy|glad|delighted) to help\b"),
    ("opener", "email pleasantry", r"\bhope (this|the) (email|message|note) finds you\b|\bI hope you'?re (doing )?well\b"),
    ("opener", "announcing the answer",
     r"\blet'?s (dive|delve|jump|dig) (in|into|deeper)\b|\blet'?s break (it|this) down\b|"
     r"\bhere'?s (a|the) (comprehensive |quick |detailed )?(breakdown|overview|rundown)\b|\bin this (article|post|guide), (we|I) will\b"),
    ("closer", "recap closer", r"^\s*(in conclusion|in summary|to summari[sz]e|overall|ultimately|all in all|to wrap up)\b"),
    ("closer", "help-desk sign-off",
     r"\bhope (this|that) helps\b|\blet me know if you (have|need) any\b|\bfeel free to (reach out|ask|let me know)\b|\bhappy (writing|coding|reading)!"),

    # Sentence templates
    ("template", "negative parallelism (not X, it's Y)",
     r"\bnot (just |only |merely |simply )?(about )?[^.,;]{1,40}[,;—–-]+\s*(it'?s|this is|that'?s|they'?re|but)\b|"
     r"\bisn'?t (just |only |merely )?(about )?[^.]{1,40}\.\s*it'?s\b|"
     r"\bnot only\b[^.]{1,80}\bbut (also)?\b|\bless about\b[^.]{1,60}\bmore about\b"),
    ("template", "rhetorical question then answer",
     r"\b(the (result|answer|catch|kicker|best part|twist|truth|problem|secret))\?|\b(why|what) does (this|that|it) (matter|mean)\?|\bso what'?s the (catch|point)\?"),
    ("template", "colon / 'here's' reveal",
     r"\bhere'?s (the thing|why|the kicker|the deal|what)\s*:|\bthe (bottom line|kicker|takeaway|truth)\s*:"),
    ("template", "tacked-on -ing commentary",
     r",\s*(highlighting|underscoring|emphasi[sz]ing|showcasing|reflecting|demonstrating|illustrating|reinforcing|signal(l)?ing|cementing) (the|its|their|a|his|her|how)\b"),
    ("template", "inflated significance",
     r"\b(stands|serves) as (a|an) (testament|reminder|beacon|symbol)\b|\bplays? an? (vital|pivotal|crucial|key|significant|important) role\b|"
     r"\bmarks? an? (significant|important|major) (milestone|shift|step)\b|\bpav(e|es|ed|ing) the way\b"),
    ("template", "staccato hype fragments", r"(\b\w+\.\s+){2,}(just|only|pure) \w+\.|\bno (fluff|filler|nonsense)\."),
    ("template", "range sweep (from X to Y)", r"\bfrom [\w\s-]{2,30} to [\w\s-]{2,30},? (we|you|everyone|businesses|companies|people)\b"),
    ("template", "'whether you're a … or …'", r"\bwhether you'?re an? [^.]{1,40} or an?\b"),

    # Vocabulary
    ("vocab", "stock AI word",
     r"\b(delv(e|es|ed|ing)|tapestry|testament|realm|embark(s|ed|ing)?|leverag(e|es|ed|ing)|harness(es|ed|ing)?|"
     r"unlock(s|ed|ing)?|unleash(es|ed|ing)?|elevat(e|es|ed|ing)|empower(s|ed|ing)?|foster(s|ed|ing)?|bolster(s|ed|ing)?|"
     r"underscor(e|es|ed|ing)|showcas(e|es|ed|ing)|spearhead(s|ed|ing)?|robust|seamless(ly)?|pivotal|multifaceted|"
     r"holistic|synergy|paradigm|plethora|myriad|cornerstone|beacon|game[- ]changer|game[- ]changing|ever[- ]evolving|"
     r"cutting[- ]edge|transformative|unparalleled|meticulous(ly)?|intricac(y|ies)|labyrinth(ine)?|treasure trove|interplay)\b"),
    ("vocab", "stock phrase",
     r"\bin today'?s (fast[- ]paced|digital|modern|ever[- ]changing) (world|age|landscape|era)\b|\bin an era of\b|"
     r"\bit'?s (important|worth|crucial|essential) (to note|noting|to remember|mentioning)\b|\bit bears mentioning\b|"
     r"\bwhen it comes to\b|\bat the end of the day\b|\ba deep dive\b|\bnavigat(e|ing) the (complexities|intricacies|world|landscape)\b|"
     r"\b(rich|vibrant) tapestry\b|\b(the )?(digital|evolving|ever[- ]changing|competitive) landscape\b|\btake (it|things|your \w+) to the next level\b|"
     r"\ba (wide|broad|diverse) (range|array|variety) of\b"),
    ("vocab", "intensifier", r"\b(truly|incredibly|remarkably|deeply|genuinely|undeniably)\s+\w+"),
    ("vocab", "vague attribution",
     r"\b(studies|research|experts|many people|some (people|critics)) (show|shows|suggest|suggests|agree|believe|say|argue)\b|\bit is widely (regarded|believed|accepted)\b"),

    # Fiction
    ("fiction", "stock fiction phrase",
     r"\bbarely above a whisper\b|\b(a )?breath (she|he|they|I) didn'?t know\b|\bthe air (was )?thick with\b|"
     r"\bshiver ran down\b|\beyes (sparkling|glinting|twinkling) with\b|\btime (seemed to )?st(ood|and) still\b|"
     r"\bsomewhere,? (in the distance,? )?a dog barked\b|\blittle did (she|he|they|I|we) know\b|\ba mix(ture)? of \w+ and \w+\b|"
     r"\ba flicker of (something|\w+)\b"),
    ("fiction", "stock fantasy name", r"\b(Elara|Lyra|Kael|Seraphina|Zephyr|Thorne|Elowen|Evelyn Reed|Aria Blackwood)\b"),
]

COMPILED = [(c, l, re.compile(p, re.IGNORECASE | re.MULTILINE)) for c, l, p in RULES]

TRIPLET = re.compile(r"\b[\w-]+(?: [\w-]+)?, [\w-]+(?: [\w-]+)?,? and [\w-]+(?: [\w-]+)?\b")
EM_DASH = re.compile(r"—|(?<=\w) -- (?=\w)|(?<=\w) – (?=\w)")
BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
BULLET = re.compile(r"^\s*([-*•]|\d+[.)])\s+")
HEADING = re.compile(r"^\s*#{1,6}\s+\S")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿✅❌⭐]")
CONTRACTABLE = re.compile(r"\b(do not|does not|did not|is not|are not|was not|were not|cannot|can not|will not|would not|"
                          r"should not|could not|it is|that is|there is|I am|you are|we are|they are|I have|you have|we have|"
                          r"have not|has not|let us|I will|you will|we will)\b", re.IGNORECASE)
CONTRACTION = re.compile(r"\b\w+'(t|s|re|ve|ll|d|m)\b", re.IGNORECASE)


def sentences(text):
    flat = re.sub(r"\s+", " ", re.sub(r"^\s*([-*•#>]|\d+[.)])\s*", "", text, flags=re.MULTILINE))
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", flat) if len(s.split()) >= 3]


def analyse(text):
    lines = text.splitlines()
    hits = []
    for n, line in enumerate(lines, 1):
        for cat, label, rx in COMPILED:
            for m in rx.finditer(line):
                hits.append({"line": n, "category": cat, "label": label, "match": m.group(0).strip()})
        for m in TRIPLET.finditer(line):
            hits.append({"line": n, "category": "template", "label": "group of three", "match": m.group(0)})

    words = len(re.findall(r"\b\w+\b", text)) or 1
    nonblank = [l for l in lines if l.strip()] or [""]
    sents = sentences(text)
    lengths = [len(s.split()) for s in sents]

    stats = {
        "words": words,
        "em_dashes": len(EM_DASH.findall(text)),
        "bold_spans": len(BOLD.findall(text)),
        "bullet_lines": sum(bool(BULLET.match(l)) for l in nonblank),
        "headings": sum(bool(HEADING.match(l)) for l in nonblank),
        "emoji": len(EMOJI.findall(text)),
        "sentences": len(lengths),
        "mean_sentence_len": round(statistics.mean(lengths), 1) if lengths else 0,
        "sentence_len_variation": round(statistics.pstdev(lengths) / statistics.mean(lengths), 2) if len(lengths) > 1 else None,
        "contractions": len(CONTRACTION.findall(text)),
        "uncontracted": len(CONTRACTABLE.findall(text)),
    }

    warnings = []
    per100 = 100 / words
    if stats["em_dashes"] > 1:
        warnings.append(f"{stats['em_dashes']} em dashes. Aim for 0-1; use commas, full stops, colons or brackets.")
    if stats["bold_spans"] >= 3:
        warnings.append(f"{stats['bold_spans']} bold spans. Bold scattered through prose reads as AI formatting.")
    if stats["bullet_lines"] > 0 and stats["bullet_lines"] / len(nonblank) > 0.5 and words < 400:
        warnings.append("More than half the lines are bullets in a short piece. Consider prose.")
    if stats["headings"] and words < 300:
        warnings.append(f"{stats['headings']} heading(s) in under 300 words. Short pieces don't need headings.")
    if stats["emoji"]:
        warnings.append(f"{stats['emoji']} emoji. Remove unless the register is genuinely casual.")
    v = stats["sentence_len_variation"]
    if v is not None and stats["sentences"] >= 6 and v < 0.35:
        warnings.append(f"Sentence lengths are very uniform (variation {v}). Mix short and long sentences.")
    if stats["uncontracted"] >= 3 and stats["contractions"] < stats["uncontracted"] / 2:
        warnings.append(f"{stats['uncontracted']} uncontracted forms vs {stats['contractions']} contractions. "
                        "Use contractions unless the register is formal.")

    # Score: weighted hits per 100 words plus warnings. Rough, for comparing drafts.
    weights = {"opener": 3, "closer": 3, "template": 2, "vocab": 1, "fiction": 2}
    raw = sum(weights.get(h["category"], 1) for h in hits) * per100 * 10 + len(warnings) * 5 + max(0, stats["em_dashes"] - 1) * 2
    score = min(100, round(raw))
    return {"score": score, "hits": hits, "warnings": warnings, "stats": stats}


def report(result):
    out = []
    s = result["score"]
    verdict = "clean" if s < 10 else "a few tells" if s < 25 else "noticeably AI-flavoured" if s < 50 else "heavy AI tells"
    out.append(f"AI-tell score: {s}/100 ({verdict})")
    st = result["stats"]
    out.append(f"{st['words']} words, {st['sentences']} sentences, mean {st['mean_sentence_len']} words/sentence, "
               f"length variation {st['sentence_len_variation']}")
    if result["warnings"]:
        out.append("\nDocument-level:")
        out.extend(f"  - {w}" for w in result["warnings"])
    if result["hits"]:
        out.append("\nLine-level:")
        for h in sorted(result["hits"], key=lambda h: (h["line"], h["category"])):
            out.append(f"  L{h['line']:<4} [{h['category']}] {h['label']}: \"{h['match']}\"")
    if not result["warnings"] and not result["hits"]:
        out.append("\nNo mechanical tells found. Now reread it for substance: is there a point, and specifics?")
    return "\n".join(out)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    text = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    result = analyse(text)
    print(json.dumps(result, indent=2) if "--json" in argv else report(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
