'''
Find the angle between the hour and minute hand at a given time
'''

#setting variable
time = ""
hour = ""
minute = ""
number= 0
test = False
test1=False
x=""


#Input a specific time

while test==False:
    try:
        time = input("Input a time in the following format: xxxx\n")


        #checking that input is valid
        while test1 == False:
            try:
                for a in time:

                    #checking if inputs are valid integer
                    if a.isdigit():

                        #getting hour number in string
                        if number >=0 and number <2:
                            hour +=a

                        #getting minute number in string 
                        elif number >=2 and number <=3:
                            minute += a

                        number +=1
                    
                    else:
                        raise ValueError
                #checking that there is the correct number of inputs   
                if number !=4:
                        raise ValueError
                else:
                   test=True

            except ValueError:
                    print("Please enter the valid integer in valid format!")
            finally:
                break #break test1 while loop

            break #break test while loop

    except:
        pass
        
       

minute = int(minute)
hour = int(hour)

if hour ==12: 
    hour = 0 #sets degrees starting witth 0 degrees at 12 o'clock


#Find angle for hour hand

#30 degrees per hour since the clock is 360 degrees divided by 12
#The clock moves per minute thus there is an additional 0.5 degrees per minute that the hand moves
    #(30 degrees divide by 60 minutes)
hour_angle=hour * 30 + 0.5 * minute


#find angle for minute hand
#the minute hand moves 360/60 = 6 degrees per minute
minute_angle = minute*6


#finding angle between the two hands (smaller angle and bigger angle)
if hour_angle > minute_angle:
    small_angle_total =hour_angle-minute_angle
    big_angle_total = minute_angle - hour_angle +360
    
else:
    small_angle_total = minute_angle - hour_angle
    big_angle_total =hour_angle-minute_angle +360
    


print("The smaller angle between the hour and minute hands is %0.1f" %small_angle_total)
print("The bigger angle between the hour and minute hands is %0.1f" %big_angle_total)


