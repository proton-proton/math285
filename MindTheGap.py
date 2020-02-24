from typing import Any, List, Sequence, Tuple, Union
from axelrod.action import Action
from axelrod import FSMPlayer


C, D = Action.C, Action.D
actions = (C, D)
Transition = Tuple[int, Action, int, Action]

class MindTheGap(FSMPlayer):
    """
    Finite state machine player based off of the Central portion of the London Tube map.
    """

    name = "Mind The Gap"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": False,
        "makes_use_of": set(),
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self) -> None:
        transitions = (
            (0, C, 12, D),
            (0, D, 2, D),
            (1, C, 7, D),
            (1, D, 9, D),
            (2, C, 5, C),
            (2, D, 6, D),
            (3, C, 4, D),
            (3, D, 6, C),
            (4, C, 4, D),
            (4, D, 6, D),
            (5, C, 13, D),
            (5, D, 3, D),
            (6, C, 7, C),
            (6, D, 6, C),
            (7, C, 13, D),
            (7, D, 4, D),
            (8, C, 10, D),
            (8, D, 9, D),
            (9, C, 11, D),
            (9, D, 1, D),
            (10, C, 1, C),
            (10, D, 9, D),
            (11, C, 2, D),
            (11, D, 5, D),
            (12, C, 11, C),
            (12, D, 8, C),
            (13, C, 1, D),
            (13, D, 5, D),
        )

        super().__init__(
            transitions=transitions, initial_state=0, initial_action=C
        )
