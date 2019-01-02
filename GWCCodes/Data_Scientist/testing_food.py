import food

list_of_food = food.get_reports(test=False)
'''
for item in list_of_food[5]:
    print("----KEY ", item, " ----")
    print(list_of_food[5][item])
    print('\n')
'''
x = 0
num_cheese = 0
for item in list_of_food:
    if "CHEESE" in item["Description"]:
        print("--- ", item["Category"], " ---")
        print(item['Description'])
        '''
        for item in list_of_food[x]:
            print("----KEY ", item, " ----")
            print(list_of_food[x][item])
            print('\n')
        '''
        num_cheese += 1
    #else:
        #print("No Cheese Found")
    x += 1

print("There are ", num_cheese, " different kinds of cheese!")
