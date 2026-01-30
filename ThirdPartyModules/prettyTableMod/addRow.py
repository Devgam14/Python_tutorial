from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["id" , "Names" , "Age" , "Gender" , "Salary" ]
table.add_row([1 , "John Doe" , 23 , "Male" , 12345.98])
table.add_row([2 , "Jane Doe" , 33 , "Female" , 42345.98])
table.add_row([3 , "Park Doe" , 44 , "Male" , 42345.98])
table.add_row([4 , "Matt Doe" , 63 , "Male" , 67345.98])
table.add_row([5 , "Ruth Doe" , 23 , "Female" , 89345.98])
# print(table)
table.border = False
table.align = "r" ## aligns the text inside the rows uses the first characters to decribe eg : "r" for right "l" for left "c" for center
table.vertical_char = "|" ## uses the passed single string to  set the vertical char 
## search out others on pypi
# print(table.get_html_string())
# print(table.get_json_string())
# print(table.get_csv_string())
# print(table.get_formatted_string())
# print(table.get_latex_string())