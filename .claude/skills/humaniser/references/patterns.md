# AI writing tells: pattern catalogue

This is a catalogue of the habits readers name when they say text "sounds like AI". Each entry gives the pattern, why it grates, and what to do instead.

Sources: three Reddit threads, r/WritingWithAI "Why is AI so bad at writing?", r/Productivitycafe "Why is AI generated text so irritating", and r/NoStupidQuestions "Why is AI so bad with text?" (which turned out to be about lettering in AI images, so it contributed little), plus widely shared lists of AI tells. Quotes from the threads are marked *(thread)*. A summary of what the threads said is at the bottom.

`scripts/check.py` detects the mechanical ones automatically. The others need judgement.

---

## 0. The principle: frequency, not existence

Every pattern here is a legitimate device that good human writers use. One commenter listed "not X, but Y" lines from JFK, Churchill, Obama and Mandela; others said they now get accused of being AI for using em dashes or negation. The tell is the **machine's inability to leave a pattern alone**:

> "A human writer — even a mediocre one — gets bored of their own habits and instinctively varies them. AI does the opposite: once it settles into a rhythm or a favorite construction, it keeps returning to the same well." *(thread)*

So the rule is: **use any device at most once per piece**, and check across the whole text, not paragraph by paragraph. AI can "fake competence for a few pages, then the pattern exposes it."

---

## 1. Openers and closers

**Sycophantic or reactive openers**
- "Great question!", "That's a surprisingly common reaction 😄", "Certainly!", "Absolutely!"
- "I'd be happy to help with that." / "I hope this email finds you well."
- Instead: start with the answer or the reason for writing.

**Announcing the structure**
- "Here are the main reasons:", "Let's break it down.", "Let's dive in.", "In this article, we will explore…"
- A thread parody opened with exactly "Hmm — Good question! 🤪 Let's see if we can break it down." Everyone recognised it.
- Instead: just do it.

**Recap closers**
- "In conclusion,", "Overall,", "Ultimately,", a "The deeper reason" section that restates everything.
- Instead: stop after the last real point.

**Help-desk sign-offs and follow-up menus**
- "Let me know if you have any other questions!", "I hope this helps!"
- The follow-up menu: "If you want, tell me what kind of AI text annoys you most — corporate tone? motivational fluff? LinkedIn posts? I can break down exactly why…" Both genuine AI replies in the Productivitycafe thread ended this way.
- Instead: nothing. Or one specific next step.

---

## 2. Sentence templates

**Negative parallelism / false contrast**: the most-complained-about construction in the threads.
- "It's not this, it's that." / "Not because… but because…" / "It wasn't X. It was Y."
- "Not X. Not Y. Just Z."
- "This isn't about X. It's about Y." / "Not only… but also…"
- Why: it argues against a claim nobody made so Y sounds profound. One commenter's pizza-order parody: "I don't want pepperoni, I don't want jalapeños, but pepperoni AND jalapeños."
- Instead: **state Y affirmatively**. In fiction: "Replace with one concrete sentence (body/action/object)." *(thread)*

**Anaphora**: consecutive sentences or clauses starting the same way ("We will not… We will not… We're going to… We're going to…").
- Instead: once is rhetoric, three times is a tic. Vary the openings.

**Rule of three**
- "fast, reliable, and scalable"; "Smooth. Simple. Uncanny." (from a thread parody)
- Instead: use the number of items that actually exist.

**Rhetorical question → answer**
- "The result? A 40% boost." / "Why does this matter? Because…"
- Instead: "That boosted output by 40%."

**Colon / "here's" reveals**
- "Here's the thing:", "The bottom line:", "The kicker?"

**Staccato fragments / "AI beat language"**
- "No fluff. No filler. Just results." / "Clipped. Punchy. Dramatic."
- Instead: one normal sentence. Fragments are fine occasionally; a rhythm of them isn't.

**Tacked-on participle commentary**
- "…, highlighting the importance of collaboration." / "…, underscoring its commitment to…"
- Instead: cut it, or make the point properly with evidence.

**Inflated significance / hysteria**
- "stands as a testament to", "plays a pivotal role in", "marks a significant milestone"
- "Unearned over-the-top dramatic emphasis / trying to make everything sound profound." *(thread)*
- "Explains something extremely simple as if it was some genius take." *(thread)*
- Instead: say what it actually did, at the temperature it deserves.

**Faux-profound similes**
- "with the confidence of a man who knows how to sit in a booth", "like a wound", "like a monitor flatlining"
- Instead: only use a comparison if it's precise and you'd be happy defending it. Most sentences don't need one.

**Prepackaged aphorisms**
- "Rights come with responsibilities." "That's the cost of living in a free society." "If not, it's just noise."
- One commenter described it as "every sentence is prepackaged wisdom with zero personality"; another as "Zoltar the fortune teller staring off into the middle distance reciting a script."
- Instead: argue from the specific case in front of you. Cut the fortune-cookie line that sums it up.

