# empty dictionary contact where key is name and value is phone number
contacts ={}

# empty list of tasks
tasks = []

# empty dictionary of notes
notes={}

#user adds contacts
def input_contact():
    name= input('enter your name:')
    number= input('enter your number:')
    contacts[name]=number
allKeys = contacts.keys()

