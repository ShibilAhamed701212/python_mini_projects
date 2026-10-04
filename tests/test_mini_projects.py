"""Unit tests for the pure game logic in each mini project."""

import builtins

import pytest

import dice_rolling_game
import guess_the_number
import name_list_manager
import rock_paper_scissors


def feed_input(monkeypatch, *answers):
    """Replaces input() so it returns the given answers in order."""
    answers = iter(answers)
    monkeypatch.setattr(builtins, "input", lambda _prompt="": next(answers))


def test_roll_dice_returns_requested_count_in_range():
    rolls = dice_rolling_game.roll_dice(50)
    assert len(rolls) == 50
    assert all(1 <= r <= 6 for r in rolls)


@pytest.mark.parametrize(
    ("user", "computer", "expected"),
    [
        ("r", "s", "You Win!"),
        ("s", "p", "You Win!"),
        ("p", "r", "You Win!"),
        ("s", "r", "You Lose!"),
        ("p", "s", "You Lose!"),
        ("r", "p", "You Lose!"),
        ("r", "r", "It's a Draw!"),
    ],
)
def test_determine_winner(user, computer, expected):
    assert rock_paper_scissors.determine_winner(user, computer) == expected


def test_get_user_choice_rejects_invalid_then_accepts(monkeypatch, capsys):
    feed_input(monkeypatch, "x", " P ")
    assert rock_paper_scissors.get_user_choice() == "p"
    assert "Invalid choice" in capsys.readouterr().out


def test_get_valid_int_retries_until_integer(monkeypatch, capsys):
    feed_input(monkeypatch, "abc", "4.5", "-7")
    assert guess_the_number.get_valid_int("? ") == -7
    assert capsys.readouterr().out.count("Invalid input") == 2


@pytest.mark.parametrize(
    ("guess", "secret", "start", "end", "expected"),
    [
        # Regression: these used to be compared against secret/2 and secret*2,
        # which called a one-off guess "way off" around zero and negatives.
        (-1, 0, 0, 10, "Low, but getting closer."),
        (-4, -5, -10, 10, "High, but you're in the neighborhood."),
        (-6, -5, -10, 10, "Low, but getting closer."),
        (1, 50, 1, 100, "Too low! Not even close."),
        (100, 50, 1, 100, "Too high! Way off."),
        (55, 50, 1, 100, "High, but you're in the neighborhood."),
    ],
)
def test_closeness_hint(guess, secret, start, end, expected):
    assert guess_the_number.closeness_hint(guess, secret, start, end) == expected


def test_play_game_rejects_inverted_range(monkeypatch, capsys):
    feed_input(monkeypatch, "10", "1")
    guess_the_number.play_game()
    assert "Range error" in capsys.readouterr().out


def test_play_game_counts_attempts(monkeypatch, capsys):
    monkeypatch.setattr(guess_the_number.random, "randint", lambda a, b: 7)
    feed_input(monkeypatch, "1", "10", "3", "7")
    guess_the_number.play_game()
    assert "found the number 7 in 2 attempts" in capsys.readouterr().out


def test_name_list_manager_add_remove_clear(monkeypatch, capsys):
    feed_input(
        monkeypatch,
        "2", "Ada",
        "2", "  ",
        "1",
        "3", "Bob",
        "3", "Ada",
        "2", "Lin",
        "4", "y",
        "1",
        "9",
        "5",
    )
    name_list_manager.main()
    out = capsys.readouterr().out
    assert "'Ada' added to the list." in out
    assert "Name cannot be empty." in out
    assert "1. Ada" in out
    assert "'Bob' not found in the list." in out
    assert "'Ada' removed." in out
    assert "List cleared." in out
    assert "The list is currently empty." in out
    assert "Invalid choice" in out
