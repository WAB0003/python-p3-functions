#!/usr/bin/env python3

#!function in javacript:
# function myFunction(parameters) {
#     console.log("running myFunction")
#     return param+1
# }

# const myFunctionReturnValue = myFunction(1)
# console.log(myFunctionReturnValue)

#! Writing same function in python it's called a method
# def my_function(parameters):
#     print("running my_function")
#     return parameters + 1




def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number/2
