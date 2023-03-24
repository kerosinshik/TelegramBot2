while True:
    password = input("Enter password: ")
    if len(password) >= 6 and password.count('#') > 0 and password.istitle():
        print('безопасный')
        break
    else:
        print('не безопасный')
