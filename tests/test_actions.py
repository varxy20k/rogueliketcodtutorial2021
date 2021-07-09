from rogueliketcodtutorial2021.actions import MovementAction


def test_movement():
    a = MovementAction(5, 5)
    assert a.dx == 5
    assert a.dy == 5
