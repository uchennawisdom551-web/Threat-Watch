print('-' * 40)
print("Alert Detection")
print('-' * 40)

success = 0
failed = 0
with open('logs.txt', 'r')as file:
    for line in file:
        if "LOGIN_SUCCESS" in line:
             
             success+=1
        else:
             failed+=1

    print(f'Successful logins: {success}')
    print(f'Failed Attempts: {failed}')
             
    