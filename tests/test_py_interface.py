import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rentropy import eta
import pytest

def test_eta():
    assert eta(b"hello, world") == pytest.approx(3.0220551, 0.0000001)
