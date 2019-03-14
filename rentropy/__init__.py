"""rentropy -- a small wrapper around an entropy implementation in rust

There are other ways to compute the entropy, but as discussed on StackOverflow_,
this is either slow or requires numpy.

.. _StackOverflow: https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
"""
from .rentropy import _eta


def eta(inp):
    """Computes the Shannon entropy of bytes."""
    _eta(inp)
