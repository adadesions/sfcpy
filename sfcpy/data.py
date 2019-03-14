"""
    Getting data in package
"""
from sfcpy import DATA_PATH

def data(filename):
    return str(DATA_PATH+filename)
