# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ex6.py
# Time       ：12/26/2021 10:05 PM
# Author     ：author name
# version    ：python 3.8
# Description：
"""
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
