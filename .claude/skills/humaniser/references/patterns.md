# AI writing tells: pattern catalogue

This is a catalogue of the habits readers name most often when they say text "sounds like AI". Each entry gives the pattern, why it grates, and what to do instead. Sections run roughly from most to least noticed.

`scripts/check.py` detects the mechanical ones automatically. The others need judgement.

---

## 1. Openers and closers

**Sycophantic or reactive openers**
- "Great question!", "Certainly!", "Absolutely!", "Of course!", "Sure thing!"
- "I'd be happy to help with that."
- "I hope this email finds you well." / "I hope you're doing well."
- Why it grates: it's filler that delays the answer and feels like customer-service script.
- Instead: start with the answer or the reason for writing.

**Restating or announcing**
- "You're asking about X. Let's dive in." / "Here's a comprehensive breakdown."
- "In this article, we will explore…"
- Instead: just do it.

**Recap closers**
- "In conclusion,", "In summary,", "Overall,", "Ultimately,", "All in all,"
- A final paragraph that repeats the three points just made.
- Instead: stop after the last real point. If a takeaway is needed, make it new information (a recommendation or next step), not a recap.

**Help-desk sign-offs**
- "I hope this helps!", "Let me know if you have any other questions!", "Feel free to reach out!", "Happy writing!"
- Instead: nothing. Or a specific next step ("Send me the logs and I'll look.").

---

## 2. Sentence templates

**Negative parallelism / false contrast**
- "It's not just a tool, it's a revolution."
- "This isn't about X. It's about Y."
- "Not only… but also…"
- "It's less about X and more about Y."
- Why: it argues against a claim nobody made, to make Y sound profound. Readers now spot it instantly.
- Instead: say Y directly.

**Rule of three**
- "fast, reliable, and scalable"; "clarity, consistency, and confidence"
- Three examples, three bullet points, three adjectives, every time.
- Instead: use the number of items that actually exist. Two is often stronger.

**Rhetorical question → answer**
- "The result? A 40% boost." / "Why does this matter? Because…" / "So what's the catch?"
- Instead: "That boosted output by 40%."

**Colon / "here's" reveals**
- "Here's the thing:", "Here's why:", "The bottom line:", "The kicker?", "The best part?"
- Instead: drop the setup and state it.

**Staccato hype**
- "No fluff. No filler. Just results."
- "Simple. Powerful. Effective."
- Instead: one normal sentence.

**Tacked-on participle commentary**
- "…, highlighting the importance of collaboration."
- "…, underscoring its commitment to excellence."
- "…, reflecting a broader shift in the industry."
- Why: it pretends to analyse while adding nothing.
- Instead: cut it, or make the actual point in its own sentence with evidence.

**Inflated significance**
- "stands as a testament to", "serves as a reminder that", "plays a vital/pivotal/crucial role in"
- "marks a significant milestone", "paving the way for", "in the ever-evolving landscape of"
- Instead: say what it actually did. "The bridge opened in 1932" not "The bridge stands as an enduring testament to engineering ambition."

**"From X to Y" range sweeps**
- "From startups to Fortune 500 companies…", "from ancient Rome to modern Silicon Valley…"
- Instead: name the specific case you mean.

---

## 3. Vocabulary

Words and phrases strongly over-represented in AI output. One alone is fine; a cluster is a giveaway.

**Verbs**: delve, embark, navigate, leverage, harness, unlock, unleash, elevate, empower, foster, cultivate, bolster, streamline, underscore, showcase, spearhead, revolutionise, resonate, transcend, illuminate.

**Adjectives**: robust, seamless, pivotal, crucial, vital, vibrant, dynamic, intricate, nuanced, multifaceted, comprehensive, holistic, cutting-edge, innovative, transformative, game-changing, ever-evolving, invaluable, unparalleled, meticulous, profound.

**Nouns**: tapestry, testament, realm, landscape, journey, symphony, beacon, cornerstone, catalyst, synergy, paradigm, interplay, plethora, myriad, labyrinth, treasure trove, game-changer.

**Phrases**:
- "In today's fast-paced world", "in today's digital age", "in an era of"
- "It's important to note that", "It's worth noting", "It bears mentioning"
- "When it comes to", "At the end of the day", "a deep dive"
- "plays a crucial role", "a wide range of", "a myriad of", "a plethora of"
- "navigate the complexities of", "the intricacies of"
- "rich tapestry", "delve deeper", "unlock the potential", "take it to the next level"
- "Whether you're a beginner or an expert…"

**Intensifier stacks**: "truly", "incredibly", "deeply", "remarkably", "absolutely", "genuinely" sprinkled through for false warmth.

Fix: use the plainest word that's accurate. "Use" not "leverage". "Important" or nothing, not "pivotal". Often the word can just go.

---

## 4. Punctuation and typography

