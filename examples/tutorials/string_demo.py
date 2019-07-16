"""The **string_demo** problem solved with a genetic algorithm.

A simple benchmark that is designed to deomonstrate a PushGP's string manipulation
capabilities. The goal of the problem is as follows:

Take the input string, remove the last 2 characters, and then concat this
result with itself.

By default, the error function will be the Damerau-Levenshtein Distance.

NOTICE: This problem file is run during PyshGP's CI tests as validation tests.
For this reason, the hyperparameters that contribute the most to runtime are kept
aritifically low. To see the best search performance, consider increasing
population size, max generations, and initial_genome_size.

"""
import logging
import numpy as np
import random
import sys

from pyshgp.gp.estimators import PushEstimator
from pyshgp.gp.genome import GeneSpawner
from pyshgp.push.instruction_set import InstructionSet


def target_function(s):
    """Generate a training data point."""
    return s[:-2] + s[:-2]


X = np.array([
    "abcde", "", "E", "Hi", "Tom", "leprechaun", "zoomzoomzoom",
    "qwertyuiopasd", "GallopTrotCanter", "Quinona", "_abc"
]).reshape(-1, 1)
y = np.array([[target_function(s[0])] for s in X])


instruction_set = (
    InstructionSet()
    .register_core_by_stack({"str", "int"})
    .register_n_inputs(X.shape[1])
)


spawner = GeneSpawner(
    instruction_set=instruction_set,
    literals=[],
    erc_generators=[
        lambda: random.randint(0, 10),
    ]
)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        stream=sys.stdout
    )

    est = PushEstimator(
        spawner=spawner,
        population_size=200,
        max_generations=30,
        initial_genome_size=(10, 50),
        parallelism=False,
        verbose=2
    )

    est.fit(X=X, y=y)
    print(est._result.program)
    print(est.predict(X))
    print(est.score(X, y))
