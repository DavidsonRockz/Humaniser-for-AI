# Humaniser for AI

A Claude skill that writes and rewrites text so it doesn't read like a chatbot wrote it.

It targets the things people complain about most in AI writing: em dashes everywhere, "it's not X, it's Y", everything in threes, "delve / tapestry / testament", "Great question!" openers, "In conclusion" recaps, bullet points for a two-line answer, hedging, fake enthusiasm, and confident text that says nothing specific.

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
