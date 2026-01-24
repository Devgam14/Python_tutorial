def sum_nums(nums : list | tuple) -> int:
    """This function sums numbers from a list or tuple

    Args:
        nums (list | tuple): _description_

    Returns:
        int: _description_
    """
    total : int = 0
    if len(nums) == 0:
        return f'Your list {nums} is empty there is nothing to sum'
    else:
        for num in nums:
            total += num
        return f"The sum of number in a {nums} is {total}"

def name_formater (name: str):
    if name == "" :
        print("Enter your name")
    elif name.isdigit():
        print("Enter an alphabet name")
    return f"{name.strip().title()}"
user_name = "Peter"
class User:
    pass
