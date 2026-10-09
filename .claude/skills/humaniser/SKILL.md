---
name: humaniser
description: Write or rewrite text so it reads like a person wrote it, not a chatbot. Use when drafting emails, posts, essays, replies, fiction, or any prose, or when the user asks to "humanise", "de-AI", make text "sound less like AI", "sound natural", or "less robotic". Targets the specific tics readers complain about - em dash overuse, "it's not X, it's Y", groups of three, "delve/tapestry/testament" vocabulary, sycophantic openers, recap closers, bullet-point overload, hedging, fake enthusiasm, and empty, detail-free filler.
---

# Humaniser

People spot AI text fast, and once they do, they stop reading charitably. The complaints are remarkably consistent: it's padded, it's falsely upbeat, it hedges everything, it says nothing specific, it formats a two-line answer like a slide deck, and it leans on the same handful of words and sentence shapes every time. Readers describe it as "soulless", "corporate", "like a LinkedIn post", "a student padding a word count".

This skill fixes that. The goal isn't to fool a detector. It's to write something a reader doesn't resent.

## The core idea

Most AI tells come from one root cause: **text generated to sound like writing, rather than to say something.** Swapping "delve" for "explore" doesn't fix that. What fixes it is having a point, saying it plainly, and stopping.

So rewriting has two layers:

1. **Substance** (most important): cut what says nothing, add the specific thing a human would know or think, commit to a view.
2. **Surface**: remove the stock words, punctuation habits and sentence templates listed in `references/patterns.md`.

Doing only layer 2 produces text that still feels hollow, just with fewer em dashes.

## Workflow

### 1. Work out the job
Before writing, pin down:
- **Who's reading** and what they already know.
- **What the one point is.** If you can't say it in a sentence, the text will wander.
- **Register.** A Slack reply, a cover letter and a short story need different voices. Match the user's own writing if they've shared any; mirror their spelling (British/American), punctuation and formality.

### 2. Draft (or take the user's draft) and cut
Delete, don't rephrase:
- Openers that react to the request ("Great question!", "Certainly!", "I hope this finds you well").
- Restating the question or announcing what you're about to do ("Let's dive in", "Here's a breakdown").
- Closers that recap what was just said, or offer more help ("In conclusion", "Overall", "I hope this helps! Let me know if…").
- Throat-clearing hedges ("It's important to note that", "It's worth mentioning").
- Any sentence that would survive unchanged in a thousand other documents.

Start with the actual answer. End when the content ends.

### 3. Add what a human would add
This is the step machines skip, and the biggest single difference:
- **Specifics over abstractions.** Names, numbers, dates, places, a real example, the actual error message. "Sales dropped 12% after we raised prices in March" beats "pricing changes can significantly impact revenue".
- **An opinion.** If the user would have one, state it. "I'd go with Postgres" beats "Both options have their merits."
- **Uneven emphasis.** People spend three sentences on what matters and half a clause on what doesn't. AI gives everything equal weight.
- **Honest uncertainty, once, where it applies**: "I'm not sure about the tax side", instead of a blanket of "may", "might", "can potentially".

Never invent specifics. If a detail is needed and you don't have it, leave a clear placeholder like `[number]` or ask.

### 4. Strip the surface tells
Go through `references/patterns.md`. The worst offenders:
- **Em dashes.** Use at most one per piece, and usually none. Use a comma, full stop, colon or brackets instead.
- **"It's not X, it's Y" / "not just X, but Y"** and other set-up-then-reveal shapes. State Y.
- **Groups of three** ("fast, reliable, and scalable"). Use two, or one, or four. Break the habit.
- **Stock vocabulary**: delve, tapestry, testament, realm, landscape, navigate, leverage, robust, seamless, pivotal, crucial, foster, elevate, unlock, journey, game-changer, ever-evolving.
- **Rhetorical question then answer** ("The result? Chaos.", "So what does this mean?").
- **Colon reveals** ("Here's the thing:", "The kicker:").
- **Staccato hype fragments** ("No fluff. No filler. Just results.").
- **Tacked-on "-ing" commentary** (", highlighting the importance of…", ", underscoring its significance").
- **Inflated significance** ("stands as a testament to", "plays a pivotal role in", "marks a significant milestone").

### 5. Fix the shape
- **Formatting should match the medium.** Conversational replies, emails and messages are paragraphs. No headers, no bold scattered through sentences, no bullet lists for things that are really a sentence. Use lists only for genuinely list-shaped content (steps, options to compare, items to buy). No emoji bullets.
- **Vary rhythm.** Mix sentence lengths. Let a paragraph be one line if that's what it needs. AI prose has a metronome feel: every sentence medium-length, every paragraph three to four sentences.
- **Headings in sentence case**, if you use them at all.
- **Use contractions** unless the register is genuinely formal.
- **Length**: shorter than you think. If the user asked a one-line question, the answer is probably one to three lines.

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

Fiction has its own set of tells (see the fiction section of `references/patterns.md`): stock names (Elara, Kael, Lyra, Seraphina), "a voice barely above a whisper", "the air thick with tension", characters explaining their feelings in full sentences, every scene ending on a hopeful, tidy note, and generic sensory filler. Prefer concrete, slightly odd specifics, subtext over stated emotion, dialogue that interrupts and dodges, and endings that don't wrap up with a moral.
