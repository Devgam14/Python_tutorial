testingList = ["gam" , "james" , "campelte" , "helloa"]
tester2 = ["bro", "hey", "henry", "ador"]
tester3 = ["bro", "hey", "henry", "ador", "great", "gomear"]

def vowelsSorter (List) -> list :
    '''
    Docstring for vowelsSorter
    vowelSorter sorts a list of words returning those words containing the vowels "a" and "e" in them else returns the list a message\n
    :param List: List
    :return: list 
    :rtype: list
    '''
    orderedList  = []
    if  type(List) == list:
        for index in List :
            for word in index:
                if "a" and "e" in word  or "e" and "a" in word:
                    orderedList.append(index)
                return f"List argument does not have the a and e vowel in it {List}"
        return orderedList
    return f"the argument being passed {List} is not a list"
print(vowelsSorter(testingList))
print(vowelsSorter("hey"))
print(vowelsSorter(tester2))
print(vowelsSorter(tester3))


"""
 WRITE A SCRIPT FOR A FIVE YEAR OLD CHILD USED TO RUN 
 SCRIPT ASKES FOR NAME OF THE CHILD AND AGE DETAILS 
 A LIST OF OPERATIONS THAT THE CHILD CAN PERFORM
 THAT USES NUMBERS TO NOTE LIKE IN USSSD 
 IT GENERATE RANDOM QUESTIONS FROM THE OPERATION SHE CHOOSE
 A MATHEMATICAL QUIZ FOR CHILDREN 
 IT PRINTS OUT A MESSAGE CONCERNING THE PERFORMANCE OF THE QUIZ 
"""

















