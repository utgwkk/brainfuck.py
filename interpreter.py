import sys
import re

def _generate_tree(program, ptr):
    tree = []
    while ptr < len(program):
        if program[ptr] == '[':
            leaf, nptr = _generate_tree(program, ptr + 1)
            tree.append(leaf + [']'])
            ptr = nptr
        elif program[ptr] == ']':
            return tree, ptr
        else:
            tree.append(program[ptr])
        ptr += 1
    return tree, 0


def parse(program):
    program = re.sub(r'[^\.,\+\-><\[\]]', '', program)
    return _generate_tree(program, 0)[0]


def _run(tree, memory, ptr):
    output = ''
    for ch in tree:
        if isinstance(ch, list):
            ptr, a = _run(ch, memory, ptr)
            output += a
        elif ch == '+':
            memory[ptr] += 1
        elif ch == '-':
            memory[ptr] -= 1
        elif ch == '>':
            ptr += 1
            if ptr >= len(memory):
                memory.append(0)
        elif ch == '<':
            ptr -= 1
        elif ch == '.':
            output += chr(memory[ptr])
        elif ch == ',':
            try:
                memory[ptr] = ord(sys.stdin.read(1))
            except TypeError:
                memory[ptr] = 0
        elif ch == ']':
            if memory[ptr] != 0:
                return _run(tree, memory, ptr)
            else:
                return ptr, output
    return 0, output


def run(tree):
    return _run(tree, [0], 0)[1]

