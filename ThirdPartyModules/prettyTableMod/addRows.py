from prettytable import PrettyTable

table = PrettyTable()
table.add_rows([
    [1 , "John Doe" , 23 , "Male" , 12345.98],
    [2 , "Jane Doe" , 33 , "Female" , 42345.98],
    [3 , "Park Doe" , 44 , "Male" , 42345.98],
    [4 , "Matt Doe" , 63 , "Male" , 67345.98],
    [5 , "Ruth Doe" , 23 , "Female" , 89345.98]
])
table.del_row(3) #deletes row 
table.clear_rows()
table.clear()
print(table)