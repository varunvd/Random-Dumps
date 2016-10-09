#!/usr/bin/python
from PyDictionary import PyDictionary 
a=raw_input("Enter the word\n")
dictionary=PyDictionary()
answer=dict()
answer=dictionary.meaning(a)
print answer
