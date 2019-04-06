from pyshgp.push.atoms import CodeBlock
from pyshgp.push.interpreter import PushInterpreter
from pyshgp.push.instruction_set import InstructionSet


# Not using fixture in order to spot unintentional updates during execution.
i_set = InstructionSet(register_core=True).register_n_inputs(10)


def load_program(name: str, core_type_lib) -> CodeBlock:
    with open("tests/resources/programs/" + name + ".json") as f:
        return CodeBlock.from_json_str(f.read(), i_set, core_type_lib)


def test_program_relu_1(interpreter: PushInterpreter, core_type_lib):
    prog = load_program("relu_via_max", core_type_lib)
    result = interpreter.run(prog, [-5], ["float"])
    assert result == [0.0]

    result = interpreter.run(prog, [5.6], ["float"])
    assert result == [5.6]


def test_program_relu_2(interpreter: PushInterpreter, core_type_lib):
    prog = load_program("relu_via_if", core_type_lib)
    result = interpreter.run(prog, [-5], ["float"])
    assert result == [0.0]

    result = interpreter.run(prog, [5.6], ["float"])
    assert result == [5.6]


def test_program_fibonacci(interpreter: PushInterpreter, core_type_lib):
    prog = load_program("fibonacci", core_type_lib)
    interpreter.run(prog, [5], [])
    assert list(interpreter.state["int"]) == [1, 1, 2, 3, 5]

    interpreter.run(prog, [1], [])
    assert list(interpreter.state["int"]) == [1]

    interpreter.run(prog, [-3], [])
    assert list(interpreter.state["int"]) == []


def test_program_rswn(interpreter: PushInterpreter, core_type_lib):
    prog = load_program("replace_space_with_newline", core_type_lib)
    interpreter.run(prog, ["hello world"], [])
    assert list(interpreter.state["int"]) == [10]
    assert interpreter.state.stdout == "hello\nworld"

    interpreter.run(prog, ["nospace"], [])
    assert list(interpreter.state["int"]) == [7]
    assert interpreter.state.stdout == "nospace"

    interpreter.run(prog, ["   "], [])
    assert list(interpreter.state["int"]) == [0]
    assert interpreter.state.stdout == "\n\n\n"
