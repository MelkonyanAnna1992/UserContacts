import json


def readUserContactsInfo():
    with open('./info.json') as data_file:
        v_data = json.load(data_file)

    return v_data


def addNewUserContact(v_data):
    # Initilizing the contact_info values using tuple
    contact_info = ("first_name", "last_name", "phone")
    current_dict = {}

    print("Please add appropriate creadentials one by one.")
    for info in contact_info:
        current_dict[info] = str(input("Please insert a {} info.\n".format(info)))

    # Adding new user contact information with exists information
    v_data.append(current_dict)

    # Writing information into JSON format file.
    to_json(v_data)
    print("-"*70)
    print("User contacts information added.")
    print("-"*70)


def getUserPhoneNumber(v_data):
    user_name = str(input("Please give first name or last name: "))
    v_found = False
    for user_info in v_data:
        if (user_info["first_name"] == user_name or user_info["last_name"] == user_name):
            print("="*70)
            print("First Name: " + user_info["first_name"] + " - Last Name: " + user_info   ["last_name"] + " - Phone number: " + user_info["phone"] + '.')
            print("="*70)
            v_found = True
            break
    if not v_found:
        print("-"*70)
        print("\nUser not found.")
        print("-"*70)


def deleteAllUserContacts(v_data):
    v_data.clear()
    print("-"*70)
    print("\nThe contact lisat is empty.")
    print("-"*70)
    # Writing information into JSON format file.
    to_json(v_data)


def to_json(v_data):
    # Seting output json file name value.
    v_file_name = "UserContactInfo.json"

    # Writing information into JSON file.
    with open(v_file_name, "w") as outfile:
        json.dump(v_data, outfile, indent=4, sort_keys=True)

v_data = {}
v_first_run = True
# Starting program
while True:
    if v_first_run:
        v_data = readUserContactsInfo()
        v_first_run = False
    print("-"*70)
    print("\nPlease insert the appropriate mode value in integer format.")
    print("\n\
    1 - Add new user contacts \n\
    2 - Get user phone number \n\
    3 - Clear all users information \n\
    0 - Exit\n")
    print("-"*70)
    try:
        v_mode = int(input("Choose mode: "))
        if (v_mode == 0):
            print("Program terminated.")
            break
        elif (v_mode == 1):
            addNewUserContact(v_data)
        elif (v_mode == 2):
            getUserPhoneNumber(v_data)
        elif (v_mode == 3):
            deleteAllUserContacts(v_data)
    except ValueError:
        print("-"*70)
        print("Please insert only integer value from 0 to 4 value.")
        print("-"*70)
