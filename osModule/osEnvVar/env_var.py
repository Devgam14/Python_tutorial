import os

print(os.environ) ## shows all the envs in your device 
print(os.environ.get("BUNDLED_DEBUGPY_PATH")) ### shows the path of the env
os.environ["MY_VAr"] = "Hello" ## set variable