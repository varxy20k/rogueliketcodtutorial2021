from typing import Optional

import tcod.event

from rogueliketcodtutorial2021.actions import Action, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        key = event.sym

        if key == tcod.event.K_UP:
            return MovementAction(0, -1)

        return None
