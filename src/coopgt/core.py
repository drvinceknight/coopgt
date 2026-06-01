"""
Functions to check core related properties of a characteristic function game.
"""

import itertools
from collections.abc import Sequence

import numpy as np
import numpy.typing as npt
import scipy.optimize


def is_imputation(
    characteristic_function: dict,
    payoff_vector: Sequence[float | int],
    number_of_players: int | None = None,
) -> bool:
    """
    Checks whether a payoff vector is an imputation, that is whether it is
    efficient and individually rational.

    Parameters
    ----------
    characteristic_function : dict
        A dictionary mapping elements of the power set of the set of players to
        a payoff value.
    payoff_vector : sequence
        The payoff to each player, ordered so that ``payoff_vector[i - 1]`` is
        the payoff to player ``i``.
    number_of_players : int
        The number of players. If no number of players is given it will be
        calculated from the keys of the function.

    Returns
    -------
    bool
        Whether or not the payoff vector is an imputation.
    """
    if number_of_players is None:
        number_of_players = max(map(len, characteristic_function.keys()))

    players = range(1, number_of_players + 1)
    grand_coalition = tuple(players)

    is_efficient = sum(payoff_vector) == characteristic_function[grand_coalition]
    is_individually_rational = all(
        payoff_vector[player - 1] >= characteristic_function[(player,)]
        for player in players
    )
    return is_efficient and is_individually_rational


def is_in_core(
    characteristic_function: dict,
    payoff_vector: Sequence[float | int],
    number_of_players: int | None = None,
) -> bool:
    """
    Checks whether a payoff vector is in the core, that is whether it is
    efficient and no coalition can improve on its allocation.

    Parameters
    ----------
    characteristic_function : dict
        A dictionary mapping elements of the power set of the set of players to
        a payoff value.
    payoff_vector : sequence
        The payoff to each player, ordered so that ``payoff_vector[i - 1]`` is
        the payoff to player ``i``.
    number_of_players : int
        The number of players. If no number of players is given it will be
        calculated from the keys of the function.

    Returns
    -------
    bool
        Whether or not the payoff vector is in the core.
    """
    if number_of_players is None:
        number_of_players = max(map(len, characteristic_function.keys()))

    grand_coalition = tuple(range(1, number_of_players + 1))

    if sum(payoff_vector) != characteristic_function[grand_coalition]:
        return False

    return all(
        sum(payoff_vector[player - 1] for player in coalition)
        >= characteristic_function[coalition]
        for coalition in characteristic_function.keys()
        if coalition != ()
    )


def is_convex(characteristic_function: dict) -> bool:
    """
    Checks whether a characteristic function is convex (supermodular), that is
    whether ``v(S | T) + v(S & T) >= v(S) + v(T)`` for all coalitions ``S`` and
    ``T``.

    Parameters
    ----------
    characteristic_function : dict
        A dictionary mapping elements of the power set of the set of players to
        a payoff value.

    Returns
    -------
    bool
        Whether or not the characteristic function is convex.
    """
    for S_1, S_2 in itertools.combinations_with_replacement(
        characteristic_function.keys(), 2
    ):
        union = tuple(sorted(set(S_1) | set(S_2)))
        intersection = tuple(sorted(set(S_1) & set(S_2)))
        if (
            characteristic_function[union] + characteristic_function[intersection]
            < characteristic_function[S_1] + characteristic_function[S_2]
        ):
            return False
    return True


def find_core_point(
    characteristic_function: dict,
    number_of_players: int | None = None,
) -> npt.NDArray | None:
    """
    Finds a payoff vector in the core, or returns ``None`` if the core is empty.

    This solves the Bondareva--Shapley linear program: minimise the total payout
    subject to every coalition receiving at least its value. The core is
    non-empty if and only if this minimum equals ``v(N)``, in which case the
    minimiser is a point of the core.

    Parameters
    ----------
    characteristic_function : dict
        A dictionary mapping elements of the power set of the set of players to
        a payoff value.
    number_of_players : int
        The number of players. If no number of players is given it will be
        calculated from the keys of the function.

    Returns
    -------
    numpy.ndarray or None
        A payoff vector in the core, or ``None`` if the core is empty.
    """
    if number_of_players is None:
        number_of_players = max(map(len, characteristic_function.keys()))

    players = range(1, number_of_players + 1)
    grand_coalition = tuple(players)
    coalitions = [coalition for coalition in characteristic_function if coalition != ()]

    coalitional_rationality = [
        [-1 if player in coalition else 0 for player in players]
        for coalition in coalitions
    ]
    values = [-characteristic_function[coalition] for coalition in coalitions]

    result = scipy.optimize.linprog(
        c=np.ones(number_of_players),
        A_ub=coalitional_rationality,
        b_ub=values,
        bounds=(None, None),
    )
    if np.isclose(result.fun, characteristic_function[grand_coalition]):
        return result.x
    return None
