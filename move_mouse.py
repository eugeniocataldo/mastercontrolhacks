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

print("Mouse is now at")
print(pyautogui.position())


def search_record(text_to_write):

    """
    This function runs a search function within processes in MasterControl. You need to be in the main page (you need to see the tabs on the left)
    """

    go_to_image_and_click(process_tab)
    go_to_image_and_click(search_button)
    pyautogui.typewrite(text_to_write)
    go_to_image_and_click(submit_search_button)


def add_user_to_record():

    """
    This function adds a user to a record. You need to be inside a search and only have one record returned in your search
    """

    go_to_image_and_click(view_infocard_button)
    go_to_image_and_click(status_tab)
    go_to_image_and_click(modify_step_icon)
    go_to_image_and_click(add_user_icon)

    # Write the user to add in the textbox and press enter
    pyautogui.typewrite(user_to_add) 
    pyautogui.press('enter')
    go_to_image_and_click(add_button)
    go_to_image_and_click(save_button)
    pyautogui.typewrite("Adding user to record")
    go_to_image_and_click(save_button_second_step) #TODO: Test if it finds the right one 
    go_to_image_and_click(close)


def move_record_forward():

    """
    This function moves a record to the next step (approves it). You need to be inside a search and only have one record returned in your search
    """

    go_to_image_and_click(open_task_button)
    go_to_image_and_click(sign_off_button)
    go_to_image_and_click(empty_space_below_status) #TODO: Test whether you can see this, since you'd need to click on empty space
    go_to_image_and_click(data_approval)
    go_to_image_and_click(empty_space_below_comments) #TODO: Test whether you can see this, since you'd need to click on empty space
    go_to_image_and_click(sign_off_button) #TODO: Check whether I need to add a comment or if it can be e

