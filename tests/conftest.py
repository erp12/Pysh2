import pytest

from pyshgp.push.instruction_set import InstructionSet
from pyshgp.push.atoms import Closer, Literal
from pyshgp.push.interpreter import PushInterpreter
from pyshgp.push.state import PushState


@pytest.fixture(scope="session")
def instr_set():
    return InstructionSet(register_all=True)


@pytest.fixture(scope="function")
def atoms(instr_set):
    return {
        "5": Literal(5),
        "1.2": Literal(1.2),
        "true": Literal(True),
        "add": instr_set["int_add"],
        "sub": instr_set["int_sub"],
        "if": instr_set["exec_if"],
        "close": Closer()
    }


@pytest.fixture(scope="function")
def state():
    return PushState({"int", "float", "bool", "str"})


@pytest.fixture(scope="function")
def interpreter():
    return PushInterpreter()