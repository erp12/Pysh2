# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:34:38 2016

@author: Eddie
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


from .boolean import (boolean_and_intruction, boolean_or_intruction,
    boolean_not_intruction, boolean_xor_intruction,
    boolean_invert_first_then_and_intruction,
    boolean_invert_second_then_and_intruction, boolean_from_integer_instruction,
    boolean_from_float_instruction)
from .char import (char_all_from_string_instruction,
    char_from_integer_instruction, char_from_float_instruction,
    char_is_letter_instruction, char_is_digit_instruction,
    char_is_white_space_instruction)
from .code import (exec_noop_instruction, code_noop_instruction,
    code_from_boolean_instruction, code_from_float_instruction,
    code_from_integer_instruction, code_from_exec_instruction,
    code_append_instruction, code_atom_instruction, code_car_instruction,
    code_cdr_instruction, code_cons_instruction, code_do_instruction,
    code_do_star_instruction, code_do_range_intruction,
    exec_do_range_intruction, code_do_count_intruction,
    exec_do_count_intruction, code_do_times_intruction,
    exec_do_times_intruction, exec_while_intruction, exec_do_while_intruction,
    code_if_instruction, exec_if_instruction, exec_when_instruction,
    code_length_instruction, code_list_instruction, code_wrap_instruction,
    code_member_instruction, code_nth_instruction, code_nthcdr_instruction)
from .common import (pop_exec_instr, pop_integer_instr, pop_float_instr,
    pop_code_instr, pop_boolean_instr, pop_string_instr, pop_char_instr,
    dup_exec_instr, dup_integer_instr, dup_float_instr, dup_code_instr,
    dup_boolean_instr, dup_string_instr, dup_char_instr, swap_exec_instr,
    swap_integer_instr, swap_float_instr, swap_code_instr, swap_boolean_instr,
    swap_string_instr, swap_char_instr, rot_exec_instr, rot_integer_instr,
    rot_float_instr, rot_code_instr, rot_boolean_instr, rot_string_instr,
    rot_char_instr, flush_exec_instr, flush_integer_instr, flush_float_instr,
    flush_code_instr, flush_boolean_instr, flush_string_instr, flush_char_instr,
    eq_exec_instr, eq_integer_instr, eq_float_instr, eq_code_instr,
    eq_boolean_instr, eq_string_instr, eq_char_instr, stack_depth_exec_instr,
    stack_depth_integer_instr, stack_depth_float_instr, stack_depth_code_instr,
    stack_depth_boolean_instr, stack_depth_string_instr, stack_depth_char_instr,
    yank_exec_instr, yank_integer_instr, yank_float_instr, yank_code_instr,
    yank_boolean_instr, yank_string_instr, yank_char_instr, yank_dup_exec_instr,
    yank_dup_integer_instr, yank_dup_float_instr, yank_dup_code_instr,
    yank_dup_boolean_instr, yank_dup_string_instr, yank_dup_char_instr,
    shove_exec_instr, shove_integer_instr, shove_float_instr, shove_code_instr,
    shove_boolean_instr, shove_string_instr, shove_char_instr,
    empty_exec_instr, empty_integer_instr, empty_float_instr, empty_code_instr,
    empty_boolean_instr, empty_string_instr, empty_char_instr)
from .io import (print_newline_instr, print_exec_instr, print_integer_instr,
    print_float_instr, print_code_instr, print_boolean_instr)
from .numbers import (add_integer_instr, add_float_instr, sub_integer_instr,
    sub_float_instr, mult_integer_instr, mult_float_instr, div_integer_instr,
    div_float_instr, mod_integer_instr, mod_float_instr, lt_integer_instr,
    lt_float_instr, lte_integer_instr, lte_float_instr, gt_integer_instr,
    gt_float_instr, gte_integer_instr, gte_float_instr, min_integer_instr,
    min_float_instr, max_integer_instr, max_float_instr, inc_integer_instr,
    inc_float_instr, dec_integer_instr, dec_float_instr, float_sin_instr,
    float_cos_instr, float_tan_instr, int_from_float_instr,
    int_from_boolean_instr, int_from_string_instr, integer_from_char_instr,
    float_from_int_instr, float_from_bool_instr, float_from_string_instr,
    float_from_char_instr)
from .string import (string_from_integer_instr, string_from_float_instr,
    string_from_boolean_instr, string_concat_instr, string_head_instr,
    string_tail_instr, string_split_at_index_instr, string_split_at_str_instr,
    string_split_at_char_instr, string_split_at_space_instr,
    string_length_instr, string_reverse_instr, string_char_at_instr,
    string_empty_string_instr, string_contains_instr, string_replace_instr,
    string_from_char_instr, string_append_char_instr, string_first_instr,
    string_last_instr, string_nth_instr, string_replace_char_instr,
    string_replace_first_char_instr, string_remove_char_instr,
    )
