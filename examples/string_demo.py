# _*_ coding: utf_8 _*_
"""
Created on 7/25/2016

@author: Eddie
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import random
import collections

import pysh.utils as u
import pysh.gp.gp as gp
import pysh.push.interpreter as interp
import pysh.push.instructions.registered_instructions as ri
import pysh.push.instruction as instr

'''
Take the input string, remove the last 2 characters, and then concat this result with itself.
The fitness will be the number of non-matching characters in the resulting string. For example,
desired result of "abcde" would be "abcabc", and a string of "abcabcrrr" would have an error of 3, for
3 too many characters, and the string "aaaaaa" would have error of 4, since it gets 2 of the characters right.
'''

def string_difference(s1, s2):
    '''
    Returns the difference in the strings, based on character position.
    '''
    char_lvl_diff = 0
    for c1, c2 in zip(s1, s2):
        char_lvl_diff += int(not c1 == c2)
    return char_lvl_diff + abs(len(s1) - len(s2))

def string_char_counts_difference(s1, s2):
    '''
    '''
    result = len(s1) + len(s2)
    s1_letters = collections.Counter(s1)
    for c in s2:
        if c in s1_letters:
            result -= 2
            s1_letters[c] -= 1
            if s1_letters[c] == 0:
                s1_letters.pop(c, None)
    return result


def random_str():
    s = ""
    for i in range(random.randint(1, 10)):
        s += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    return s

def string_error_func(program):
    inputs = ["abcde", "", "E", "Hi", "Tom", "leprechaun", "zoomzoomzoom", 
                "qwertyuiopasd", "GallopTrotCanter", "Quinona", "_abc"]
    errors = []

    for inpt in inputs:
        # Create the push interpreter
        interpreter = interp.PyshInterpreter([inpt])
        interpreter.run_push(program)
        # Get output
        prog_output = interpreter.state.stacks["_string"].stack_ref(0)

        if isinstance(prog_output, u.NoStackItem) or isinstance(prog_output, u.StackOutOfBounds):
            # If response is un-evaluatable, add a bad error.
            errors.append(1000)
        else:
            #compare to target output
            target_output = inpt[:-2] + inpt[:-2]
            errors.append(string_difference(prog_output, target_output) + string_char_counts_difference(prog_output, target_output))
    return errors

string_params = {
    "atom_generators" : [instr.PyshInputInstruction(0),
                         ri.get_instruction("_string_length"),
                         ri.get_instruction("_string_head"),
                         ri.get_instruction("_string_concat"),
                         ri.get_instruction("_string_stack_depth"),
                         ri.get_instruction("_string_swap"),
                         ri.get_instruction("_string_dup"),
                         ri.get_instruction("_integer_add"),
                         ri.get_instruction("_integer_sub"),
                         ri.get_instruction("_integer_dup"),
                         ri.get_instruction("_integer_swap"),
                         ri.get_instruction("_integer_stack_depth"),
                         lambda: random.randint(0, 10),
                         lambda: random_str()],
    "population_size" : 500,
    "max_generations" : 200,
    "epigenetic_markers" : [],
    "genetic_operator_probabilities" : {"alternation" : 0.5,
                                        "uniform_mutation" : 0.5},
    "uniform_mutation_constant_tweak_rate" : 0.8
}

if __name__ == "__main__":
    gp.evolution(string_error_func, string_params)
