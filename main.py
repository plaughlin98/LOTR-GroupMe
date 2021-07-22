import lotr
import groupme

def SendMessage():
    message = lotr.message_to_send
    print(message)
    inp = input("Do you want to send this one? Y/N")
    if inp.upper() == 'Y':
        groupme.MessageGroup(groupme.group, message)
    
        

if __name__ == '__main__':
    SendMessage()