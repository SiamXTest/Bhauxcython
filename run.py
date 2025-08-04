import ctypes

# Load the .so file (ensure it's in same folder or provide full path)
lib = ctypes.CDLL("./312.so")

# If the .so file has a function (like say_hello), call it
lib.say_hello()
