import pytest
import tcod.event

from rogueliketcodtutorial2021.input_handlers import EventHandler


def test_ev_quit_raises_system_exit() -> None:
    handler = EventHandler()

    event = tcod.event.Quit()

    with pytest.raises(SystemExit):
        handler.ev_quit(event)
