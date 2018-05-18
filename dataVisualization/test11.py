# a = list(range(5))
# c = a
# b = {}.fromkeys(a,c)
#
# print(b)
# I think these functions could be refactored using the operator module.
# But I don't think it should be "fast" or "elegant" in this way. Just clear like this.
import itertools
x = "asddddff"
y = itertools.groupby(x)
b = []
for i, v in y:
    a = list(v)
    b.append(a)
print(max(b, key=len))

def long_repeat(line):
    count =0
    for char in line:
        newchar = char
        while(line.count(newchar)>0):
            newchar += char
            # print(newchar)
        if count < len(newchar)-1:
            count = len(newchar)-1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert long_repeat('sdsffffse') == 4, "First"
    # assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaaab') == 3, "Third"
    # assert long_repeat('') == 0, "Empty"
    # print('"Run" is good. How is "Check"?')
