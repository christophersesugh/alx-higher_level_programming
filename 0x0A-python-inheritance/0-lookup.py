#!/usr/bin/python3
"""Implements lookup functio."""


def lookup(obj):
    """
    Returns all the attributs of a class.

    Args:
        obj (class): class of which its attirbutes is to be returned.

    Return:
        objlist (list): list of attributes
    """
    objlist = []
    for attribute in dir(obj()):
        objlist.append(attribute)
    return objlist