---

## 3. Vocabulary

Words over-represented in AI output. One alone is fine; a cluster is a giveaway.

**Verbs**: delve, embark, navigate, leverage, harness, unlock, unleash, elevate, empower, foster, cultivate, bolster, streamline, underscore, showcase, spearhead, resonate.

**Adjectives**: robust, seamless, pivotal, crucial, vital, vibrant, intricate, nuanced, multifaceted, comprehensive, holistic, cutting-edge, transformative, game-changing, ever-evolving, invaluable, unparalleled, meticulous, profound.

**Nouns**: tapestry, testament, realm, landscape, journey, beacon, cornerstone, catalyst, synergy, paradigm, interplay, plethora, myriad, treasure trove.

**Phrases**: "In today's fast-paced world", "It's important to note that", "However, it depends…", "When it comes to", "At the end of the day", "a wide range of", "navigate the complexities of", "Whether you're a beginner or an expert…"

**Pet words**: "absolute/absolutely". One commenter said they're "sick of the word 'absolute' due to how it uses every four sentences."

**Decorative adverbs**: "It's the use of adjectives like *silently* that no one was talking about." *(thread)* Watch for silently, softly, quietly, gently, slowly, deeply attached to verbs that don't need them.

**Intensifiers**: truly, incredibly, remarkably, deeply, genuinely.

Fix: use the plainest accurate word, or nothing.

---

## 4. Punctuation and typography

**Em dashes (—)**: the most-cited tell overall. At most one per piece. One writer's rule: allow them only "for a hard interruption mid-sentence, or a thought cut off in panic" *(thread)*. Otherwise use a period, comma, colon or brackets.

**Em-dash list headers**: "**Syntax** — generated text seems…" with every item formatted the same way.

**Bold scattered through prose**, **Title Case Headings**, **emoji as decoration** (😄 🔥 🤪 😎). All three showed up in the thread's parody and in the real AI replies.

---

## 5. Structure and formatting

**Neatly segmented, balanced, over-explained**: the original poster's summary of an AI reply was "thanks for writing a neatly segmented, balanced, over explained post about how neatly segmented, balanced writing is irritating." Symptoms:
- headed sections each with an identical bullet list
- "balanced pros/cons, symmetrical phrasing, clear conclusions"
- a short question answered with a numbered essay
- Instead: prose for anything conversational. Lists only for genuinely list-shaped content.

**Over-explaining**: "Add context you didn't ask for. Summarize what you already know." "Stretching 3 sentences into 10." "AI uses too many words, and too much filler." *(thread)*
- Instead: economy. "Great writing does a lot with very few words."

**No point**: "I keep feeling like we'll get to the point but it just never happens." *(thread)*
- Instead: know your one point before you start. Put it early.

**Uniform rhythm / droning cadence**: "The cadence and prose are also dry and boring." *(thread)* Every sentence medium length, every paragraph the same shape.
- Instead: "vary sentence length aggressively" *(thread)*.

**Too smooth / too perfect**: "Grammatically flawless, overly structured, polite to a fault." Humans "vary tone, break rules, interrupt themselves." *(thread)*
- Instead: let the voice have some asymmetry: a short blunt sentence, an aside, a contraction, an opinion. Don't fake errors (see SKILL.md, "Don't overcorrect").

**Drift in long outputs**: "The longer the output, the more it drifts toward its default cadence." *(thread)* Write long pieces in sections of roughly 500-800 words and re-check each one against this list.

---

## 6. Tone

**Corporate / customer-service / LinkedIn voice**: "Sounds like a customer service email." "Echoes LinkedIn-style motivation or blog tone." *(thread)*

**Safety not soul / artificial neutrality**: "Avoid strong opinions… Neutral tone, balanced takes, generic phrasing… bland or evasive." *(thread)*
- Instead: take a position. "Strong opinions are often what make writing interesting."

**Sycophancy / never pushing back**: "It rarely pushes back, it hedges criticism, it avoids sharp, direct statements." *(thread)*

**Over-politeness and hedging**: "It's important to note…", "However, it depends…" "Can feel repetitive, cautious, or patronizing — especially if you just want a direct answer." *(thread)*

**Forced playfulness**: "fun, playful, and oh-so-interesting" with emoji (from the parody).

**Impersonal and generic**: "extremely impersonal and painfully generic" *(thread)*. There's no person behind it: no memories, no stakes, no embarrassment.
- Instead: write from somewhere specific. Whose view is this? What do they know first-hand?

---

## 7. Content

**Generic, specific-free description.** The best example from the threads: ask AI to describe New York and "it won't say it smelled of weed and halal carts. It won't talk about the man in a pimp costume or the smell of piss by the subway… the heat radiates off the metal grates… the sweat and the air conditioning will make you feel chilly and even a little gross." *(thread)*
- Instead: the detail only someone who'd been there would know. If you don't have it, ask the user rather than inventing it.

