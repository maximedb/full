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
[Open-Domain Dialog Evaluation using Follow-Ups Likelihood](https://aclanthology.org/2022.coling-1.40/)

## Citation
```
@inproceedings{de-bruyn-etal-2022-open,
    title = "Open-Domain Dialog Evaluation Using Follow-Ups Likelihood",
    author = "De Bruyn, Maxime  and
      Lotfi, Ehsan  and
      Buhmann, Jeska  and
      Daelemans, Walter",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.40",
    pages = "496--504",
    abstract = "Automatic evaluation of open-domain dialogs remains an unsolved problem. Existing methods do not correlate strongly with human annotations. In this paper, we present a new automated evaluation method based on the use of follow-ups. We measure the probability that a language model will continue the conversation with a fixed set of follow-ups (e.g. not really relevant here, what are you trying to say?). When compared against twelve existing methods, our new evaluation achieves the highest correlation with human evaluations.",
}
```

## License

`full` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
