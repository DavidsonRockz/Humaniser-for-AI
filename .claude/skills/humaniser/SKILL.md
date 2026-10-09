---
name: humaniser
description: Write or rewrite text so it reads like a person wrote it, not a chatbot. Use when drafting emails, posts, essays, replies, fiction, or any prose, or when the user asks to "humanise", "de-AI", make text "sound less like AI", "sound natural", or "less robotic". Targets the tics readers complain about - em dash overuse, "it's not X, it's Y", groups of three, "delve/tapestry/testament" vocabulary, sycophantic openers, recap closers and follow-up menus, neatly segmented over-explained answers, hedging, prepackaged-wisdom platitudes, and in fiction, emotion labelling, stock feelings and on-the-nose writing with no subtext.
---

# Humaniser

People spot AI text fast, and once they do, they stop reading charitably. The complaints are remarkably consistent. Commenters in the Reddit threads this skill is built from called it "cringe and repetitive", "prepackaged wisdom with zero personality", "impersonal and painfully generic", "neatly segmented, balanced, over explained", and "trying to sound smart / deep" while having "NO POINT". In fiction, the problem is a lack of **specificity and subtext**.

This skill fixes that. The goal isn't to fool a detector. It's to write something a reader doesn't resent.

## The core idea

Most AI tells come from one root cause: **text generated to sound like writing, rather than to say something.** Swapping "delve" for "explore" doesn't fix that. What fixes it is having a point, saying it plainly, and stopping.

So rewriting has two layers:

1. **Substance** (most important): cut what says nothing, add the specific thing a human would know or think, commit to a view.
2. **Surface**: remove the stock words, punctuation habits and sentence templates listed in `references/patterns.md`.

Doing only layer 2 produces text that still feels hollow, just with fewer em dashes.

**Frequency, not existence.** Every pattern in the catalogue is a real device that good writers use. JFK and Churchill used "not X, but Y", and plenty of people use em dashes. What gives AI away is that it "can't leave a pattern alone": it reaches for the same move again and again. So the rule is that any device can appear at most once per piece, checked across the whole text.

## Workflow

### 1. Work out the job
Before writing, pin down:
- **Who's reading** and what they already know.
- **What the one point is.** If you can't say it in a sentence, the text will wander.
- **Register.** A Slack reply, a cover letter and a short story need different voices.
- **Voice samples.** If the user has shared their own writing, match it by imitating the sample itself, not a description of it. Mirror their sentence length, spelling (British/American), punctuation, formality and pet phrases. If they want a long piece in their voice and you have no sample, ask for 3-4 paragraphs.

### 2. Draft (or take the user's draft) and cut
Delete, don't rephrase:
- Openers that react to the request ("Great question!", "Certainly!", "I hope this finds you well").
- Restating the question or announcing what you're about to do ("Let's dive in", "Here's a breakdown").
- Closers that recap what was just said, or offer more help ("In conclusion", "Overall", "I hope this helps! Let me know if…").
- Throat-clearing hedges ("It's important to note that", "However, it depends").
- Context the reader didn't ask for, and explanations of things they already know.
- Fortune-cookie summary lines ("Rights come with responsibilities.", "That's the cost of progress.").
- Any sentence that would survive unchanged in a thousand other documents.

Start with the actual answer. End when the content ends, with no menu of follow-up offers ("If you want, I can also…").

### 3. Add what a human would add
This is the step machines skip, and the biggest single difference:
- **Specifics over abstractions.** Names, numbers, dates, places, a real example, the actual error message. "Sales dropped 12% after we raised prices in March" beats "pricing changes can significantly impact revenue". For description, use the detail only someone who'd been there would know: New York's "weed and halal carts" and "the heat radiat[ing] off the metal grates", not "the bustling energy of the city".
- **The second idea, not the first.** The first name, image or example that comes to mind is the one every AI output uses. Go one step past it.
- **An opinion.** If the user would have one, state it. "I'd go with Postgres" beats "Both options have their merits."
- **Uneven emphasis.** People spend three sentences on what matters and half a clause on what doesn't. AI gives everything equal weight.
- **Honest uncertainty, once, where it applies**: "I'm not sure about the tax side", instead of a blanket of "may", "might", "can potentially".

Never invent specifics. If a detail is needed and you don't have it, leave a clear placeholder like `[number]` or ask.

