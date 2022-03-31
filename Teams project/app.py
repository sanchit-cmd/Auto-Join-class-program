from pyautogui import *
from time import sleep
from datetime import *

def open_teams(): #function to open the teams app
    click(61 , 1064)#clicks the search button
    sleep(1)
    write("teams") #trypes "teams" in the search bar
    sleep(1)
    press("enter") #enter to open teams app
    sleep(60)


def close_teams(): #function toh close the teams app 
    sleep(5)
    click(1910, 13) #clicks on the X button to close the teams app

def scroll():
    sleep(5)
    click(1910 , 280)#moves the cursor to the scroll bar and scrolls the page to the top of the screen
    sleep(1)
    dragTo(1910 , 543 , 3, button="left")#drags to the calender required


def GetBoundingBoxCoordinates():
    weekDay = datetime.today().weekday()
    time = datetime.now().hour()

    origin , diagonalPoint = (0,0) , (0,0)

    origin[0] = 120 + weekDay * 248
    diagonalPoint = origin[0] + 248

    origin[1] = 207 + (9 - time) * 81
    diagonalPoint[1] = origin[1] + 81
    


def get_coordinates(): #send the coordinate for the active meeting
    origin , diagonalPoint = GetBoundingBoxCoordinates()
    for x in range(origin[0] , diagonalPoint[0]):
        for y in range(origin[1] , diagonalPoint[1]):
            if(pixel(x,y) == 91, 95, 199):
                return x,y

    return -1 , -1


def join_team(): #function to join a meeting
    sleep(5)
    click(38 , 304) #clicks on the caleder
    sleep(3)
    x,y = get_coordinates() #returns the coordinaate of the active class
    
    if x == -1 and y == -1:
        return False  
    
    doubleClick(x,y) # clicks on the class
    sleep(8)
    click(1761,101) #clicks on the join button_1
    sleep(10)
    click(1114 , 473) #clicks on the mute button
    sleep(2)
    click(1491 , 759) #clicks on the join button_2
    return True




def leave_team(): #function to leave a meeting
    sleep(10)
    click(1614 , 52) #clicks the X button of the pop up window 
    sleep(1)
    click(1614 , 52) #blank click
    sleep(2)
    click(1849, 101) #clicks the close button



open_teams() #opens the team app
time_hours = datetime.now().hour
while 9 <= time_hours <= 14: #loop will run while the time is between 9am and 2pm

    time_hours = datetime.now().hour
    time_min = datetime.now().minute
    in_meeting  = False
    

    if time_hours == 9 and time_min >= 0:
        if in_meeting == False:
            in_meeting = join_team()
        if time_hours == 9 and time_min >= 40:
            if in_meeting == True:
                leave_team()
                in_meeting = False


    elif time_hours == 10 and time_min >= 0:
        if in_meeting == False:
            in_meeting = join_team()
        if time_hours == 10 and time_min >= 40:
            if in_meeting == True:
                leave_team()
                in_meeting = False


    elif time_hours == 11 and time_min >= 0:
        if in_meeting == False:
            in_meeting = join_team()
        if time_hours == 11 and time_min >= 40:
            if in_meeting == True:
                leave_team()
                in_meeting = False


    elif time_hours == 12 and time_min >= 0:
        if in_meeting == False:
            in_meeting = join_team()
        if time_hours == 12 and time_min >= 40:
            if in_meeting == True:
                leave_team()
                in_meeting = False


    elif time_hours == 13 and time_min >= 0:
        if in_meeting == False:
            in_meeting = join_team()
        if time_hours == 13 and time_min >= 40:
            if in_meeting == True:
                leave_team()
                in_meeting = False

        


close_teams() #closes the teams app