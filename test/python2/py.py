# encoding=utf-8
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
print(parentUrl)

# eg
sys.path.append(parentUrl)

name = raw_input("what is your name?")
if name.endswith('tank'):
    print 'hello tank'
elif name.endswith('xiao'):
    print 'hello xiao'
else:
    print 'hello strange'
