# Cooperative games

A **characteristic function game** is a pair \((N, v)\), where \(N\) is a set of
\(n\) players and the characteristic function \(v\) maps every coalition
\(C \subseteq N\) to a value \(v(C)\), with \(v(\emptyset) = 0\). The value
\(v(C)\) is interpreted as the worth the coalition \(C\) can secure on its own.
In `coopgt` a characteristic function is a dictionary whose keys are the
coalitions, written as sorted tuples of players numbered from 1.

## Properties of games

Two standard structural properties are **monotonicity**
(\(v(C_1) \leq v(C_2)\) whenever \(C_1 \subseteq C_2\)) and **superadditivity**
(\(v(C_1 \cup C_2) \geq v(C_1) + v(C_2)\) for disjoint \(C_1, C_2\)). A stronger
property is **convexity** (supermodularity):

\[
v(S \cup T) + v(S \cap T) \geq v(S) + v(T) \quad \text{for all } S, T.
\]

## Sharing the value

Once the grand coalition \(N\) forms and secures \(v(N)\), the question is how
to divide it. `coopgt` provides two complementary answers.

The **Shapley value** allocates to each player their average marginal
contribution over all orderings of the players. It is the unique allocation
satisfying efficiency, the null-player property, symmetry, and additivity, and
so captures a notion of fairness.

The **core** captures stability rather than fairness. A payoff vector \(x\) is in
the core if it is efficient, \(\sum_{i \in N} x_i = v(N)\), and no coalition can
improve on its allocation, \(\sum_{i \in C} x_i \geq v(C)\) for every coalition
\(C\). The core can be empty, but for convex games it is always non-empty and
contains the Shapley value.

A weaker requirement is that of an **imputation**: an efficient and individually
rational payoff vector, \(x_i \geq v(\{i\})\) for every player \(i\). Every core
allocation is an imputation, but not conversely.
