# -*- coding: utf-8 -*-
"""
Created on Sun Jun  17, 2016

@author: Eddie
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from ... import utils as u
from ... import constants as c

from ..instruction import PyshInstruction
from .jit import JustInTimeInstruction


exec_noop_instruction = PyshInstruction('_exec_noop',
                                        lambda state: state,
                                        stack_types=['_exec'])
# <instr_open>
# <instr_name>exec_noop
# <instr_desc>An instruction that does nothing. (although can still be useful!)
# <instr_close>

code_noop_instruction = PyshInstruction('_code_noop',
                                        lambda state: state,
                                        stack_types=['_code'])
# <instr_open>
# <instr_name>code_noop
# <instr_desc>An instruction that does nothing. (although can still be useful!)
# <instr_close>


def code_maker(pysh_type):
    def f(state):
        if len(state[pysh_type]) > 0:
            new_code = state[pysh_type].ref(0)
            state[pysh_type].pop()
            state['_code'].push(new_code)
        return state
    instruction = PyshInstruction('_code_from' + pysh_type,
                                  f,
                                  stack_types=['_code', pysh_type])
    if pysh_type == '_exec':
        instruction.parentheses = 1
    return instruction


code_from_boolean_instruction = code_maker('_boolean')
# <instr_open>
# <instr_name>code_from_boolean
# <instr_desc>Takes the top boolean and stores it on the code stack.
# <instr_close>
code_from_float_instruction = code_maker('_float')
# <instr_open>
# <instr_name>code_from_float
# <instr_desc>Takes the top float and stores it on the code stack.
# <instr_close>
code_from_integer_instruction = code_maker('_integer')
# <instr_open>
# <instr_name>code_from_integer
# <instr_desc>Takes the top integer and stores it on the code stack.
# <instr_close>
code_from_exec_instruction = code_maker('_exec')
# <instr_open>
# <instr_name>code_from_exec
# <instr_desc>Takes the top item from the exec stack (after the `code_from_exec` instruction) and stores it on the code stack.
# <instr_close>


def code_append(state):
    if len(state['_code']) > 1:
        new_item = u.ensure_list(state['_code'].ref(
            0)) + u.ensure_list(state['_code'].ref(1))
        state['_code'].pop()
        state['_code'].pop()
        state['_code'].push(new_item)
    return state


code_append_instruction = PyshInstruction('_code_append',
                                          code_append,
                                          stack_types=['_code'])
# <instr_open>
# <instr_name>code_append
# <instr_desc>Takes the top two items from the code stack, appends them into 1 list, and pushes the result onto the code stack.
# <instr_close>


def code_atom(state):
    if len(state['_code']) > 0:
        top_code = state['_code'].ref(0)
        state['_code'].pop()
        state['_boolean'].push(not isinstance(top_code, list))
    return state


code_atom_instruction = PyshInstruction('_code_atom',
                                        code_atom,
                                        stack_types=['_code', '_boolean'])
# <instr_open>
# <instr_name>code_atom
# <instr_desc>Pushes True if the top item on the code stack is not a list. False otherwise.
# <instr_close>


def code_car(state):
    if len(state['_code']) > 0 and len(u.ensure_list(state['_code'].ref(0))) > 0:
        top_code = u.ensure_list(state['_code'].ref(0))[0]
        state['_code'].pop()
        state['_code'].push(top_code)
    return state


code_car_instruction = PyshInstruction('_code_car',
                                       code_car,
                                       stack_types=['_code'])
# <instr_open>
# <instr_name>code_car
# <instr_desc>Pushes the first item of the list on top of the `code` stack. For example, if the top piece of code is "( A B )" then this pushes "A" (after popping the argument). If the code on top of the stack is not a list then this has no effect.
# <instr_close>


def code_cdr(state):
    if len(state['_code']) > 0:
        top_code = u.ensure_list(state['_code'].ref(0))[1:]
        state['_code'].pop()
        state['_code'].push(top_code)
    return state


code_cdr_instruction = PyshInstruction('_code_cdr',
                                       code_cdr,
                                       stack_types=['_code'])
# <instr_open>
# <instr_name>code_cdr
# <instr_desc>Pushes a version of the list from the top of the `code` stack without its first element. For example, if the top piece of code is "( A B )" then this pushes "( B )" (after popping the argument). If the code on top of the stack is not a list then this pushes the empty list ("( )").
# <instr_close>


def code_cons(state):
    if len(state['_code']) > 1:
        new_item = [state['_code'].ref(1)] + \
            u.ensure_list(state['_code'].ref(0))
        state['_code'].pop()
        state['_code'].pop()
        state['_code'].push(new_item)
    return state


code_cons_instruction = PyshInstruction('_code_cons',
                                        code_cons,
                                        stack_types=['_code'])
# <instr_open>
# <instr_name>code_cons
# <instr_desc>Pushes the result of "consing" (in the Lisp sense) the second stack item onto the first stack item (which is coerced to a list if necessary). For example, if the top piece of code is "( A B )" and the second piece of code is "X" then this pushes "( X A B )" (after popping the argument).
# <instr_close>


def code_do(state):
    if len(state['_code']) > 0:
        top_code = state['_code'].ref(0)
        state['_exec'].push(JustInTimeInstruction('_code_pop'))
        state['_exec'].push(top_code)
    return state


code_do_instruction = PyshInstruction('_code_do',
                                      code_do,
                                      stack_types=['_code', '_exec'])
# <instr_open>
# <instr_name>code_do
# <instr_desc> Recursively invokes the interpreter on the program on top of the `code` stack. After evaluation the `code` stack is popped; normally this pops the program that was just executed, but if the expression itself manipulates the stack then this final pop may end up popping something else.
# <instr_close>


def code_do_star(state):
    if len(state['_code']) > 0:
        top_code = state['_code'].ref(0)
        state['_code'].pop()
        state['_exec'].push(top_code)
    return state


code_do_star_instruction = PyshInstruction('_code_do*',
                                           code_do_star,
                                           stack_types=['_code', '_exec'])
# <instr_open>
# <instr_name>code_do*
# <instr_desc>Like `code_do` but pops the stack before, rather than after, the recursive execution.
# <instr_close>


def code_do_range(state):
    if len(state['_code']) > 0 and len(state['_integer']) > 1:
        to_do = state['_code'].ref(0)
        current_index = state['_integer'].ref(1)
        destination_index = state['_integer'].ref(0)
        state['_integer'].pop()
        state['_integer'].pop()
        state['_code'].pop()

        increment = 0
        if current_index < destination_index:
            increment = 1
        elif current_index > destination_index:
            increment = -1

        if not increment == 0:
            state['_exec'].push([(current_index + increment),
                                 destination_index,
                                 JustInTimeInstruction('_code_from_exec'),
                                 to_do,
                                 JustInTimeInstruction('_code_do*range')])
        state['_integer'].push(current_index)
        state['_exec'].push(to_do)
    return state


code_do_range_intruction = PyshInstruction('_code_do*range',
                                           code_do_range,
                                           stack_types=['_exec', '_integer', '_code'])
# <instr_open>
# <instr_name>code_do*range
# <instr_desc>An iteration instruction that executes the top item on the `code` stack a number of times that depends on the top two integers, while also pushing the loop counter onto the `integer` stack for possible access during the execution of the body of the loop. The top integer is the "destination index" and the second integer is the "current index." First the code and the integer arguments are saved locally and popped. Then the integers are compared. If the integers are equal then the current index is pushed onto the `integer` stack and the code (which is the "body" of the loop) is pushed onto the `exec` stack for subsequent execution. If the integers are not equal then the current index will still be pushed onto the `integer` stack but two items will be pushed onto the `exec` stack -- first a recursive call to `code_do*range` (with the same code and destination index, but with a current index that has been either incremented or decremented by 1 to be closer to the destination index) and then the body code.
# <instr_close>


def exec_do_range(state):
    '''
    Differs from code.do*range only in the source of the code and the recursive call.
    '''
    if len(state['_exec']) > 0 and len(state['_integer']) > 1:
        to_do = state['_exec'].ref(0)
        current_index = state['_integer'].ref(1)
        destination_index = state['_integer'].ref(0)
        state['_integer'].pop()
        state['_integer'].pop()
        state['_exec'].pop()

        increment = 0
        if current_index < destination_index:
            increment = 1
        elif current_index > destination_index:
            increment = -1

        if not increment == 0:
            state['_exec'].push([(current_index + increment),
                                 destination_index,
                                 JustInTimeInstruction('_exec_do*range'),
                                 to_do])

        state['_integer'].push(current_index)
        state['_exec'].push(to_do)
    return state


exec_do_range_intruction = PyshInstruction('_exec_do*range',
                                           exec_do_range,
                                           stack_types=['_exec', '_integer'],
                                           parentheses=1)
# <instr_open>
# <instr_name>exec_do*range
# <instr_desc>An iteration instruction that executes the top item on the `exec` stack a number of times that depends on the top two integers, while also pushing the loop counter onto the `integer` stack for possible access during the execution of the body of the loop. This is similar to `code_do*count` except that it takes its code argument from the `exec` stack. The top integer is the "destination index" and the second integer is the "current index." First the code and the integer arguments are saved locally and popped. Then the integers are compared. If the integers are equal then the current index is pushed onto the `integer` stack and the code (which is the "body" of the loop) is pushed onto the `exec` stack for subsequent execution. If the integers are not equal then the current index will still be pushed onto the `integer` stack but two items will be pushed onto the `exec` stack -- first a recursive call to `exec_do*range` (with the same code and destination index, but with a current index that has been either incremented or decremented by 1 to be closer to the destination index) and then the body code. Note that the range is inclusive of both endpoints; a call with integer arguments 3 and 5 will cause its body to be executed 3 times, with the loop counter having the values 3, 4, and 5. Note also that one can specify a loop that "counts down" by providing a destination index that is less than the specified current index.
# <instr_close>


def code_do_count(state):
    if not (len(state['_integer']) == 0 or state['_integer'].ref(0) < 1 or len(state['_code']) == 0):
        to_push = [0,
                   state['_integer'].ref(0) - 1,
                   JustInTimeInstruction('_code_from_exec'),
                   state['_code'].ref(0),
                   JustInTimeInstruction('_code_do*range')]
        state['_code'].pop()
        state['_integer'].pop()
        state['_exec'].push(to_push)
    return state


code_do_count_intruction = PyshInstruction('_code_do*count',
                                           code_do_count,
                                           stack_types=['_exec', '_integer', '_code'])
# <instr_open>
# <instr_name>code_do*count
# <instr_desc>An iteration instruction that performs a loop (the body of which is taken from the `code` stack) the number of times indicated by the `integer` argument, pushing an index (which runs from zero to one less than the number of iterations) onto the `integer` stack prior to each execution of the loop body.
# <instr_close>


def exec_do_count(state):
    '''
    differs from code.do*count only in the source of the code and the recursive call
    '''
    if not (len(state['_integer']) == 0 or state['_integer'].ref(0) < 1 or len(state['_exec']) == 0):
        to_push = [0,
                   state['_integer'].ref(0) - 1,
                   JustInTimeInstruction('_exec_do*range'),
                   state['_exec'].ref(0)]
        state['_exec'].pop()
        state['_integer'].pop()
        state['_exec'].push(to_push)
    return state


exec_do_count_intruction = PyshInstruction('_exec_do*count',
                                           exec_do_count,
                                           stack_types=['_exec', '_integer'],
                                           parentheses=1)
# <instr_open>
# <instr_name>exec_do*count
# <instr_desc>An iteration instruction that performs a loop (the body of which is taken from the `exec` stack) the number of times indicated by the `integer` argument, pushing an index (which runs from zero to one less than the number of iterations) onto the `integer` stack prior to each execution of the loop body. This is similar to `code_do*count` except that it takes its code argument from the `exec` stack.
# <instr_close>


def code_do_times(state):
    if not (len(state['_integer']) == 0 or state['_integer'].ref(0) < 1 or len(state['_code']) == 0):
        to_push = [0,
                   state['_integer'].ref(0) - 1,
                   JustInTimeInstruction('_code_from_exec'),
                   [JustInTimeInstruction(
                       '_integer_pop')] + u.ensure_list(state['_code'].ref(0)),
                   JustInTimeInstruction('_code_do*range')]
        state['_code'].pop()
        state['_integer'].pop()
        state['_exec'].push(to_push)


code_do_times_intruction = PyshInstruction('_code_do*times',
                                           code_do_times,
                                           stack_types=['_code', '_integer'])
# <instr_open>
# <instr_name>code_do*times
# <instr_desc>Like `code_do*count` but does not push the loop counter.
# <instr_close>


def exec_do_times(state):
    '''
    differs from code.do*times only in the source of the code and the recursive call
    '''
    if not (len(state['_integer']) == 0 or state['_integer'].ref(0) < 1 or len(state['_exec']) == 0):
        to_push = [0,
                   state['_integer'].ref(0) - 1,
                   JustInTimeInstruction('_exec_do*range'),
                   [JustInTimeInstruction('_integer_pop')] + u.ensure_list(state['_exec'].ref(0))]
        state['_exec'].pop()
        state['_integer'].pop()
        state['_exec'].push(to_push)
    return state


exec_do_times_intruction = PyshInstruction('_exec_do*times',
                                           exec_do_times,
                                           stack_types=['_exec', '_integer'],
                                           parentheses=1)
# <instr_open>
# <instr_name>exec_do*times
# <instr_desc>Like `exec_do*count` but does not push the loop counter.
# <instr_close>


def exec_while(state):
    if len(state['_exec']) > 0:
        if len(state['_boolean']) == 0:
            state['_exec'].pop()
        elif not state['_boolean'].ref(0):
            state['_exec'].pop()
            state['_boolean'].pop()
        else:
            block = state['_exec'].ref(0)
            state['_exec'].push(JustInTimeInstruction('_exec_while'))
            state['_exec'].push(block)
            state['_boolean'].pop()
    return state


exec_while_intruction = PyshInstruction('_exec_while',
                                        exec_while,
                                        stack_types=['_exec', '_boolean'],
                                        parentheses=1)
# <instr_open>
# <instr_name>exec_while
# <instr_desc>Repeats the top item of the exect stack until the boolean stack has a False or is empty.
# <instr_close>


def exec_do_while(state):
    if len(state['_exec']) > 0:
        block = state['_exec'].ref(0)
        state['_exec'].push(JustInTimeInstruction('_exec_while'))
        state['_exec'].push(block)
    return state


exec_do_while_intruction = PyshInstruction('_exec_do*while',
                                           exec_do_while,
                                           stack_types=['_exec', '_boolean'],
                                           parentheses=1)
# <instr_open>
# <instr_name>exec_do*while
# <instr_desc>Pushes the next item on the `exec` stack until the boolean stack has a False or is empty. Similar to `exec_while`, but results in one extra call to the body of the loop.
# <instr_close>


# ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# Code Map
# def code_map(state):
#     if len(state['_code']) > 0 and len(state['_exec']) > 0:
#         pass
# ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????


def code_if(state):
    if len(state['_code']) > 1 and len(state['_boolean']) > 0:
        to_push = state['_code'].ref(0)
        if state['_boolean'].ref(0):
            to_push = state['_code'].ref(1)
        state['_code'].pop()
        state['_code'].pop()
        state['_boolean'].pop()
        state['_exec'].push(to_push)


code_if_instruction = PyshInstruction('_code_if',
                                      code_if,
                                      stack_types=['_code', '_exec', '_boolean'])
# <instr_open>
# <instr_name>code_if
# <instr_desc>Pushes the second item of the `code` stack to the `exec` stack if the top boolean is True. Otherwise, pushes the top item of the `code` stack to the `exec` stack.
# <instr_close>


def exec_if(state):
    if len(state['_exec']) > 1 and len(state['_boolean']) > 0:
        to_push = state['_exec'].ref(1)
        if state['_boolean'].ref(0):
            to_push = state['_exec'].ref(0)
        state['_exec'].pop()
        state['_exec'].pop()
        state['_boolean'].pop()
        state['_exec'].push(to_push)


exec_if_instruction = PyshInstruction('_exec_if',
                                      exec_if,
                                      stack_types=['_exec', '_boolean'],
                                      parentheses=2)
# <instr_open>
# <instr_name>exec_if
# <instr_desc>Pushes the top item of the `exec` stack (after removing the `exec_if` instruction)  to the `exec` stack if the top boolean is True. Otherwise, pushes the second item of the `exec` stack to the `exec` stack. Differs from `code_if` in the source of the code and in the order of the if/then parts.
# <instr_close>


def exec_when(state):
    if len(state['_exec']) > 0 and len(state['_boolean']) > 0:
        if not state['_boolean'].ref(0):
            state['_exec'].pop()
        state['_boolean'].pop()


exec_when_instruction = PyshInstruction('_exec_when',
                                        exec_when,
                                        stack_types=['_exec', '_boolean'],
                                        parentheses=1)
# <instr_open>
# <instr_name>exec_when
# <instr_desc>If the top boolean is False, pop the top item on the `exec` stack (after `exec_when`) effectively skipping it. If top boolean is True, the top item on `exec` stack is untouched and will be evaluated next interation of the program interpretation.
# <instr_close>


def code_length(state):
    if len(state['_code']) > 0:
        l = len(u.ensure_list(state['_code'].ref(0)))
        state['_code'].pop()
        state['_integer'].push(l)


code_length_instruction = PyshInstruction('_code_length',
                                          code_length,
                                          stack_types=['_code', '_integer'])
# <instr_open>
# <instr_name>code_length
# <instr_desc>Pushes the length of the top item on the `code` stack to the `integer` stack.
# <instr_close>


def code_list(state):
    if len(state['_code']) > 1:
        new_item = [state['_code'].ref(1), state['_code'].ref(0)]
        if u.count_points(new_item) <= c.global_max_points:
            state['_code'].pop()
            state['_code'].pop()
            state['_code'].push(new_item)


code_list_instruction = PyshInstruction('_code_list',
                                        code_list,
                                        stack_types=['_code'])
# <instr_open>
# <instr_name>code_list
# <instr_desc>Pushes the top two items of the `code` stack back onto the `code` stack in a list.
# <instr_close>


def code_wrap(state):
    if len(state['_code']) > 0:
        new_item = [state['_code'].ref(0)]
        if u.count_points(new_item) <= c.global_max_points:
            state['_code'].pop()
            state['_code'].push(new_item)


code_wrap_instruction = PyshInstruction('_code_wrap',
                                        code_wrap,
                                        stack_types=['_code'])
# <instr_open>
# <instr_name>code_wrap
# <instr_desc>Pushes the top item of the code stack back onto the `code` stack inside of a list.
# <instr_close>


def code_member(state):
    if len(state['_code']) > 1:
        new_bool = state['_code'].ref(
            1) in u.ensure_list(state['_code'].ref(0))
        state['_code'].pop()
        state['_code'].pop()
        state['_boolean'].push(new_bool)


code_member_instruction = PyshInstruction('_code_member',
                                          code_member,
                                          stack_types=['_code', '_boolean'])
# <instr_open>
# <instr_name>code_member
# <instr_desc>Pushes True if the second item on the `code` stack is found in the top item on the code stack. Pushes False otherwise.
# <instr_close>


def code_nth(state):
    if len(state['_integer']) > 0 and len(state['_code']) > 0 and len(u.ensure_list(state['_code'].ref(0))) > 0:
        top_code_as_list = u.ensure_list(state['_code'].ref(0))
        i = abs(state['_integer'].ref(0)) % len(top_code_as_list)
        new_item = top_code_as_list[i]
        state['_code'].pop()
        state['_integer'].pop()
        state['_code'].push(new_item)


code_nth_instruction = PyshInstruction('_code_nth',
                                       code_nth,
                                       stack_types=['_code', '_integer'])
# <instr_open>
# <instr_name>code_nth
# <instr_desc>Pushes the nth item of the top item on the `code` stack. To avoid indexing out of bounds, index of nth idem comes form the top `integer` mod the length of the top `code` item.
# <instr_close>


def code_nthcdr(state):
    if len(state['_integer']) > 0 and len(state['_code']) > 0 and len(u.ensure_list(state['_code'].ref(0))) > 0:
        top_code_as_list = u.ensure_list(state['_code'].ref(0))
        i = abs(state['_integer'].ref(0)) % len(top_code_as_list)
        new_item = top_code_as_list[:i] + top_code_as_list[i + 1:]
        state['_code'].pop()
        state['_integer'].pop()
        state['_code'].push(new_item)


code_nthcdr_instruction = PyshInstruction('_code_nthcdr',
                                          code_nthcdr,
                                          stack_types=['_code', '_integer'])
# <instr_open>
# <instr_name>code_nthcdr
# <instr_desc>Pushes the top item on the `code` stack, without the nth item. To avoid indexing out of bounds, index of nth idem comes form the top `integer` mod the length of the top `code` item.
# <instr_close>
