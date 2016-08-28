.. Pythia documentation master file, created by
   sphinx-quickstart on Sun Aug 28 10:16:24 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Pythia's documentation!
==================================

Contents:

.. toctree::
   :maxdepth: 2

.. automodule:: pythia

.. autoclass:: Experiment
    :members:

    .. automethod:: __init__

.. autoclass:: Model
    :members:

    .. automethod:: __init__

.. autoclass:: ApiBase
    :members:

Example
=======
.. code-block:: python
    :linenos:
    :emphasize-lines: 6,12,22,23,24

    from pythia import Experiment

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

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
