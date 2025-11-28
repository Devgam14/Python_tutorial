### A void function returns none to the caller

def sum_num() : ## function body
    fn = input("Enter a number ::: ")
    sn = input("Enter a number :::: ")
    print(f"The sum of {fn} and {sn} is {int(fn) + int(sn)}") ### function body
    
sum_num() ### function calling
print(sum_num())