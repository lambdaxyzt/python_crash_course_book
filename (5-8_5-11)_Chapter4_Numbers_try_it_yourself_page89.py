#5-8
username_list = ['admin','ali','john','take','test']
for user in username_list:
    if user == 'admin':
        print(f'hello {user}')
        print('would you like to see logs ?')
    else :
        print(f'hello {user}, thank you for logging again')
#5-9
username_list.clear()
if username_list:
    print('we need to add user')


#5-10
current_list = ['Admin','ali','John','take']
current_lower_list = []
for user in current_list :
    current_lower_list.append(user.lower())
new_user = ['ali','doe','administrator']
for user in new_user :
    if user.lower() in current_lower_list:
        print(f'{user} username used before take another name')
    else :
        print(f'{user} username is avalable')

#5-11
list = [x for x in range(1,10)]
for x in list :
    if x == 1:
        print('1st')
    elif x == 2 :
        print('2nd')
    elif x == 3 :
        print('3rd')
    else :
        print(str(x)+'th')
