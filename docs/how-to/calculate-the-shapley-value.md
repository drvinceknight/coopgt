# Calculate the Shapley value

To find the Shapley value of a game \(G = (N, v)\) use
`coopgt.shapley_value.calculate`.

For example, for \(G = (3, v)\) with

\[
v(C) = \begin{cases}
0 & \text{if } C = \emptyset \\
6 & \text{if } C = \{1\} \\
12 & \text{if } C = \{2\} \\
42 & \text{if } C = \{3\} \\
12 & \text{if } C = \{1, 2\} \\
42 & \text{if } C = \{1, 3\} \\
42 & \text{if } C = \{2, 3\} \\
42 & \text{if } C = \{1, 2, 3\}
\end{cases}
\]

first create the characteristic function as a dictionary:

```python
>>> characteristic_function = {
...     (): 0,
...     (1,): 6,
...     (2,): 12,
...     (3,): 42,
...     (1, 2): 12,
...     (1, 3): 42,
...     (2, 3): 42,
...     (1, 2, 3): 42,
... }

```

Then compute the Shapley value:

```python
>>> import coopgt.shapley_value
>>> shapley = coopgt.shapley_value.calculate(characteristic_function)
>>> [round(float(value), 2) for value in shapley]
[2.0, 5.0, 35.0]

```

The \(i\)th entry is the payoff allocated to player \(i\).
