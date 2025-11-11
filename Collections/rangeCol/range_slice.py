##Range Slicing :
## Range Slicing is the process of creating a new collcetion from an existing collection

values = range(1, 101)
print(values)
### slicing from 4 to 20
new_range = values[3 : 20]
print(new_range)
new_range2 = values[10 : ] ## note if there are no values on the right it mean to the last character in range
print(new_range2)
new_range3 = values[9 : 49 : 2]
new_range4 = values[9 : 49 : 3]
print(list(new_range3))
print(list(new_range4))

### Negative slicing 
vals = range(1, 20)
print(list(vals[-15 : -1]))
## 4 .... 10
print(vals[-16 : -10])