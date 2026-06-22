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

I decided a bug was really fixed only after confirming it two ways: in the live game and through automated tests. For the hint-direction bug, I played the game and guessed numbers both above and below the secret, checking that "Go LOWER" and "Go HIGHER" pointed the right way — and I specifically tested an even-numbered guess, since the original bug only broke on even turns. I also wrote pytest cases in tests/test_game_logic.py: for example, check_guess(60, 50) must return "Too High", and update_score(0, "Too High", 1) must return -5. Running python3 -m pytest showed all 6 tests passing, which gave me confidence the logic was correct beyond just one playthrough. AI helped me realize my first tests were comparing the full (outcome, message) tuple against a single string, so I fixed them to check result[0].

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script from top to bottom every time you interact with the page — click a button, type in a box, anything. That means normal Python variables get wiped and recreated on every rerun, so they can't "remember" anything between clicks. st.session_state is the fix: it's a dictionary that survives reruns, so values like the secret number, attempt count, and score persist across interactions. I'd explain it to a friend like this: the script is forgetful and re-reads itself constantly, and session_state is the sticky note it keeps on the fridge so it doesn't lose track of the game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is verifying fixes with both manual testing and automated pytest cases, instead of trusting that code works just because it ran once. One thing I'd do differently with AI is to ask sharper, more specific questions up front — my first vague question about the hints got an incomplete answer, and I only got the real cause after following up. This project changed how I think about AI-generated code: I now treat it as a draft to investigate and verify rather than a finished answer, since the "production-ready" code I started with was full of subtle bugs.