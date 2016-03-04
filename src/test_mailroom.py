import pytest


test_menu = {
    "thank you",
    "report",
    "list",
    "quit",
}


@pytest.mark.parametrize('n', test_menu)
def test_welcome_prompt(n):
    from mailroom import welcome_prompt
    assert type(welcome_prompt(n)) == str
