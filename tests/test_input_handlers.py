import pytest
import tcod.event

from rogueliketcodtutorial2021.input_handlers import EventHandler


def test_ev_quit_raises_system_exit() -> None:
    handler = EventHandler()

    event = tcod.event.Quit()

    with pytest.raises(SystemExit):
        handler.ev_quit(event)


def test_ev_keydown_returns_none_if_no_match() -> None:
    handler = EventHandler()

    event = tcod.event.KeyDown(0, 0, 0)

    assert handler.ev_keydown(event) is None
