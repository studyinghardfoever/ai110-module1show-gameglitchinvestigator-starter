# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - When I first ran the game, it showed "Attempts left: 7" even though
  8 attempts were allowed and I had not made any guess yet.
- The hints were backwards: guessing 50 when the secret was 85 told me
  to "Go LOWER" instead of "Go HIGHER".

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|New game (no guess) | Attempts left: 8 | Attempts left: 7 (Attempts=1, History empty) | No error |
| Guess 50 (secret 85) | Hint: "Go HIGHER" | Hint: "Go LOWER"(secret cast to str on even turns, so int>str raises TypeError and falls back to string comparison) | No error |
| Win with guess 85 | Score matches debug | Debug Score: -10 but Final score: 40 | No error |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used both ChatGPT and Claude as pair programmers on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct suggestion:
When I asked why the secret number seemed to change on every submit and why the hints were unreliable, Claude pointed me to the block where the code casts secret to a string on even-numbered guesses (if attempts % 2 == 0: secret = str(secret)). It explained that comparing an int guess to a str secret makes guess == secret always False and makes guess > secret raise a TypeError, which then falls back to comparing the numbers as strings by dictionary order. I verified this by playing on an even-numbered turn and watching the hint point in the wrong direction exactly as predicted, confirming the root cause was the type mismatch rather than the secret actually changing.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One incorrect or misleading suggestion:
On my first question about the broken hints, the AI's initial answer did not catch the real cause — it never mentioned that the code was comparing an int against a str, so its explanation was incomplete and would have sent me looking in the wrong place. Only after I asked a more specific follow-up question did it identify the type mismatch and the string-comparison fallback. I verified the corrected explanation by reading the check_guess function line by line and confirming that the except TypeError branch was doing string comparison, which matched the wrong-direction hints I saw in the game. This taught me not to trust a first AI answer at face value and to push back with a sharper question when something doesn't add up.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
