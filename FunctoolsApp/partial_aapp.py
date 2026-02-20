from functools import partial
def power(a,b) :
    return a ** b
pow2 = partial(power, b=2)
pow4 = partial(power , b=4)
power_of_5 = partial(power, 5)

print(power(2,3))
print(pow2(4))
print(pow4(3))
print(power_of_5(2))
print(power(4, 3))

print(pow2.func)
print(pow2.keywords)
print(power_of_5.args)