import csv

#CSV files we will compare
bag_tags = 'tags.csv'
transactions = 'transactions.csv'

"""
LIST_TO_LOWER : turns all string elements in a list to lowercase, this helps to prevent names from not being updated
due to a common user input error, for example: John doe != john doe
"""
def list_to_lower(list : list):
    new_list = []
    for item in list:
        item = item.lower()
        new_list.append(item)
    return new_list

"""
RETURN_NAME_DATA : reads through a csv file and returns the names of the people from that file
*WARNING* the program currently assumes that names will be found in the 2nd column
"""
def return_name_data(file):
    myList = []
    with open(file, 'r') as tag_data:
        reader = csv.reader(tag_data,delimiter=',')
        for row in reader:
            myList.append(row[1])
    return myList

bag_tag_list = list_to_lower(return_name_data(bag_tags))
transaction_list = list_to_lower(return_name_data(transactions))


#Print statements useful for debugging

#print(bag_tag_list)
#print(' ')
#print(transaction_list)
#print(' ')

paid_list = [person for person in bag_tag_list if person in transaction_list]
#print(paid_list)

"""
UPDATE_BOOLEN_DATA : Reads through the bag tag main file and compares the name with the list of people who have paid,
if the name is present in the paid transactions file then the boolean value in the bag tag file will be updated to true
"""
def update_boolean_data(file):
    updated_data = []
    with open(file, 'r') as tag_data2:
        reader = csv.reader(tag_data2)
        for row in reader:
            if row[1].lower() in paid_list:
                row[5] = 'True'
            updated_data.append(row)
    
    with open(file, 'w') as updated_tags:
        writer = csv.writer(updated_tags)
        writer.writerows(updated_data)

update_boolean_data(bag_tags)
print('Done!')
