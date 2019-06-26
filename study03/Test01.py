# 整形
# var1 = 1;
# 浮点型
# var2 = 1.1;
# 字符型
# var3 = 'String';
#
# print(var1);
# print(var2);
# print(var3);

# 多变量
# var_a = var_b = 1;
# print(var_a);print(var_b);
# var_c, var_d = 2.3, 'var_d';
# print(var_c, var_d);
#
# str4 = '1.1';
# print('\n')
# print('\n')
# print(str4[0:0])

# number
# int
# intvar, floatvar, boolvar, complexvar = 1, 1.1, True, 4+3j;
# print(type(intvar), type(floatvar), type(boolvar), type(complexvar));
# print(isinstance(intvar, int));

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
# var4, var5 = 1, 2;
# print(var4, var5);
# del var4, var5;
# print(var4, var5);

# 加
# print(5 + 4);
# # 减
# print(4.3 - 2);
# # 乘
# print(3 * 7);
# #  除
# print(2 / 4);
# # 除整
# print(2 // 4);
# # 余
# print(17 % 3);
# # 乘方
# print((2 ** 8) ** 4 // 2);
#
# str1 = 'test';
# print(str1 * 3)

# 列表
# list = [1, 2,  3]
# print(list);
# print([1, 2,  3] + [5, 6] * 2);
list = [5, 6, 5, 8] * 2;
print(list);

# 元组Tuple
tuple = (1, 2, 3);
print(tuple);

# Set
myset = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(myset);

print(myset);

# 字典 Dictionary
dictionary = {};
dictionary['one'] = '1';
dictionary[2] = '2';
print(dictionary.keys() - set());

print(dict([('a', 'b'), (2, 5)]).keys() - set());
print(dict(a = 1, b = 2).keys() - set());

x = '''
sadf
''';
print(repr(x));

print(eval('str((1 * 2 + 3)) + x'));