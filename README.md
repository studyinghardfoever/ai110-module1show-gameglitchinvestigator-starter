# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Describe the game's purpose: A number guessing game where the player guesses a secret number within a range, getting higher/lower hints until they win or run out of attempts.
- Detail which bugs you found: hardcoded range in the prompt, backwards hint direction caused by an int/str type mismatch on even turns, unstable scoring, an off-by-one attempt counter, and New Game not resetting game state.
- Explain what fixes you applied: refactored the logic into logic_utils.py, fixed check_guess to compare numerically with correct hint direction, simplified update_score, set the attempt counter to start at 0, and made New Game reset status, score, and history.


## 📸 Demo Walkthrough

1. The player selects a difficulty (e.g. Easy), and the prompt correctly shows the matching range, "Guess a number between 1 and 20."
2. The player enters a guess of 3. Since the secret is higher, the game shows the hint "📈 Go HIGHER!"
3. The player enters a higher guess. If it is above the secret, the game shows "📉 Go LOWER!", guiding them in the right direction.
4. Each wrong guess subtracts 5 points from the score, and the attempts-left counter decreases correctly.
5. When the player guesses the secret, the game shows a win message with the final score and ends. Clicking "New Game" fully resets the secret, attempts, score, and history so a fresh round can begin.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

​```
$ python3 -m pytest
=============== test session starts ===============
platform darwin -- Python 3.12.6, pytest-9.0.3, pluggy-1.6.0
collected 6 items

tests/test_game_logic.py ......             [100%]

================ 6 passed in 0.01s ================
​```
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
