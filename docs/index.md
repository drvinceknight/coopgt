# coopgt

`coopgt` is a Python library for the study of cooperative game theory. It works
with characteristic function games and provides the Shapley value, checks of
standard properties (validity, monotonicity, superadditivity, convexity), and
core membership.

---

## Installation

```bash
python -m pip install coopgt
```

## Where to start

This documentation follows the [Diátaxis](https://diataxis.fr) framework.

- **Tutorials.** Step-by-step lessons for newcomers.
  [Shapley value regression](tutorials/shapley-value-regression.md).
- **How-to guides.** Practical recipes for common tasks.
  [Calculate the Shapley value](how-to/calculate-the-shapley-value.md) and
  [check the core](how-to/check-the-core.md).
- **Reference.** The complete [API reference](reference/api.md).
- **Explanation.** Background on
  [cooperative games](explanation/cooperative-games.md).

## A first example

A characteristic function is a dictionary mapping each coalition (a tuple of
players, numbered from 1) to its value:

```python
>>> import coopgt.shapley_value
>>> characteristic_function = {
...     (): 0,
...     (1,): 0,
...     (2,): 0,
...     (1, 2): 10,
... }
>>> shapley = coopgt.shapley_value.calculate(characteristic_function)
>>> [round(float(value), 2) for value in shapley]
[5.0, 5.0]

```
