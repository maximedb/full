# FULL

Unsupervised evaluation of open-domain conversations using follow-ups likelihood.

-----

## Installation

```console
pip install full
```

## Example
We provide an example script using FULL which reproduces the results of the paper.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maximedb/full/blob/master/examples/results_reproduction.ipynb)

## Turn evaluation

```python
from full import FULL
eval_model = FULL()
conversation = ["Hi", "What's your name"]
response = "None of your business"
evaluation = eval_model.evaluate_turn(convesation, response)
print(evaluation)
```

## Conversation evaluation

```python
from full import FULL
eval_model = FULL()
conversation = ["Hi", "What's your name", "None of your business"]
evaluation = eval_model.evaluate_turn(convesation)
print(evaluation)
```

## Paper
[Open-Domain Dialog Evaluation using Follow-Ups Likelihood](https://arxiv.org/abs/2209.05185)

## Citation
```
@article{full-mdebruyn,
  doi = {10.48550/ARXIV.2209.05185},
  url = {https://arxiv.org/abs/2209.05185},
  author = {De Bruyn, Maxime and Lotfi, Ehsan and Buhmann, Jeska and Daelemans, Walter},  
  title = {Open-Domain Dialog Evaluation using Follow-Ups Likelihood},
  publisher = {arXiv},
  year = {2022}
}
```

## License

`full` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
