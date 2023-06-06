#!/usr/bin/python3
def magic_string():
    iteration = magic_string.iteration = getattr(magic_string, 'iteration', 0) + 1
    return "BestSchool" + (", BestSchool" * (iteration - 1))
