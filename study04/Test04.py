# 运算符
# 位运算符
a, b = 60, 22;
print('a=' + bin(a)[2:]);
print('b=' + bin(b)[2:]);

# &
print('a&b=' + bin(a & b)[2:]);
print('a&b=' + str(a & b));

# |
print('a|b=' + bin(a | b)[2:]);
print('a|b=' + str(a | b));

# ^
print('a^b=' + bin(a ^ b)[2:])
print('a^b=' + str(a ^ b));

# ~
print('~a=' + '-' + bin(~ a)[3:])
print('~a=' + str(~ a));

# <<
print('a<<1=' + bin(a << 1)[2:])
print('a<<1=' + str(a << 1));

# >>
print('a>>1=' + bin(a >> 1)[2:])
print('a>>1=' + str(a >> 1));
