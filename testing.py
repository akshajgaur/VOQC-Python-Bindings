import ctypes
testlib = ctypes.CDLL('./main.so')
testlib.myprint()
