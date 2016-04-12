def recArea():
    length=int(input('Enter length:'))
    width=int(input('Enter width:'))
    area=length*width
    result='The area of the rectangle is {}'.format(area)
    return result

def tempConv():
    celsius=int(input('Enter the temperature(celsius):'))
    fahrenheit=celsius*1.8+32
    result='The temperature is {} in fahrenheit'.format(fahrenheit)
    return result

def BMI():
    height=float(input('Enter height in m:'))
    weight=float(input('Enter weight in kg:'))
    bmi=weight/(height*height)
    result='Your BMI value is {:,.2f}'.format(bmi)
    return result

user_input=input("""For Rectangle Area enter R
For Temperature converter enter T
For BMI enter B
To exit, enter Q""").lower()

while user_input!= "r" and user_input!="t" and user_input!= "q" and user_input!= "b":

    print("Error, please try again")
    user_input=input("""For Rectangle Area enter R
For Temperature converter enter T
For BMI enter B
To exit, enter Q""").lower()

while user_input!= "q":
    if user_input=="r":
        print(recArea()+"\n")
        user_input=input("""For Rectangle Area enter R
For Temperature converter enter T
For BMI enter B
To exit, enter Q""").lower()
    elif user_input=="t":
        print(tempConv()+"\n")
        user_input=input("""For Rectangle Area enter R
For Temperature converter enter T
For BMI enter B
To exit, enter Q""").lower()
    elif user_input=="b":
        print(BMI()+"\n")
        user_input=input("""For Rectangle Area enter R
For Temperature converter enter T
For BMI enter B
To exit, enter Q""").lower()
    elif user_input=="q":
        quit()



