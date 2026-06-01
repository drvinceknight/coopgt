# Shapley value regression

The Shapley value is a cooperative game theoretic tool used to share a resource
between players. In this tutorial we use it to measure the importance of the
explanatory variables in a linear regression, a technique often called
**Shapley value regression**.

## The setup

We want to predict a variable \(y\) from three explanatory variables using a
linear model:

\[
y = c_1 x_1 + c_2 x_2 + c_3 x_3.
\]

For every subset of the variables we fit a linear model and record its
\(R^2\) value. The variables are the players, and the value of a coalition is
the \(R^2\) of the model that uses exactly those variables:

| Model | \(R^2\) |
| --- | --- |
| \(y = c_1 x_1\) | 0.075 |
| \(y = c_2 x_2\) | 0.086 |
| \(y = c_3 x_3\) | 0.629 |
| \(y = c_1 x_1 + c_2 x_2\) | 0.163 |
| \(y = c_1 x_1 + c_3 x_3\) | 0.630 |
| \(y = c_2 x_2 + c_3 x_3\) | 0.906 |
| \(y = c_1 x_1 + c_2 x_2 + c_3 x_3\) | 0.907 |

## The characteristic function

We translate that table into a characteristic function, mapping each coalition
to its \(R^2\) value (the empty model explains nothing):

```python
>>> characteristic_function = {
...     (): 0,
...     (1,): 0.075,
...     (2,): 0.086,
...     (3,): 0.629,
...     (1, 2): 0.163,
...     (1, 3): 0.630,
...     (2, 3): 0.906,
...     (1, 2, 3): 0.907,
... }

```

## Sharing the explained variance

The Shapley value shares the total explained variance \(R^2 = 0.907\) between
the three variables, attributing to each its average marginal contribution:

```python
>>> import coopgt.shapley_value
>>> shapley = coopgt.shapley_value.calculate(characteristic_function)
>>> [round(float(value), 3) for value in shapley]
[0.038, 0.182, 0.687]

```

The three contributions sum to the \(R^2\) of the full model:

```python
>>> round(float(sum(shapley)), 3)
0.907

```

The third variable is by far the most important, and the first contributes
least, which matches the intuition that \(x_3\) alone already explains most of
the variance.