from .vectors import (pop_integer_vector_instr, dup_integer_vector_instr,
    swap_integer_vector_instr, rot_integer_vector_instr,
    flush_integer_vector_instr, eq_integer_vector_instr,
    stack_depth_integer_vector_instr, yank_integer_vector_instr,
    yank_dup_integer_vector_instr, shove_integer_vector_instr,
    empty_integer_vector_instr, pop_float_vector_instr, dup_float_vector_instr,
    swap_float_vector_instr, rot_float_vector_instr, flush_float_vector_instr,
    eq_float_vector_instr, stack_depth_float_vector_instr,
    yank_float_vector_instr, yank_dup_float_vector_instr,
    shove_float_vector_instr, empty_float_vector_instr,
    pop_boolean_vector_instr, dup_boolean_vector_instr,
    swap_boolean_vector_instr, rot_boolean_vector_instr,
    flush_boolean_vector_instr, eq_boolean_vector_instr,
    stack_depth_boolean_vector_instr, yank_boolean_vector_instr,
    yank_dup_boolean_vector_instr, shove_boolean_vector_instr,
    empty_boolean_vector_instr, pop_string_vector_instr,
    dup_string_vector_instr, swap_string_vector_instr, rot_string_vector_instr,
    flush_string_vector_instr, eq_string_vector_instr,
    stack_depth_string_vector_instr, yank_string_vector_instr,
    yank_dup_string_vector_instr, shove_string_vector_instr,
    empty_string_vector_instr, concat_integer_vector_instr,
    append_integer_vector_instr, take_integer_vector_instr,
    subvec_integer_vector_instr, first_integer_vector_instr,
    last_integer_vector_instr, nth_integer_vector_instr,
    rest_integer_vector_instr, butlast_integer_vector_instr,
    length_integer_vector_instr, reverse_integer_vector_instr,
    push_all_integer_vector_instr, empty_vec_integer_vector_instr,
    contains_integer_vector_instr, index_of_integer_vector_instr,
    occurrences_of_integer_vector_instr, set_integer_vector_instr,
    replace_integer_vector_instr, replace_first_integer_vector_instr,
    remove_integer_vector_instr, iterate_integer_vector_instr,
    concat_float_vector_instr, append_float_vector_instr,
    take_float_vector_instr, subvec_float_vector_instr,
    first_float_vector_instr, last_float_vector_instr, nth_float_vector_instr,
    rest_float_vector_instr, butlast_float_vector_instr,
    length_float_vector_instr, reverse_float_vector_instr,
    push_all_float_vector_instr, empty_vec_float_vector_instr,
    contains_float_vector_instr, index_of_float_vector_instr,
    occurrences_of_float_vector_instr, set_float_vector_instr,
    replace_float_vector_instr, replace_first_float_vector_instr,
    remove_float_vector_instr, iterate_float_vector_instr,
    concat_boolean_vector_instr, append_boolean_vector_instr,
    take_boolean_vector_instr, subvec_boolean_vector_instr,
    first_boolean_vector_instr, last_boolean_vector_instr,
    nth_boolean_vector_instr, rest_boolean_vector_instr,
    butlast_boolean_vector_instr, length_boolean_vector_instr,
    reverse_boolean_vector_instr, push_all_boolean_vector_instr,
    empty_vec_boolean_vector_instr, contains_boolean_vector_instr,
    index_of_boolean_vector_instr, occurrences_of_boolean_vector_instr,
    set_boolean_vector_instr, replace_boolean_vector_instr,
    replace_first_boolean_vector_instr, remove_boolean_vector_instr,
    iterate_boolean_vector_instr, concat_string_vector_instr,
    append_string_vector_instr, take_string_vector_instr,
    subvec_string_vector_instr, first_string_vector_instr,
    last_string_vector_instr, nth_string_vector_instr, rest_string_vector_instr,
    butlast_string_vector_instr, length_string_vector_instr,
    reverse_string_vector_instr, push_all_string_vector_instr,
    empty_vec_string_vector_instr, contains_string_vector_instr,
    index_of_string_vector_instr, occurrences_of_string_vector_instr,
    set_string_vector_instr, replace_string_vector_instr,
    replace_first_string_vector_instr, remove_string_vector_instr,
    iterate_string_vector_instr)

