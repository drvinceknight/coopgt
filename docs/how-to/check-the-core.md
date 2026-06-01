# Check the core

The **core** of a cooperative game is the set of efficient payoff vectors that
no coalition can improve upon. The `coopgt.core` module provides checks for core
membership and for the related notions of imputation and convexity.

Consider the convex game \(G = (3, v)\) with

\[
v(C) = \begin{cases}
0 & \text{if } C = \emptyset \\
1 & \text{if } |C| = 1 \\
4 & \text{if } |C| = 2 \\
9 & \text{if } C = \{1, 2, 3\}.
\end{cases}
\]

```python
>>> characteristic_function = {
...     (): 0,
...     (1,): 1,
...     (2,): 1,
...     (3,): 1,
...     (1, 2): 4,
...     (1, 3): 4,
...     (2, 3): 4,
...     (1, 2, 3): 9,
... }

```

## Is a payoff vector an imputation?

An **imputation** is efficient and individually rational. The equal split
\((3, 3, 3)\) is an imputation:

```python
>>> import coopgt.core
>>> coopgt.core.is_imputation(characteristic_function, (3, 3, 3))
True

```

## Is a payoff vector in the core?

A payoff vector is in the **core** if it is efficient and no coalition can do
better on its own. The equal split is in the core, but giving everything to
player 1 is not, because the coalition \(\{2, 3\}\) could secure \(4 > 0\):

```python
>>> coopgt.core.is_in_core(characteristic_function, (3, 3, 3))
True
>>> coopgt.core.is_in_core(characteristic_function, (9, 0, 0))
False

```

## Is the game convex?

A game is **convex** (supermodular) when
\(v(S \cup T) + v(S \cap T) \geq v(S) + v(T)\) for all coalitions \(S\) and
\(T\). Convex games always have a non-empty core:

```python
>>> coopgt.core.is_convex(characteristic_function)
True

```

## Find a point in the core

By the Bondareva--Shapley theorem the core is non-empty exactly when the game is
balanced. `find_core_point` solves the corresponding linear program and returns
a point of the core, or `None` if the core is empty:

```python
>>> point = coopgt.core.find_core_point(characteristic_function)
>>> coopgt.core.is_in_core(characteristic_function, point)
True

```

For the three-player majority game, in which any two players can claim the whole
value, the core is empty and the function returns `None`:

```python
>>> majority_game = {
...     (): 0, (1,): 0, (2,): 0, (3,): 0,
...     (1, 2): 1, (1, 3): 1, (2, 3): 1, (1, 2, 3): 1,
... }
>>> coopgt.core.find_core_point(majority_game) is None
True

```
