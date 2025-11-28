

### Non-Default paramerts

def sum_num(fn : int , sn : int) -> str :
    if not isinstance(fn, int) or not isinstance(sn, int):
        return "Both parameters must be intergers."
    return f"The sum of {fn} and {sn} is {int(fn) + int(sn)}" ### Function body

### note arguments are passe when a function is called while paramets are passed when a function is created and you can write out the types of the poarameters and its retuen type eg :  sum_num(fn : int , sn : int) -> str :
res1 = sum_num(23, 45)
res2 = sum_num(234 , 45)
print(res1)
print(res2)