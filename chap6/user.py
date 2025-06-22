#Loging information reference using dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

#To access all infromation stored in dictionary using a loop
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
