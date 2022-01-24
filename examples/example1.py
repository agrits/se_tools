#!/usr/bin/python3
import sys
sys.path.append("../")
from system import System

s = System.from_file("system.se")
print(s)
print("\n\n")
print(s.to_latex())
