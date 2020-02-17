# use: import
from  .a import *

# user: __all__
__all__=["b", "test"]

def test():
    print("package001:__init__.test")