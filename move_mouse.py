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
    timeout = 60 # If the image is not found in 1 minute, return error
    timeout_start = time.time()


    ### Look for the image by scrolling
    while not image_found and time.time() < timeout_start + timeout:
        
        try:
            click_location_x, click_location_y = pyautogui.locateCenterOnScreen(image_path)
        except pyautogui.ImageNotFoundException:
            pyautogui.scroll(10)
        else:
            image_found = True
            
            
    if time.time() < timeout_start + timeout:
        raise TimeoutError("Couldn't find the image within the time")
    
    
    pyautogui.click(click_location_x, click_location_y)

    time.sleep(4) # Wait 4 seconds to make sure the click has been loaded


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

    click_on_image('images/view_infocard_button.PNG')
    click_on_image('images/status_tab.PNG')
    click_on_image('images/modify_step_icon.PNG')
    click_on_image('images/add_user_icon.PNG')

    # Write the user to add in the textbox and press enter
    pyautogui.typewrite(user_to_add) 
    pyautogui.press('enter')
    time.sleep(1)
    click_on_image('images/add_button.PNG')
    click_on_image('images/save_button.PNG', confidence=0.8)
    pyautogui.typewrite("Adding user to record")
    click_on_image('images/save_button_second_step.PNG') #TODO: Test if it finds the right one 
    click_on_image('images/close_button.PNG')


def move_record_forward():

    """
    This function moves a record to the next step (approves it). You need to be inside a search and only have one record returned in your search
    """

    click_on_image(open_task_button)
    click_on_image(sign_off_button)
    click_on_image(empty_space_below_status) #TODO: Test whether you can see this, since you'd need to click on empty space
    click_on_image(data_approval)
    click_on_image(empty_space_below_comments) #TODO: Test whether you can see this, since you'd need to click on empty space
    click_on_image(sign_off_button) #TODO: Check whether I need to add a comment or if it can be e




print("Mouse is now at")
print(pyautogui.position())
