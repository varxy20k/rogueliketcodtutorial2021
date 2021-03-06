import pytest
import tcod.event

from rogueliketcodtutorial2021.actions import EscapeAction, MovementAction
from rogueliketcodtutorial2021.input_handlers import EventHandler


def test_ev_quit_raises_system_exit() -> None:
    handler = EventHandler()

    event = tcod.event.Quit()

    with pytest.raises(SystemExit):
        handler.ev_quit(event)


@pytest.mark.parametrize(
    "sym, action",
    [
        (0, None),
        (tcod.event.K_UP, MovementAction(0, -1)),
        (tcod.event.K_DOWN, MovementAction(0, 1)),
        (tcod.event.K_LEFT, MovementAction(-1, 0)),
        (tcod.event.K_RIGHT, MovementAction(1, 0)),
        (tcod.event.K_ESCAPE, EscapeAction()),
    ],
)
def test_ev_keydown_performs_correct_action(sym, action) -> None:
    handler = EventHandler()

    event = tcod.event.KeyDown(0, sym, 0)

    assert handler.ev_keydown(event) == action
