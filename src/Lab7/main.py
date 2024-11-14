
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from classes.Application import *

if __name__ == "__main__":
    app = Application()
    app.run()
