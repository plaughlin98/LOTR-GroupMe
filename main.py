import lotr
import groupme

def SendMessage():
    groupme.MessageGroup(groupme.group, lotr.message_to_send)

if __name__ == '__main__':
    SendMessage()