"""
Tests for the core related functions.
"""

import coopgt.core

convex_game = {
    (): 0,
    (1,): 1,
    (2,): 1,
    (3,): 1,
    (1, 2): 4,
    (1, 3): 4,
    (2, 3): 4,
    (1, 2, 3): 9,
}

majority_game = {
    (): 0,
    (1,): 0,
    (2,): 0,
    (3,): 0,
    (1, 2): 1,
    (1, 3): 1,
    (2, 3): 1,
    (1, 2, 3): 1,
}


def test_is_imputation_true():
    assert coopgt.core.is_imputation(convex_game, (3, 3, 3)) is True


def test_is_imputation_with_given_number_of_players():
    assert (
        coopgt.core.is_imputation(convex_game, (3, 3, 3), number_of_players=3) is True
    )


def test_is_imputation_false_when_not_efficient():
    assert coopgt.core.is_imputation(convex_game, (3, 3, 2)) is False


def test_is_imputation_false_when_not_individually_rational():
    cf = {(): 0, (1,): 5, (2,): 0, (1, 2): 5}
    assert coopgt.core.is_imputation(cf, (4, 1)) is False


def test_is_in_core_true():
    assert coopgt.core.is_in_core(convex_game, (3, 3, 3)) is True


def test_is_in_core_with_given_number_of_players():
    assert coopgt.core.is_in_core(convex_game, (3, 3, 3), number_of_players=3) is True


def test_is_in_core_false_when_not_efficient():
    assert coopgt.core.is_in_core(convex_game, (3, 3, 2)) is False


def test_is_in_core_false_when_a_coalition_can_improve():
    assert coopgt.core.is_in_core(convex_game, (9, 0, 0)) is False


def test_is_in_core_false_for_empty_core_game():
    assert coopgt.core.is_in_core(majority_game, (1 / 3, 1 / 3, 1 / 3)) is False


def test_is_convex_true():
    assert coopgt.core.is_convex(convex_game) is True


def test_is_convex_false():
    assert coopgt.core.is_convex(majority_game) is False


def test_find_core_point_returns_a_core_point():
    point = coopgt.core.find_core_point(convex_game)
    assert coopgt.core.is_in_core(convex_game, point)


def test_find_core_point_with_given_number_of_players():
    point = coopgt.core.find_core_point(convex_game, number_of_players=3)
    assert coopgt.core.is_in_core(convex_game, point)


def test_find_core_point_returns_none_for_empty_core():
    assert coopgt.core.find_core_point(majority_game) is None
