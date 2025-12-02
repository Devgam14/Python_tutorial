def values (val : int) :
    "'' This function returns sum of two numbers"
    return lambda num : num * val
nums = values(7)
print(nums)
num_res : int = nums(3)
print(num_res)