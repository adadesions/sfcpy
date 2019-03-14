"""
    Space-Filling Curve library for image-processing tasks
"""
import os

HERE = os.path.abspath(os.path.dirname(__file__))

__version__ = "1.2.0"
HC_TABLE_PATH = os.path.join(HERE, "hc_lookup.txt")
DATA_PATH = os.path.join(HERE, "dataset")