import sys
import os

print(sys.executable)
print(sys.path)

try:
    import requests
    print("Success: Requests is found!")
except ImportError:
    print("Failure: Python cannot see Requests.")