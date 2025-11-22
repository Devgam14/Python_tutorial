### encoder func
def encoderFunc (message : str):
    return message.encode(encoding="utf-32")
mess = input("enter your message :").strip()
print(encoderFunc(mess))
def decodeFunc (message : str):
    return  