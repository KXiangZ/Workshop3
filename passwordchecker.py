MIN_LENGTH=5
MAX_LENGTH=15
SPECIALS = "!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|"
specialcheck=0
lowercheck=0
uppercheck=0
digitcheck=0
output=False

while output==False:
    password=input("""Please enter a valid password
    Your password must be between 5 and 15 characters, and contain:
    1 or more uppercase characters
    1 or more lowercase characters
    1 or more numbers
    and 1 or more special characters:	!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|
    """)

    for i in password:
        if i.islower():
            lowercheck+=1
        elif i.isupper():
            uppercheck+=1
        elif i.isdigit():
            digitcheck+=1
        elif i in SPECIALS:
            specialcheck+=1

    length=len(password)

    if length>=MIN_LENGTH and length<=MAX_LENGTH and lowercheck>0 and uppercheck >0 and specialcheck>0 and digitcheck>0:
         print('Your {} character password is valid: {}'.format(length,password))
         output=True
    else:
        print('Invalid password!')
