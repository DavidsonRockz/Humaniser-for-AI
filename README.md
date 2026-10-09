# Humaniser for AI

A Claude skill that writes and rewrites text so it doesn't read like a chatbot wrote it.

It targets the things people complain about most in AI writing: em dashes everywhere, "it's not X, it's Y", everything in threes, "delve / tapestry / testament", "Great question!" openers, "In conclusion" recaps, bullet points for a two-line answer, hedging, fake enthusiasm, and confident text that says nothing specific.

## Where the rules come from

The pattern catalogue is built from three Reddit threads about what makes AI writing irritating:
- [r/WritingWithAI: Why is AI so bad at writing?](https://www.reddit.com/r/WritingWithAI/comments/1uvqg0f/why_is_ai_so_bad_at_writing/), mostly about fiction: subtext, specificity, stock emotions, and the setup/reveal/metaphor formula
- [r/Productivitycafe: Why is AI generated text so irritating](https://www.reddit.com/r/Productivitycafe/comments/1ret6bf/why_is_ai_generated_text_so_irritating/), about the chatbot voice: platitudes, over-explaining, bullet-point segmentation, follow-up menus
- [r/NoStupidQuestions: Why is AI so bad with text?](https://www.reddit.com/r/NoStupidQuestions/comments/1phl0ne/why_is_ai_so_bad_with_text/), which turned out to be about lettering in AI images, so it contributed little

It also draws on widely shared lists of AI tells. Quotes from the threads are marked *(thread)* in `references/patterns.md`.

## What's in it

```
.claude/skills/humaniser/
├── SKILL.md                 # the workflow Claude follows
├── references/patterns.md   # catalogue of AI tells: what, why it grates, what to do instead
└── scripts/check.py         # lint script that flags mechanical tells with line numbers
```

The skill puts substance before surface. Cutting filler, adding specifics and committing to a point does more than swapping out words. It also warns against overcorrecting, like fake typos, forced slang or thesaurus swaps.

## Install

**Claude Code, this repo only:** it already works. Open the repo and the skill is picked up from `.claude/skills/`.

**Claude Code, everywhere:**
```bash
cp -r .claude/skills/humaniser ~/.claude/skills/
```

**Claude.ai / desktop app:** zip the `humaniser` folder and upload it under Settings → Capabilities → Skills.

## Use

Ask naturally, for example "humanise this", "make this sound less like AI", or "write a reply to this email". You can also invoke it with `/humaniser`.

Run the checker on any text yourself:

```bash
python3 .claude/skills/humaniser/scripts/check.py draft.txt
pbpaste | python3 .claude/skills/humaniser/scripts/check.py -
python3 .claude/skills/humaniser/scripts/check.py draft.txt --json
```

It needs only Python 3 with the standard library. The score is rough and meant for comparing drafts, not for proving anything. It can't tell whether the text actually has a point.

## Extending

Add new pet peeves to `references/patterns.md` (there's a "Thread-specific notes" section at the bottom). If one is mechanically detectable, add a regex to `RULES` in `scripts/check.py`.
