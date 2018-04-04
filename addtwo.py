# given [1, 2, 3] and [2, 4, 5] return [3, 6, 8]


# add lsbs + carry, if >= 10 save new carry, if not set to 0
# if either lsb is none set it to 0

def addtwo(a1, a2):
        result = []
        carry = 0
        for i in range(max(len(a1), len(a2))):
                if len(a1) == 0:
                        op1 = 0
                else:
                        op1 = a1.pop()
                if len(a2) == 0:
                        op2 = 0
                else:
                        op2 = a2.pop()

                im = 0
                if op1 + op2 + carry >= 10:
                        im = op1 + op2 + carry - 10
                        carry = 1
                else:
                        im = op1 + op2 + carry
                        carry = 0
                result.insert(0, im)
        if carry == 1:
                result.insert(0, carry)
        return result


a1 = [1, 2]
a2 = [2, 3, 4]
result = addtwo(a1, a2)
assert result == [2, 4, 6]

a1 = [1, 2]
a2 = [8, 2, 3, 4]
result = addtwo(a1, a2)
assert result == [8, 2, 4, 6]

a1 = [9, 9]
a2 = [9]
result = addtwo(a1, a2)
assert result == [1, 0, 8]

a1 = [9, 9, 9, 9, 9, 9]
a2 = [9, 9, 9, 9]
result = addtwo(a1, a2)
assert result == [1, 0, 0, 9, 9, 9, 8]
