import tcod

from rogueliketcodtutorial2021.rogueliketcodtutorial2021 import fib


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


def test_main() -> None:
    # If I'm understanding everything correctly,
    # a console is a tile map, and it can be
    # used without a window, so it's perfect
    # for integration tests.
    # Q. Is it possible to draw a console to an image?
    # A. I think that should be a window, but it seems
    # like we can print() a console and save that
    # to a file.
    # Q. Could we use snapshot testing for that?
    # A. If there was an easy way to compare strings
    # that's doable, maybe by overriding some methods,
    # I think there's a way to make the presentation
    # more user friendly in jest, we'd need to see
    # if that's available for python

    # Now I need to figure out how to perform
    # e2e tests, I'd need a way to simulate events
    # (arrow movements at least) and probably a couple
    # of more sanity tests. If I'm able to do most
    # things with a console that could be like the
    # main e2e test instead of integration, as a
    # window is only used to display a console
    # with context.present

    # I don't think I'm ready to work on this,
    # it's likely that further ahead in the tutorial
    # each entity will be in charge of printing itself
    # so that would be a great moment to start testing
    # interactions with the console.
    # Probably modeling this as a state machine or
    # leveraging rule-based stateful testing (which doesn't
    # need a state machine btw)

    # In the end, if I'm capable of switching the
    # presentation layer with another one I'll consider
    # myself successful
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    console = tcod.Console(screen_width, screen_height, order="F")

    console.print(x=player_x, y=player_y, string="@")

    assert console.ch[player_x, player_y] == ord("@")
