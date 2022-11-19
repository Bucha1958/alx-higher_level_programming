#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

dis.dis(magic_calculation)
bytecode = dis.code_info(magic_calculation)
print(bytecode)

bytecode = dis.Bytecode(magic_calculation)
print(bytecode)

for i in bytecode:
    print(i)
