# 数字类型
import math, random
# 数字类型转换
intvar, floatvar, complexvar = 1, 1.2, 5 + 4j
# int(x)
print(int(intvar))
print(int(floatvar))

# float()
print(float(intvar))
print(float(floatvar))

# complex(x)
print(complex(intvar))
print(complex(floatvar))
print(complex(complexvar))

# complex(x, y)
print(complex(intvar, intvar))
print(complex(floatvar, floatvar))
print(complex(complexvar, complexvar))

# 数学函数
print('')
print(abs(-99))
print(math.ceil(4.01))
print((2 > 1) - (2 < 1))
print(math.exp(1))
print(math.floor(-99))
print(math.log(math.e))
print(math.log(64, 2))
print(math.log10(100))
print(max(1, 2, 3, 4))
print(min(1, 2, 3, 4))
print(math.modf(1.23))
print(pow(4, 2))
print(round(12.44654, 1))
print(round(12.44654, 2))
print(math.sqrt(4))

# 随机数
print()
print(random.choice(range(5)))
print(random.randrange(0, 100, 2))
print(random.random())
print(random.seed())
listvar = [1, 2, 3]
random.shuffle(listvar)
print(listvar)
print(random.uniform(1, 5))

