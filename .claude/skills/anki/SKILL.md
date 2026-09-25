---
name: anki
description: Create a small set of Anki cards (default 5; but stay flexible if the topic requires to do so) on one topic from lecture slides or exercises. Use when asked for Anki cards or flashcards.
---
Input: a slide file and/or exercise file, plus a topic. If the topic is unclear, ask before writing.

## Process
1. Read the source. State in 2–3 lines what the cards will cover.
2. For math-heavy topics, ask what went wrong or felt shaky in the exercises before drafting, unless I've already said.
3. Draft the cards in chat. Wait for feedback, then revise. Never write card files.

## Note types
Pick per card. Default to Cloze; use Basic when the answer is an explanation, a derivation step, or a "why" that doesn't fit a gap.

Cloze fields:
- Text: statement with {{c1::...}} gaps. Paragraph-length context, so the card makes sense on its own.
- Back Extra: intuition, why it holds, common mistake.
- Summary: [SCREENSHOT FIELD — leave empty]

Basic fields:
- Front: a precise question.
- Back: the answer with intuition integrated.
- Summary: [SCREENSHOT FIELD — leave empty]

For each card, name the slide(s) worth screenshotting for the empty field.

## Content priorities
- Math-heavy subjects: exercises first. Cards on methods, on where I made errors in exercises, and on the intuition behind results. Slide content supports this.
- Concepts: test understanding (why, what happens if, how X connects to Y) over bare definitions.
- One core idea per card, max 2 clozes.
- Long derivations: one card per key step or trick, never the whole derivation on one card.

## Output format
Each card under a heading "Card n — Cloze/Basic". Each field in its own code block, so I can copy fields one at a time.
Plain text only, no HTML. Math as MathJax \( ... \) and \[ ... \]. Inside clozes, write `} }` instead of `}}` within math so it doesn't close the cloze.