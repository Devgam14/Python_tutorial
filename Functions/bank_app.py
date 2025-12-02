balance : float = 0.0
acct_num : str = "123456"

def save_money (amount : float , account : str) :
    '''
    Save function :::: 
    Parameters : amount : float,  account : string 
    it returns None type
    '''
    global balance
    if account == acct_num:
        balance += amount
        print(f"You have saved #{amount} to {acct_num} number")
        
    print("Pls check your details")
    
    
def check_bal (account : str) -> float:
    '''
     Check balance 
     Parameters :
        account : str
    returns float
    '''
    if account == acct_num :
        return balance
    return ' Check your account details '

def witdraw_money ( amount : float , account : str) -> float :
    '''
        withdraw_money 
        Parameters : 
            amount : float ,
            account : str
        returns float
    '''
    global balance
    if account == acct_num :
        if (amount < balance) :
            balance -= amount 
            return amount
    else :
        return "Check your account details"
         

help(save_money)
help(check_bal)
help(witdraw_money)
save_money(600.4 , "123456")
print(check_bal("123456"))
print(witdraw_money(200 , "123456"))
print(witdraw_money(400 , "123456"))
print(check_bal("123456"))


