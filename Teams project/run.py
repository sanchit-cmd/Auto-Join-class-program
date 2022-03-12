from ntpath import join
from pyautogui import *
from time import *
from datetime import *

def open_teams(): #function to open the teams app
    sleep(5)
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

def join_team(): #function to join a meeting
    sleep(5)
    click(38 , 304) #clicks on the caleder
    scroll()
    sleep(3)
    x,y = 1242,609 #returns the coordinaate of the active class
    doubleClick(x,y) # clicks on the class
    sleep(8)
    click(1761,101) #clicks on the join button_1
    sleep(10)
    click(1114 , 473) #clicks on the mute button
    sleep(2)
    click(1491 , 759) #clicks on the join button_2

def leave_team(): #function to leave a meeting
    sleep(10)
    click(1614 , 52) #clicks the X button of the pop up window 
    sleep(1)
    click(1614 , 52) #blank click
    sleep(2)
    click(1849, 101) #clicks the close button


open_teams() #opens the team app
join_team()
sleep(2)
leave_team()
close_teams()