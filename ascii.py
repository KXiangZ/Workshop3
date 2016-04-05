lower=10
upper=100
lower_input=int(input("Enter a number({}---{}):".format(lower,upper)).strip())
upper_input=int(input("Enter a number({}---{}):".format(lower,upper)).strip())
for i in range(lower_input,upper_input):
    print('{}  {}'.format(i,chr(i)))