**Redundant or vague**: "weird, insipid writing" *(thread)*.

**Contrived and safe**: "cliché, obvious, safe, and to-the-point writing" *(thread)*.

**Deterministic**: "always the same names and ideas" *(thread)*. The first idea that comes to mind is the one every other AI output used. Take the second or third.

**Nonsensical metaphors / continuity errors**: "metaphors that don't make sense, problems with spatial and temporal reasoning" *(thread)*.

**Confident fabrication / vague attribution**: invented stats, "studies show". Never invent; use placeholders or ask.

---

## 8. Fiction-specific tells

**Emotion labelling.** The rule from the thread: "If the sentence explains the feeling, it's probably banned; make it do something instead." Feelings should be "carried only by action, timing, expression, voice."

**Stock emotion shorthand**: "knot in my stomach. Lump in my chest. Tingling sensation. Skipped a beat." *(thread)*, plus "a breath she didn't know she was holding", "a shiver ran down her spine", "barely above a whisper", "the air thick with tension", "time stood still", "eyes sparkling with mischief", "a mix of X and Y".
- Instead: find the specific physical or behavioural detail for *this* character in *this* moment.

**No subtext / on-the-nose.** "It prefers on the nose writing." "Reads like a fanfic, super on the nose. Almost like a report… without trusting the reader putting it together." *(thread)*
- Characters state their feelings and motives outright.
- The narration spells out relationships the reader has already worked out ("Molly was my best friend").
- Instead: leave gaps. "Good writing leaves a lot to the imagination, and it's in the spaces in between that you build worlds." *(thread)*

**The four-beat formula.** In a side-by-side test in the thread, two of three models produced the same shape: "(Setup) (Reveal) (Action) (Metaphorical Reprise wrapping it all neatly)". For example, "…let the bus carry her forward into the dark."
- Instead: end on an action, a line of dialogue, or mid-moment. No closing metaphor that sums up the theme.

**Over-explained continuity**: AI insists on accounting for every object ("Wait, this object was with X, now it's with Y… Add a sentence.").

**Purple, clumsy metaphor**: "It tries to invent creative metaphors and similes, but they're clumsy and purple, rarely elegant." *(thread)* ("The math dissolved into static.")

**No idiosyncratic voice**: the threads cite Andy Weir's "A teacher! I'm a schoolteacher! I remember it now!" as a line "AI would never write". Characters should be allowed to be weird, funny, petty and wrong.

**Split dialogue**: "Do not split dialogue. Keep dialogue together and at the start of a paragraph." *(thread)* ("I don't know," she said, "what you want from me.")

**Wiki voice for world-building**: introduce lore "sideways through people: dialogue, rumors, arguments… overheard adults… misinterpretations (often partly wrong). No wiki/lecture voice." *(thread)*

**Stock names**: Elara, Lyra, Kael, Seraphina, Zephyr, Thorne.

---

## 9. Techniques the threads recommend

These go beyond banning words:

1. **Show, don't describe, the voice.** "Feed it 3-4 paragraphs of YOUR writing and ask it to match the voice. Not describe the voice — just show it." If the user has samples, mirror them.
2. **Work in chunks** of 500-800 words for long pieces, checking each one.
3. **Write several takes and pick lines.** "AI is much better at individual lines than sustained voice."
4. **Affirmative syntax.** "Only use affirmative" sentence constructions. Say what is, not what isn't.
5. **Edit as a separate pass.** "Do line edit." The human advantage is "editorial judgment, knowing which lines actually land."
6. **Test, then fix, in a loop.** "If someone comes up with unit tests for writing, then the quality will skyrocket." That's what `scripts/check.py` is for.

---

## Thread summary

**r/WritingWithAI** (92 comments). The original complaint was AI sounding "cringe and repetitive", with "It's not this, it's that" and "Not because… but because…", and "dry and boring" cadence. The most upvoted analysis said AI lacks **specificity and subtext** and leans on stock emotional shorthand. Others added economy (too many words), clumsy purple metaphors, generic setting description, the setup/reveal/action/reprise formula, and the model's tendency to return to its default style even when asked to imitate an author. Several pushed back that "not X but Y" and em dashes are classic human rhetoric, so the problem is overuse. Practical tips: voice samples, banning constructions explicitly, affirmative syntax, short chunks, multiple takes, a hard line edit.

**r/Productivitycafe** (41 comments). The focus was on chatbot-voice irritation: "prepackaged wisdom with zero personality", "impersonal and painfully generic", fortune-teller platitudes, decorative adverbs, "trying to sound smart / deep" while having no point. Two commenters posted genuine AI answers that demonstrated the tells while listing them: emoji opener, "Here are the main ones:", headed sections, bullet lists, "It's important to note", balanced takes, and a closing menu of follow-up questions. People who naturally use em dashes or negation complained about false accusations.

**r/NoStupidQuestions** (8 comments). About misspelled lettering in AI-generated images. Not relevant to prose.
