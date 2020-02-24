from collections import namedtuple
from typing import TypeVar
from axelrod.action import Action
from axelrod.strategies import LookerUp

C, D = Action.C, Action.D
actions = (C, D)

Plays = namedtuple("Plays", "self_plays, op_plays, op_openings")
Reaction = TypeVar("Reaction", Action, float)


class cord1(LookerUp):
    """
    A lookup table based strategy.

    """

    name = "cord1"

    def __init__(self) -> None:
        params = Plays(self_plays=2, op_plays=2, op_openings=0)
        pattern = "CDCDDCDCCDDCCDCC"
        super().__init__(parameters=params, pattern=pattern, initial_actions=(C,))


class cord2(LookerUp):
    """
    A lookup table based strategy.

    """

    name = "cord2"

    def __init__(self) -> None:
        params = Plays(self_plays=2, op_plays=2, op_openings=0)
        pattern = "CDCDDCDCCCDCCDCC"
        super().__init__(parameters=params, pattern=pattern, initial_actions=(C,))


class cord3(LookerUp):
    """
    A lookup table based strategy.

    """

    name = "cord3"

    def __init__(self) -> None:
        params = Plays(self_plays=2, op_plays=2, op_openings=0)
        pattern = "CDCDDCDDDDDDDDCC"
        super().__init__(parameters=params, pattern=pattern, initial_actions=(C,))


class cord4(LookerUp):
    """
    A lookup table based strategy.

    """

    name = "cord4"

    def __init__(self) -> None:
        params = Plays(self_plays=2, op_plays=2, op_openings=0)
        pattern = "CDCDCDCDDDDCCDCC"
        super().__init__(parameters=params, pattern=pattern, initial_actions=(C,))


class cord5(LookerUp):
    """
    A lookup table based strategy.

    """

    name = "cord5"

    def __init__(self) -> None:
        params = Plays(self_plays=2, op_plays=2, op_openings=0)
        pattern = "CCDCCCDCCDDCCDCC"
        super().__init__(parameters=params, pattern=pattern, initial_actions=(C,))
