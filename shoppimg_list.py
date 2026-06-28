print('welcome to the shopping list')
print('to add an items, type "add"')
print('to display the shopping list type, "show"')
print('to exit the program, type "exit"')
print('to remove an items, type "remove"')
print('—' * 40)

shopping_list = ['fruit' , 'dress for tonight', 'milk']

while True:
    user_input = input('enter your request')
    if "exit" in user_input:
        print('exit successfully')
        break

    elif "add" in user_input:
       user_input = input('what would you like to add')
       shopping_list.append(user_input)
       print('item added successfully')

    elif "show" in user_input:
        print(shopping_list)

    elif "remove" in user_input:
        user_input = input('what would you like to remove')
        if user_input in shopping_list:
            shopping_list.remove(user_input)
            print("removed successfully")
        else:
            print('please enter a valid command')

