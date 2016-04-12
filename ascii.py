def get_number(lower,upper):
    user_input=input("Enter a number ({} - {})".format(lower,upper))
    while True:
        if user_input.isdecimal():
            if int(user_input) <upper and int(user_input) > lower:
                break
        print("Please enter a valid number!")
        user_input=input("Enter a number ({} - {})".format(lower,upper))




lower=10
upper=100
lower_input=int(input("Enter a number({}---{}):".format(lower,upper)).strip())
upper_input=int(input("Enter a number({}---{}):".format(lower,upper)).strip())
for i in range(lower_input,upper_input):
    print('{}  {}'.format(i,chr(i)))

get_number(lower_input,upper_input)