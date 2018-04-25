print('--------------- Hua: conditional--------------- ')
temp = input('Input your password:')
password = 'abc'
attempt = 0
while temp != password and attempt < 3 : 
    temp = input('Input your password:')
    if temp == password:
        print('Damn right!')
    else:
        attempt += 1
        print('Invalid password')

print('Game ends')
