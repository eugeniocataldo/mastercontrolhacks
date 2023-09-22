"""
This script moves the mouse to do some stupid shit in MasterControl. Start
it in the homepage of MasterControl since that's where the hard-coded 
positions work.
The homepage of MasterControl needs to be open on the laptop screen, won't
work on a different-sized monitor
"""

#TODO: Add pauses or figure out if the click function can have a timer

import pyautogui, time

def go_to_image_and_click(image_path):

    """
    This function takes a filepath for an image and finds it on the screen
    
    Inputs:
    - image_path (string): filepath for the image to look for
    """
    
    image_found = False
    timeout = 300 # [seconds]
    timeout_start = time.time()
    
    while not image_found and time.time() < timeout_start + timeout:
        
        try:
            click_location_x, click_location_y = pyautogui.locateCenterOnScreen(image_path)
        except ImageNotFoundException:
            pyautogui.scroll(10)
        else:
            image_found = True
            
            
    if time.time() < timeout_start + timeout:
        raise TimeoutError("Couldn't find the image within the time")
    

    
    pyautogui.click(click_location_x, click_location_y)
    
    



print("Mouse is now at")
print(pyautogui.position())

PROCESS_TAB = (40, 499)
SEARCH_PROCESS = (1080, 403)
SEARCH_TEXTBOX = (287, 584)
SUBMIT_SEARCH = (1554, 706)
VIEW_INFOCARD = (1870, 501)
STATUS_TAB_IN_RECORD = (1671, 713)
# MODIFY_STEP = (???,???) # TODO: Find out if this position stays the same
ADD_USER = (905, 602)
duration = 1


text_to_write = []

#pyautogui.click(pyautogui.position())

#pyautogui.scroll(-1000) #TODO: Check if the plus position changes

pyautogui.moveTo(ADD_USER, duration = duration)

pyautogui.moveTo(SUBMIT_SEARCH, duration = duration)

"""
pyautogui.click(PROCESS_TAB)
pyautogui.click(SEARCH_PROCESS)
pyautogui.click(SEARCH_TEXTBOX)
pyautogui.typewrite(text_to_write)
pyautogui.click(SUBMIT_SEARCH)
pyautogui.click(VIEW_INFOCARD)
pyautogui.click(STATUS_TAB_IN_RECORD)

go_to_image_and_click(modify_step_icon) #TODO: Add modify step icon

pyautogui.typewrite(user_to_add)
pyautogui.press('enter')
pyautogui.scroll(X) #TODO: Find out how much I need to scroll or adapt this to big screen so don't need it
go_to_image_and_click(add_icon) #TODO: Add image of the add icon 
pyautogui.click(save_button) #TODO: Find coordinate of the button or image
pyautogui.typewrite("Adding user to record")
pyautogui.click(SAVE_BUTTON) #TODO: Add coordinates for this because there are two "save" in the image





#pyautogui.moveTo(PROCESS_TAB)

"""