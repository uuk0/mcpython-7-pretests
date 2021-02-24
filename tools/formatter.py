import subprocess
import sys
import os


local = os.path.dirname(os.path.dirname(__file__))

subprocess.call([sys.executable, "-m", "black", local])
