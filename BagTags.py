import csv

#CSV files we will compare
bag_tags = 'tags.csv'
transactions = 'transactions.csv'

#Simple helper function, makes things easier
def list_to_lower(list : list):
    new_list = []
    for item in list:
        item = item.lower()
        new_list.append(item)
    return new_list

#Return Data will read through a csv file and return the names of the people from that file
# *WARNING* the program assumes that names will be found in the 2nd column
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

paid_list = [person for person in bag_tag_list if person in transaction_list]
print(paid_list)

def update_boolean_data(file):
    updated_data = []
    with open(file, 'r') as tag_data2:
        reader = csv.reader(tag_data2)
        for row in reader:
            if row[1] in paid_list:
                row[5] = 'True'
            updated_data.append(row)
    
    with open(file, 'w') as updated_tags:
        writer = csv.writer(updated_tags)
        writer.writerows(updated_data)

update_boolean_data(bag_tags)
print('Done!')
