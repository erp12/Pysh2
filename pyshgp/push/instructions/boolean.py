
from ..instruction import PyshInstruction


def boolean_and(state):
    if len(state['_boolean']) > 1:
        result = state['_boolean'].ref(0) and state['_boolean'].ref(1)
        state['_boolean'].pop()
        state['_boolean'].pop()
        state['_boolean'].push(result)


boolean_and_intruction = PyshInstruction('_boolean_and',
                                         boolean_and,
                                         stack_types=['_boolean'])
# <instr_open>
# <instr_name>boolean_and
# <instr_desc>Pushes the logical AND of the top two booleans.
# <instr_close>


def boolean_or(state):
    if len(state['_boolean']) > 1:
        result = state['_boolean'].ref(0) or state['_boolean'].ref(1)
        state['_boolean'].pop()
        state['_boolean'].pop()
        state['_boolean'].push(result)


boolean_or_intruction = PyshInstruction('_boolean_or',
                                        boolean_or,
                                        stack_types=['_boolean'])
# <instr_open>
# <instr_name>boolean_or
# <instr_desc>Pushes the logical OR of the top two booleans.
# <instr_close>


def boolean_not(state):
    if len(state['_boolean']) > 0:
        result = not state['_boolean'].ref(0)
        state['_boolean'].pop()
        state['_boolean'].push(result)


boolean_not_intruction = PyshInstruction('_boolean_not',
                                         boolean_not,
                                         stack_types=['_boolean'])
# <instr_open>
# <instr_name>boolean_not
# <instr_desc>Pushes the logical NOT of the top boolean.
# <instr_close>


def boolean_xor(state):
    if len(state['_boolean']) > 1:
        result = not (state['_boolean'].ref(0) == state['_boolean'].ref(1))
        state['_boolean'].pop()
        state['_boolean'].pop()
        state['_boolean'].push(result)


boolean_xor_intruction = PyshInstruction('_boolean_xor',
                                         boolean_xor,
                                         stack_types=['_boolean'])
# <instr_open>
# <instr_name>boolean_xor
# <instr_desc>Pushes the logical XOR of the top two booleans.
# <instr_close>


def boolean_invert_first_then_and(state):
    if len(state['_boolean']) > 1:
        result = (not state['_boolean'].ref(0)) and state['_boolean'].ref(1)
        state['_boolean'].pop()
        state['_boolean'].pop()
        state['_boolean'].push(result)


boolean_invert_first_then_and_intruction = PyshInstruction('_boolean_invert_first_then_and',
                                                           boolean_invert_first_then_and,
                                                           stack_types=['_boolean'])
# <instr_open>
# <instr_name>boolean_invert_first_then_and
# <instr_desc>Pushes the logical AND of the top two booleans, with the fist argument inverted.
# <instr_close>


def boolean_invert_second_then_and(state):
    if len(state['_boolean']) > 1:
        result = state['_boolean'].ref(0) and (not state['_boolean'].ref(1))
        state['_boolean'].pop()
        state['_boolean'].pop()
        state['_boolean'].push(result)


boolean_invert_second_then_and_intruction = PyshInstruction('_boolean_invert_second_then_and',
                                                            boolean_invert_second_then_and,
                                                            stack_types=['_boolean'])
# <instr_open>
# <instr_name>boolean_invert_second_then_and
# <instr_desc>Pushes the logical AND of the top two booleans, with the second argument inverted.
# <instr_close>


def boolean_from_integer(state):
    if len(state['_integer']) > 0:
        new_bool = not (state['_integer'].ref(0) == 0)
        state['_integer'].pop()
        state['_boolean'].push(new_bool)


boolean_from_integer_instruction = PyshInstruction('_boolean_from_integer',
                                                   boolean_from_integer,
                                                   stack_types=['_boolean', '_integer'])
# <instr_open>
# <instr_name>boolean_from_integer
# <instr_desc>Pushes the top integer casted to a boolean. If integer is 0, boolean is false. True otherwise.
# <instr_close>


def boolean_from_float(state):
    if len(state['_float']) > 0:
        new_bool = not (state['_float'].ref(0) == 0.0)
        state['_float'].pop()
        state['_boolean'].push(new_bool)


boolean_from_float_instruction = PyshInstruction('_boolean_from_float',
                                                 boolean_from_float,
                                                 stack_types=['_boolean', '_float'])
# <instr_open>
# <instr_name>boolean_from_float
# <instr_desc>Pushes the top float casted to a boolean. If float is 0.0, boolean is false. True otherwise.
# <instr_close>
