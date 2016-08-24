# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:36:03 2016

@author: Eddie
"""
import math

import pysh_globals as g

def safe_cast_arg(arg, typ = int):
    try:
        return typ(arg)
    except Exception, e:
        if typ == int:
            safe_cast_arg(arg, float)
        elif typ == float:
            safe_cast_arg(arg, bool)
        else:
            return str(arg)

def flatten_all(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result += flatten_all(i)
        else:
            result += i
    return result


def recognize_pysh_type(thing):
    '''
    If thing is a literal, return its type -- otherwise return False.
    '''
    if type(thing) is str and len(thing) > 0 and thing[0] == '_':
        return '_instruction'
    elif type(thing) is int:
        return '_integer'
    elif type(thing) is float:
        return '_float'
    elif type(thing) is str:
        return '_string'
    elif type(thing) is bool:
        return '_boolean'
    elif type(thing) is list:
        return '_list'
    else:
        print "Could not find pysh type for", thing, "of type", type(thing)
        return False
    
        

def keep_number_reasonable(n):
    '''
    Returns a version of n that obeys limit parameters.
    '''
    if n > g.max_number_magnitude:
        n = g.max_number_magnitude
    elif n < -g.max_number_magnitude:
        n = -g.max_number_magnitude
    return n

def normalize_genetic_operator_probabilities(gen_op_dict):
    tot = sum(gen_op_dict.values())
    new_probs = map(lambda x: round(x / tot, 4), gen_op_dict.values())
    return dict(zip(gen_op_dict.keys(), new_probs))

def count_parens(tree):
    '''
    Returns the number of paren pairs in tree.
    '''
    remaining = tree
    total = 0

    while True:
        if type(remaining) != list:
            return total
        elif len(remaining) == 0:
            return total + 1
        elif type(remaining[0]) != list:
            remaining.pop(0)
        else:
            remaining = remaining[0] + remaining[1:]
            total

def count_points(tree):
    '''
    Returns the number of points in tree, where each atom and each pair of parentheses 
    counts as a point.
    '''
    remaining = tree
    total = 0

    while True:
        if type(remaining) != list:
            return total + 1
        elif len(remaining) == 0:
            return total + 1
        elif type(remaining[0]) != list:
            remaining = remaining[1:]
            total += 1
        else:
            remaining = remaining[0] + remaining[1:]
            total += 1
    return total



def reductions(f, l):
    '''
    Returns a list of the intermediate values of the reduction (as
    per reduce) of coll by f, starting with init.
    '''
    result = []
    for i in range(len(l)):
        if i == 0:
            result.append(l[i])
        else:
            result.append(f(result[-1], l[i]))
    return result


# def list_to_open_close_sequence(lst):
#     if type(lst) == list:
#         flatten_all
#     else:
#         return lst


def get_matcing_close_index(sequence):
    i = None
    open_count = 0
    for j in range(len(sequence)):
        if sequence[j] == '_open':
            open_count += 1
        elif sequence[j] == '_close':
            open_count -= 1
        if open_count == 0:
            return j
        j += 1

def open_close_sequence_to_list(sequence):
    if not type(sequence) == list:
        return sequence
    elif len(sequence) == 0:
        return []
    else:
        result = []
        rest = sequence
        while len(rest) > 0:
            if rest[0] == '_open':
                i = get_matcing_close_index(rest)
                sub_seq = rest[1:i]
                result.append( open_close_sequence_to_list(sub_seq) )
                rest = rest[i+1:]
            else:
                result.append(rest[0])
                rest.pop(0)
        return result
# print open_close_sequence_to_list(["_open", 1, 2, "_open", 'a', 'b', "_open", 'c', "_close", "_open", "_open", 'd', "_close", "_close", 'e', "_close", "_close"])
# print open_close_sequence_to_list(["_open", 1, "_close", "_open", 2, "_close"])
# print open_close_sequence_to_list(["_open", "_open", 1, "_close", "_open", 2, "_close", "_close"])


def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    Taken From: http://stackoverflow.com/a/26853961/4297413 Thanks to Aaron Hall
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def ensure_list(thing):
    if type(thing) == list:
        return thing
    else:
        return [thing]

