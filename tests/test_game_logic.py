from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_score_decreases_on_wrong_guess():
    # Guessing wrong should subtract 5 points
    result = update_score(0, "Too High", 1)
    assert result == -5


def test_score_increases_on_win():
    # Winning should add points (positive gain)
    result = update_score(0, "Win", 1)
    assert result > 0


def test_score_unchanged_on_empty_outcome():
    # An outcome that is not Win/Too High/Too Low should leave score unchanged
    result = update_score(0, "playing", 0)
    assert result == 0