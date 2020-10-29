def login(users, username, password):
    if username in users:
        if password == users[username]:
            return True
        else:
            return False
    else:
        return False

user1 = {'username1':'password1','username2':'password2'}

print(login(user1,'username1','password1'))
print(login(user1,'username4','password4'))
print(login(user1,'username2','password3'))   