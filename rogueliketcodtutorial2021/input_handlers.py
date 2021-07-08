from typing import Optional

import tcod.event

from rogueliketcodtutorial2021.actions import Action


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
