import pytest

from pyshgp.push.atoms import CodeBlock
from pyshgp.push.state import PushState
from pyshgp.utils import Token


class TestPushState:

    def test_len(self, state: PushState):
        assert len(state) == 0
        state["int"].push(100)
        state.load_inputs([1, 2])
        assert len(state) == 3

    def test_from_dict(self, atoms):
        d = {
            "int": [0, 1],
            "stdout": "Hello Push!",
            "exec": [atoms["add"]]
        }
        state = PushState.from_dict(d)
        assert len(state) == 3
        assert state["int"].top() == 1

    def test_load_program(self, state: PushState, atoms):
        prog = CodeBlock.from_list([atoms["5"], atoms["5"], atoms["add"]])
        state.load_program(prog)
        assert len(state) == 1
        assert len(state["exec"].top()) == 3

    def test_inspect_outputs(self, state: PushState):
        state["int"].push(100)
        state["int"].push(-77)
        state["str"].push("Hello")
        state["str"].push("World")
        ouputs = state.observe_stacks(["int", "int", "str"])
        assert ouputs == [-77, 100, "World"]

    def test_inspect_outputs_empty(self, state: PushState):
        ouputs = state.observe_stacks(["int", "int", "str"])
        assert ouputs == [Token.no_stack_item] * 3

    def test_pop_values(self, state: PushState):
        state["int"].push(100)
        state["int"].push(-77)
        state["str"].push("Hello")
        state["str"].push("World")
        popped_vals = state.pop_from_stacks(["int", "int", "str"])
        assert popped_vals == [-77, 100, "World"]
        assert state["str"].top() == "Hello"
        assert len(state) == 1

    def test_pop_values_empty(self, state: PushState):
        popped_vals = state.pop_from_stacks(["int", "int", "str"])
        assert popped_vals == Token.revert
        assert len(state) == 0

    def test_push_values(self, state: PushState):
        state.push_to_stacks(
            [5, 100, "Foo"],
            ["int", "int", "str"]
        )
        assert state["int"].top() == 100
        assert state["str"].top() == "Foo"
        assert len(state) == 3