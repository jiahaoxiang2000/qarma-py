def permutation(state: list, p: list) -> list:
    return [state[p[i]] for i in range(len(state))]


def rotate_left(value: int, shift: int) -> int:
    return ((value << shift) | (value >> (4 - shift))) & 0xF


def mix_column(state: list) -> list:
    result = state[:]
    for i in range(4):
        for j in range(4):
            index = i + j * 4
            result[index] = (
                rotate_left(state[(index + 4) % 16], 1)
                ^ rotate_left(state[(index + 8) % 16], 2)
                ^ rotate_left(state[(index + 12) % 16], 3)
            )
    return result


def s_box(state: list, S: list) -> list:
    return [S[state[i]] for i in range(len(state))]


def o_func(w: int, b: int) -> int:
    t1 = (w >> 1) | (w << (b - 1)) & ((1 << b) - 1)
    t2 = w >> (b - 1)
    return t1 ^ t2


def o_func_inverse(w: int, b: int) -> int:
    t1 = (w << 1) & ((1 << b) - 1) | (w >> (b - 1))
    t2 = w >> (b - 3) & (2)
    return t1 ^ t2


def psi_func(input: int) -> int:
    """
    LFSR ticked 23 times on 64-bit number. the primitive polynomial is x^64 + x^50 + x^33 + x^19 + 1

    Parameters:
    input (int): The input value to be processed.

    Returns:
    int: The result of the bitwise operations.
    """
    spill = input >> 51
    tmp = (
        (input << 13) & ((1 << 64) - 1)
        ^ (spill << 50)
        ^ (spill << 33)
        ^ (spill << 19)
        ^ spill
    )
    spill = tmp >> 54
    tmp = (
        (tmp << 10) & ((1 << 64) - 1)
        ^ (spill << 50)
        ^ (spill << 33)
        ^ (spill << 19)
        ^ spill
    )
    return tmp


def int_to_4bit_list(P):
    return [(P >> i) & 0xF for i in range(0, 64, 4)][::-1]


def bit_list_to_int(bit_list):
    result = 0
    for bit in bit_list:
        result = (result << 4) | bit
    return result