### 4. Strip the surface tells
Go through `references/patterns.md`. The worst offenders:
- **Em dashes.** Use at most one per piece, and usually none. Use a comma, full stop, colon or brackets instead.
- **Negative parallelism**: "It's not X, it's Y", "Not because… but because…", "Not X. Not Y. Just Z." This was the most-complained-about construction in the threads. Write affirmatively and state Y.
- **Groups of three** ("fast, reliable, and scalable"). Use two, or one, or four. Break the habit.
- **Stock vocabulary**: delve, tapestry, testament, realm, landscape, navigate, leverage, robust, seamless, pivotal, crucial, foster, elevate, unlock, journey, game-changer, ever-evolving.
- **Rhetorical question then answer** ("The result? Chaos.", "So what does this mean?").
- **Colon reveals** ("Here's the thing:", "The kicker:").
- **Staccato hype fragments** ("No fluff. No filler. Just results.").
- **Tacked-on "-ing" commentary** (", highlighting the importance of…", ", underscoring its significance").
- **Inflated significance** ("stands as a testament to", "plays a pivotal role in") and unearned drama that makes simple points sound profound.
- **Faux-profound similes** ("with the confidence of a man who…", "like a wound") and decorative adverbs nobody needed ("silently", "softly").
- **Anaphora**: three sentences in a row starting the same way.
- **Pet words**, especially "absolutely".

### 5. Fix the shape
- **Formatting should match the medium.** Conversational replies, emails and messages are paragraphs. No headers, no bold scattered through sentences, no bullet lists for things that are really a sentence, no "**Label** — explanation" lists. Use lists only for genuinely list-shaped content (steps, options to compare, items to buy). No emoji bullets.
- **Don't balance everything.** Symmetrical pros and cons ending in "it depends" reads as evasive. Pick a side and say what would change your mind.
- **Vary rhythm.** Mix sentence lengths. Let a paragraph be one line if that's what it needs. AI prose has a metronome feel: every sentence medium-length, every paragraph three to four sentences.
- **Headings in sentence case**, if you use them at all.
- **Use contractions** unless the register is genuinely formal.
- **Length**: shorter than you think. If the user asked a one-line question, the answer is probably one to three lines.
- **Long pieces drift.** "The longer the output, the more it drifts toward its default cadence." For anything over about 800 words, write and check in sections, then do a final pass for constructions that repeat across sections.

### 6. Check
Run the checker on your draft:

```bash
python3 .claude/skills/humaniser/scripts/check.py draft.txt
# or
echo "text" | python3 .claude/skills/humaniser/scripts/check.py -
```

It flags the mechanical tells (vocabulary, em dashes, templates, openers, closers, formatting density, sentence-length uniformity) with line numbers. Treat it as a lint pass, not a verdict. A clean score doesn't mean the text is good, and one flagged word in an otherwise solid paragraph is fine.

Then reread once as the intended reader and ask: *would a busy person feel their time was respected?* and *could I tell who wrote this?*

## Don't overcorrect

Readers dislike fake-human writing almost as much as AI writing. Avoid:
- Inserting deliberate typos, random lowercase, or "lol"/"tbh" into a register that doesn't call for it.
- Forced slang, folksy asides, or jokes that weren't asked for.
- Swapping every banned word for a thesaurus synonym, which just produces a new set of tells.
- Making things vague to sound casual. Plain isn't the same as sloppy.
- Rewriting the user's meaning. Keep their facts, claims and intent intact; change how it's said, not what.

## Mode: rewriting someone else's text

When the user pastes text to humanise:
1. Keep every factual claim, name, number and link.
2. Keep their point of view and any strong phrasing that's clearly theirs.
3. Apply steps 2-5.
4. Return the rewrite on its own, with no preamble. Only add a short note after it if you had to cut something substantive or need a detail from them (e.g. "I removed the claim about 40% growth since there was no source. Add it back if it's real.").

## Mode: fiction

Fiction has its own tells (see section 8 of `references/patterns.md`). The rules that matter most:

- **Don't label emotions.** "If the sentence explains the feeling, it's probably banned; make it do something instead." Carry feeling through action, timing, expression and voice.
- **No stock shorthand**: knot in the stomach, lump in the throat, heart skipped a beat, breath she didn't know she was holding, barely above a whisper, the air thick with tension.
- **Subtext, and trust the reader.** Don't have characters state their motives. Don't spell out what the reader has already inferred. Don't account for every object's whereabouts. Leave gaps.
- **Break the four-beat formula**: setup, reveal, reaction, then a closing metaphor that wraps it all up ("…and let the bus carry her forward into the dark"). End on an action, a line of dialogue, or mid-moment instead.
- **Specific, lived sensory detail** over generic sights-sounds-smells.
- **Let characters be odd**: petty, funny, wrong, distracted. A voice AI "would never write" is the goal.
- **Keep dialogue unsplit** ("I don't know," she said, "what you want" becomes "I don't know what you want," she said). Introduce world-building sideways through people, not in a wiki voice.
- **Names**: avoid Elara, Lyra, Kael, Seraphina and friends. Pick names that fit the setting.
- Em dashes only for a hard interruption or a thought cut off mid-panic.
