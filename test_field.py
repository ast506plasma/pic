from Field import *
#import Grid at some point

class Grid:
    def __init__(self, xmin, xmax, ncells):
        self.size = (xmax - xmin) / ncells

def test_field_basic():
    Ngrid = 100
