#!/usr/bin/env python3

def return_evens(sequence):
    evens = [num for num in sequence if num % 2 == 0]
    return evens

result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Output: [0, 8]

def make_exclamation(sentences):
    exclamations = [sentence + "!" for sentence in sentences]
    return exclamations

result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)  # Output: ["Hello!", "I'm doing great!", "Python is fun!"]