all_instructions = [
    boolean_and_intruction,
    boolean_or_intruction,
    boolean_not_intruction,
    boolean_xor_intruction,
    boolean_invert_first_then_and_intruction,
    boolean_invert_second_then_and_intruction,
    boolean_from_integer_instruction,
    boolean_from_float_instruction,
    char_all_from_string_instruction,
    char_from_integer_instruction,
    char_from_float_instruction,
    char_is_letter_instruction,
    char_is_digit_instruction,
    char_is_white_space_instruction,
    exec_noop_instruction,
    code_noop_instruction,
    code_from_boolean_instruction,
    code_from_float_instruction,
    code_from_integer_instruction,
    code_from_exec_instruction,
    code_append_instruction,
    code_atom_instruction,
    code_car_instruction,
    code_cdr_instruction,
    code_cons_instruction,
    code_do_instruction,
    code_do_star_instruction,
    code_do_range_intruction,
    exec_do_range_intruction,
    code_do_count_intruction,
    exec_do_count_intruction,
    code_do_times_intruction,
    exec_do_times_intruction,
    exec_while_intruction,
    exec_do_while_intruction,
    code_if_instruction,
    exec_if_instruction,
    exec_when_instruction,
    code_length_instruction,
    code_list_instruction,
    code_wrap_instruction,
    code_member_instruction,
    code_nth_instruction,
    code_nthcdr_instruction,
    pop_exec_instr,
    pop_integer_instr,
    pop_float_instr,
    pop_code_instr,
    pop_boolean_instr,
    pop_string_instr,
    pop_char_instr,
    dup_exec_instr,
    dup_integer_instr,
    dup_float_instr,
    dup_code_instr,
    dup_boolean_instr,
    dup_string_instr,
    dup_char_instr,
    swap_exec_instr,
    swap_integer_instr,
    swap_float_instr,
    swap_code_instr,
    swap_boolean_instr,
    swap_string_instr,
    swap_char_instr,
    rot_exec_instr,
    rot_integer_instr,
    rot_float_instr,
    rot_code_instr,
    rot_boolean_instr,
    rot_string_instr,
    rot_char_instr,
    flush_exec_instr,
    flush_integer_instr,
    flush_float_instr,
    flush_code_instr,
    flush_boolean_instr,
    flush_string_instr,
    flush_char_instr,
    eq_exec_instr,
    eq_integer_instr,
    eq_float_instr,
    eq_code_instr,
    eq_boolean_instr,
    eq_string_instr,
    eq_char_instr,
    stack_depth_exec_instr,
    stack_depth_integer_instr,
    stack_depth_float_instr,
    stack_depth_code_instr,
    stack_depth_boolean_instr,
    stack_depth_string_instr,
    stack_depth_char_instr,
    yank_exec_instr,
    yank_integer_instr,
    yank_float_instr,
    yank_code_instr,
    yank_boolean_instr,
    yank_string_instr,
    yank_char_instr,
    yank_dup_exec_instr,
    yank_dup_integer_instr,
    yank_dup_float_instr,
    yank_dup_code_instr,
    yank_dup_boolean_instr,
    yank_dup_string_instr,
    yank_dup_char_instr,
    shove_exec_instr,
    shove_integer_instr,
    shove_float_instr,
    shove_code_instr,
    shove_boolean_instr,
    shove_string_instr,
    shove_char_instr,
    empty_exec_instr,
    empty_integer_instr,
    empty_float_instr,
    empty_code_instr,
    empty_boolean_instr,
    empty_string_instr,
    empty_char_instr,
    print_newline_instr,
    print_exec_instr,
    print_integer_instr,
    print_float_instr,
    print_code_instr,
    print_boolean_instr,
    add_integer_instr,
    add_float_instr,
    sub_integer_instr,
    sub_float_instr,
    mult_integer_instr,
    mult_float_instr,
    div_integer_instr,
    div_float_instr,
    mod_integer_instr,
    mod_float_instr,
    lt_integer_instr,
    lt_float_instr,
    lte_integer_instr,
    lte_float_instr,
    gt_integer_instr,
    gt_float_instr,
    gte_integer_instr,
    gte_float_instr,
    min_integer_instr,
    min_float_instr,
    max_integer_instr,
    max_float_instr,
    inc_integer_instr,
    inc_float_instr,
    dec_integer_instr,
    dec_float_instr,
    float_sin_instr,
    float_cos_instr,
    float_tan_instr,
    int_from_float_instr,
    int_from_boolean_instr,
    int_from_string_instr,
    integer_from_char_instr,
    float_from_int_instr,
    float_from_bool_instr,
    float_from_string_instr,
    float_from_char_instr,
    string_from_integer_instr,
    string_from_float_instr,
    string_from_boolean_instr,
    string_concat_instr,
    string_head_instr,
    string_tail_instr,
    string_split_at_index_instr,
    string_split_at_str_instr,
    string_split_at_char_instr,
    string_split_at_space_instr,
    string_length_instr,
    string_reverse_instr,
    string_char_at_instr,
    string_empty_string_instr,
    string_contains_instr,
    string_replace_instr,
    string_from_char_instr,
    string_append_char_instr,
    string_first_instr,
    string_last_instr,
    string_nth_instr,
    string_replace_char_instr,
    string_replace_first_char_instr,
    string_remove_char_instr,
    pop_integer_vector_instr,
    dup_integer_vector_instr,
    swap_integer_vector_instr,
    rot_integer_vector_instr,
    flush_integer_vector_instr,
    eq_integer_vector_instr,
    stack_depth_integer_vector_instr,
    yank_integer_vector_instr,
    yank_dup_integer_vector_instr,
    shove_integer_vector_instr,
    empty_integer_vector_instr,
    pop_float_vector_instr,
    dup_float_vector_instr,
    swap_float_vector_instr,
    rot_float_vector_instr,
    flush_float_vector_instr,
    eq_float_vector_instr,
    stack_depth_float_vector_instr,
    yank_float_vector_instr,
    yank_dup_float_vector_instr,
    shove_float_vector_instr,
    empty_float_vector_instr,
    pop_boolean_vector_instr,
    dup_boolean_vector_instr,
    swap_boolean_vector_instr,
    rot_boolean_vector_instr,
    flush_boolean_vector_instr,
    eq_boolean_vector_instr,
    stack_depth_boolean_vector_instr,
    yank_boolean_vector_instr,
    yank_dup_boolean_vector_instr,
    shove_boolean_vector_instr,
    empty_boolean_vector_instr,
    pop_string_vector_instr,
    dup_string_vector_instr,
    swap_string_vector_instr,
    rot_string_vector_instr,
    flush_string_vector_instr,
    eq_string_vector_instr,
    stack_depth_string_vector_instr,
    yank_string_vector_instr,
    yank_dup_string_vector_instr,
    shove_string_vector_instr,
    empty_string_vector_instr,
    concat_integer_vector_instr,
    append_integer_vector_instr,
    take_integer_vector_instr,
    subvec_integer_vector_instr,
    first_integer_vector_instr,
    last_integer_vector_instr,
    nth_integer_vector_instr,
    rest_integer_vector_instr,
    butlast_integer_vector_instr,
    length_integer_vector_instr,
    reverse_integer_vector_instr,
    push_all_integer_vector_instr,
    empty_vec_integer_vector_instr,
    contains_integer_vector_instr,
    index_of_integer_vector_instr,
    occurrences_of_integer_vector_instr,
    set_integer_vector_instr,
    replace_integer_vector_instr,
    replace_first_integer_vector_instr,
    remove_integer_vector_instr,
    iterate_integer_vector_instr,
    concat_float_vector_instr,
    append_float_vector_instr,
    take_float_vector_instr,
    subvec_float_vector_instr,
    first_float_vector_instr,
    last_float_vector_instr,
    nth_float_vector_instr,
    rest_float_vector_instr,
    butlast_float_vector_instr,
    length_float_vector_instr,
    reverse_float_vector_instr,
    push_all_float_vector_instr,
    empty_vec_float_vector_instr,
    contains_float_vector_instr,
    index_of_float_vector_instr,
    occurrences_of_float_vector_instr,
    set_float_vector_instr,
    replace_float_vector_instr,
    replace_first_float_vector_instr,
    remove_float_vector_instr,
    iterate_float_vector_instr,
    concat_boolean_vector_instr,
    append_boolean_vector_instr,
    take_boolean_vector_instr,
    subvec_boolean_vector_instr,
    first_boolean_vector_instr,
    last_boolean_vector_instr,
    nth_boolean_vector_instr,
    rest_boolean_vector_instr,
    butlast_boolean_vector_instr,
    length_boolean_vector_instr,
    reverse_boolean_vector_instr,
    push_all_boolean_vector_instr,
    empty_vec_boolean_vector_instr,
    contains_boolean_vector_instr,
    index_of_boolean_vector_instr,
    occurrences_of_boolean_vector_instr,
    set_boolean_vector_instr,
    replace_boolean_vector_instr,
    replace_first_boolean_vector_instr,
    remove_boolean_vector_instr,
    iterate_boolean_vector_instr,
    concat_string_vector_instr,
    append_string_vector_instr,
    take_string_vector_instr,
    subvec_string_vector_instr,
    first_string_vector_instr,
    last_string_vector_instr,
    nth_string_vector_instr,
    rest_string_vector_instr,
    butlast_string_vector_instr,
    length_string_vector_instr,
    reverse_string_vector_instr,
    push_all_string_vector_instr,
    empty_vec_string_vector_instr,
    contains_string_vector_instr,
    index_of_string_vector_instr,
    occurrences_of_string_vector_instr,
    set_string_vector_instr,
    replace_string_vector_instr,
    replace_first_string_vector_instr,
    remove_string_vector_instr,
    iterate_string_vector_instr
]
