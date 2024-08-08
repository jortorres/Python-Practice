from array import *


vals = array('i',[5,9,-8,6])
vals.reverse()
print(vals.buffer_info())
print(vals.index)
print(vals)

print(vals[0])

for e in vals:
    print(e)