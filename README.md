# PyPythia [![Build Status](https://travis-ci.org/ChristianSch/PyPythia.svg?branch=master)](https://travis-ci.org/ChristianSch/PyPythia)
Python library for the Pythia platform.

## Installation
You can fetch the `pypythia module via pip::
```
pip install pypythia
```

## Usage

Simple example:

```
from pypythia import Experiment

# init experiment

# implies that an instance of Pythia is listening on localhost
exp = Experiment('http://localhost:5667/api/v1/')

exp.name = "some catchy name"
exp.description = "describe the experiment here"

# create a model
model = exp.create_model()
model.name = "2 layers foo bar dropout softmax"

for i in range(NUM_EPOCHS):
    for j in range(NUM_EXAMPLES):
        # the following two lines are not really valid
        train_classifier()
        train_accuracy = accuracy(classifier)

        # save the measured training accuracy
        model.add_measurement(name='train_accuracy',
                              value=train_accuracy,
                              step=j,
                              epoch=i)
```

## Examples
* [MNIST ConvNet in Tensorflow](https://github.com/ChristianSch/PyPythia/blob/master/examples/Tensorflow%20MNIST.ipynb)
