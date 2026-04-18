import math
import os
# there are two type module in python
# 1. built -in  module
# 2. external module
# math prdefined module in python
print(math.sqrt(16))
# print(os.getcwd())


# create a own module
import myModule
myModule.hellow() 

# external module
import requests
response = requests.get("https://www.google.com")