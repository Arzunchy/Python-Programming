"""
Bitwise operators work on numbers at the binary (bit) level, not decimal.
& → AND

| → OR

^ → XOR (different bits)

~ → NOT (flip bits)

<< → Shift left

>> → Shift right
"""
# 1️⃣ AND — &
"""
Rule: Result bit is 1 only if both bits are 1.

0101
0011
----
0001  → 1
"""
a = 5
b = 3
print(a & b)   # Output: 1

#2️⃣ OR — |
"""
Rule: Result bit is 1 if at least one bit is 1.

0101
0011
----
0111 → 7
"""
print(a | b)   # Output: 7

#3️⃣ XOR — ^
"""
Rule: Result bit is 1 if bits are different.

0101
0011
----
0110 → 6
"""

print(a ^ b)   # Output: 6
"""
Example swap trick:

x = 4  #            1001
y = 9               0100 ~
                    1101             
x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)   # 9 4
"""

#4️⃣ NOT — ~
"""
Rule: Flips all bits (1→0, 0→1)

Python uses signed integers, so:

~a = -(a + 1)
"""
print(~5)   # Output: -6 # Remember shortcut:
#~n = -(n+1)

#5️⃣ Left Shift — <<
"""
Rule: Shift bits left → multiply by 2 each shift

5 = 0101
5 << 1 → 1010 → 10
5 << 2 → 10100 → 20
"""

print(5 << 1)   # 10
print(5 << 2)   # 20
# Fast multiplication by powers of 2.

#6️⃣ Right Shift — >>
"""
Rule: Shift bits right → divide by 2 each shift

0101 >> 1 → 0010 → 2
"""
print(5 >> 1)   # 2
print(5 >> 2)   # 1
# Fast integer division by powers of 2.