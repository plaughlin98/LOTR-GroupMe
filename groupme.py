import sys, config
from datetime import datetime
from threading import Timer
from groupy.client import Client


    #### AUTH ####
def GetAllGroups():
    token = config.GROUPME_ACCESS_TOKEN
    client = Client.from_token(token)
    all_groups = client.groups.list()
    return all_groups

def GetInput(n):
    inp = input("Pick the number of the group you want: ")
    try: 
        inp = int(inp)
    except ValueError:
        print("That is not an Integer.")
        GetInput()
    if inp <= 0 or inp > n:
        print("That Number is not within range.")
        GetInput()
    else:
        return inp

def GetGroup(list_of_groups):
    group_dict = {}
    n = 1

    for group in list_of_groups:
        group_dict[n] = group.name
        print(str(n) + ': ' + group.name)
        n += 1

    group_num = GetInput(n - 1)
    for group in list_of_groups:
        if group.name == group_dict[group_num]:
            selected_group = group
            break
    return selected_group
    

def MessageGroup(group, message):
    group.post(message)


# all_groups = GetAllGroups()

# group = GetGroup(all_groups)


# print(group)


# SEND MESSAGE EVERY DAY

# x = datetime.today()
# y = x.replace(day=x.day+1, hour=10, minute=0, second=0, microsecond=0)
# delta_t = y-x

# secs = delta_t.seconds+1

# t = Timer(secs, print('hello'))
# t.start()