**Em dashes (—)**: the single most-cited tell. AI uses them constantly for asides and reveals.
- Limit: zero or one per piece. Replace with a comma, full stop, colon, or parentheses.

**Bold scattered through prose**: "This is **really important** for **your workflow**."
- Use bold rarely, for something a skimmer truly must not miss.

**Title Case Headings**: "Key Benefits Of Using This Approach".
- Use sentence case, and only use headings in long documents.

**Emoji as bullets or decoration**: ✅ 🚀 💡 🔥 in professional text.

**Curly-quote / ellipsis characters** (… “ ”) in a context where the user types straight ASCII. Match the user.

---

## 5. Structure and formatting

**Bullet-point everything**: a conversational question answered with headers, bullets, and a bolded summary.
- Prose for anything conversational, an email, a message, or an argument. Lists only when items are genuinely parallel and separate.

**Uniform rhythm**: every sentence 15-25 words, every paragraph 3-4 sentences, every section the same length.
- Vary it. Short sentence. Then a longer one that carries a qualification or an example along with it. Occasionally a one-line paragraph.

**Equal weight on everything**: each point gets the same depth regardless of importance.
- Spend words where the reader needs them.

**Mirrored structure**: every section introduced with a summary sentence, then detail, then a mini-conclusion.

**Excess length**: padding to look thorough. A quick question gets a quick answer.

---

## 6. Tone

**Relentless positivity / fake enthusiasm**: "What a fantastic idea!", "This is an exciting opportunity!", everything is "amazing".
- Match the actual emotional temperature of the situation.

**Sycophancy**: praising the user's question, idea or draft before (or instead of) helping. Agreeing with whatever they said.
- Be direct. If something's wrong, say so politely.

**Hedging everything**: "may", "might", "could potentially", "in some cases", "it depends", "generally speaking", stacked in every sentence.
- Commit where you can. Hedge once, specifically, where the uncertainty is real.

**Both-sidesing**: "While X has benefits, Y also has its merits. Ultimately, the choice depends on your needs."
- Give a recommendation and the condition that would change it.

**Corporate / HR voice**: "We value your feedback and are committed to continuous improvement."
- Write like a specific person talking to another specific person.

**Unrequested moralising and disclaimers**: "It's important to remember to always be respectful…", "Remember, everyone's journey is different."
- Leave out unless the user needs a genuine safety note.

**No personality / no "I"**: an author with no opinions, preferences or experiences.
- When writing as or for the user, let their view through.

**Mock-casual**: "Let's be real", "Honestly?", "Here's the tea", "game-changer, folks" bolted onto otherwise flat text.

---

## 7. Content

**Generic, specific-free claims**: "Communication is key to any successful team."
- Replace with a concrete instance, number, or example, or delete.

**Confident fabrication**: invented statistics, quotes, studies, citations, or "experts say".
- Never invent. Use placeholders or ask.

**Vague attribution**: "Studies show", "Experts agree", "Many people believe", "It is widely regarded".
- Name the source or drop the appeal.

**Surface-level coverage**: listing every consideration without depth on any of them.
- Pick the two that matter and go deeper.

**Saying what things are "about"**: "At its core, this is about trust."
- Show the thing instead.

---

## 8. Fiction-specific tells

**Names**: Elara, Lyra, Kael, Seraphina, Aria, Zephyr, Thorne, Sterling, Blackwood, "Dr. Evelyn Reed". Pick names that fit the setting and era, and aren't the first thing that comes to mind.

**Stock phrases**:
- "a voice barely above a whisper", "a breath she didn't know she was holding"
- "the air thick with tension/anticipation", "a shiver ran down her spine"
- "eyes sparkling with mischief", "a mix of X and Y" (emotions), "a flicker of something"
- "the weight of the world on his shoulders", "time seemed to stand still"
- "Somewhere in the distance, a dog barked."
- "little did they know"

**Stated emotion**: "She felt a deep sense of sadness wash over her." Show it through action, detail or dialogue instead.

**Therapised dialogue**: characters who articulate their feelings in complete, self-aware sentences ("I think I'm afraid of letting people in because of my past"). Real dialogue dodges, interrupts, misunderstands and leaves things unsaid.

**Tidy endings**: every scene closes on reflection, hope, or a lesson learned. Let some scenes end abruptly or unresolved.

**Generic sensory padding**: "the scent of rain and possibility", lists of senses ticked off one by one.

**Everyone is nice**: conflict resolves through a heartfelt talk. Give characters real friction and selfish motives.

**Purple metaphor stacking**: three similes per paragraph, each more abstract than the last.

---

## Thread-specific notes

The source Reddit threads (r/WritingWithAI, r/NoStupidQuestions, r/Productivitycafe) couldn't be fetched when this catalogue was written. Paste notable comments or pet peeves from them here so the skill can draw on them directly.

<!-- Add entries below in the same format: pattern, why it grates, what to do instead. -->
