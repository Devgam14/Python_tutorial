import random

number_list = []
int("5")
choice = int(input('enter a number'))
for _ in range(choice * 2 ) :
    number = random.randint(1 , 11)
    number_list.append(number)


def get_pairs (pair_data) : 
  it = iter(number_list)
  for x, y in zip(it , it):
    answer = x + y 
    question = yield(f"{x} + {y} = ")  
for pairs in get_pairs(number_list):
    print(pairs)


    