from __future__ import print_function
import sys

def my_print(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)
    
my_print("abc","xyz","mno",sep="--")