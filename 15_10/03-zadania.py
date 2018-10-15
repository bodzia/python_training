import os, sys
from pprint import pprint

pprint("working directories: ")
pprint(sys.path, indent=4)
pprint("current directory: ")
pprint(os.getcwd())