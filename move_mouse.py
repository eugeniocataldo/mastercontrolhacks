"""
This script moves the mouse to do some stupid shit in MasterControl. Start
it in the homepage of MasterControl since that's where the hard-coded 
positions work.
The homepage of MasterControl needs to be open on the laptop screen, won't
work on a different-sized monitor
"""

#TODO: Add pauses or figure out if the click function can have a timer

import pyautogui, time
pyautogui.useImageNotFoundException()



def select_image(all_images, position):


    """
    Helper function for look_for_image, to tackle the case in which there are multiple images

    Inputs:
    - all_images (iterator from pyautogui.locateAllOnScreen()): Iterator containin all the images on screen
    - position (string): Text with where the image is

    """

    left_pixels = []
    top_pixels = []
    images = []

    for image in all_images:
        images.append(image)
        left_pixels.append(image.left)
        top_pixels.append(image.top)

    if position == 'Top':
        my_index = top_pixels.index(min(top_pixels))
    else:
        raise NotImplementedError("The position you want is not implemented")
    
    print(images)

    selected_image = images[my_index]
    center_x = selected_image.left + selected_image.width/2
    center_y = selected_image.top + selected_image.height/2

    return center_x, center_y


def look_for_image(image_path, multiple_images=False, confidence=0.999):

    """
    This function takes a filepath for an image and finds it on the screen
    
    Inputs:
    - image_path (string): filepath for the image to look for
    - multiple_images (bool): True if the image comes more times in the screen (default False)
    - confidence (float): confidence for the image location algorithm (default is the function default)
    """

    image_found = False
    timeout = 60 # If the image is not found in 1 minute, return error
    timeout_start = time.time()


    ### Look for the image by scrolling
    while not image_found and time.time() < timeout_start + timeout:
        
        try:
            if multiple_images:
                all_images = pyautogui.locateAllOnScreen(image_path)
            else:
                click_location_x, click_location_y = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        except pyautogui.ImageNotFoundException:
            pyautogui.scroll(-50)
            print("Image not found, scrolling down")
        else:
            image_found = True
            
    if time.time() > timeout_start + timeout:
        raise TimeoutError("Couldn't find the image within the time")
    
    if multiple_images:
        click_location_x, click_location_y = select_image(all_images=all_images, position="Top") #For now it's only the top one, will check if more are needed
        #TODO: If it remains only top, can probably delete because it automatically picks the top one
    
    return click_location_x, click_location_y




def click_on_image(image_path, multiple_images=False, confidence=0.8):

    """
    This function takes a filepath for an image and finds it on the screen
    
    Inputs:
    - image_path (string): filepath for the image to look for
    - multiple_images (bool): True if the image comes more times in the screen (default False)
    """
    
    click_location_x, click_location_y = look_for_image(image_path, confidence=confidence)
    
    pyautogui.click(click_location_x, click_location_y)

    time.sleep(1) # Wait 4 seconds to make sure the click has been loaded
    print("Done with one click! Moving to the next")


def search_record(text_to_write):

    """
    This function runs a search function within processes in MasterControl. You need to be in the main page (you need to see the tabs on the left)
    """

    click_on_image('images/process_tab.PNG', confidence=0.8)
    click_on_image('images/search_button.PNG', confidence=0.8)
    for _ in range(40):
        pyautogui.press('delete')
    pyautogui.typewrite(text_to_write)
    time.sleep(1)

    click_on_image('images/submit_search_button.PNG', confidence=0.8)
    print("Finished with searching")

def add_user_to_record(user_to_add):

    """
    This function adds a user to a record. You need to be inside a search and only have one record returned in your search
    """
    print("Starting to add user")
    time.sleep(2)
    click_on_image('images/view_infocard_button.PNG')
    print("Here already")
    click_on_image('images/status_tab.PNG')
    click_on_image('images/modify_step_icon.PNG')
    click_on_image('images/add_user_icon.PNG')

    # Write the user to add in the textbox and press enter
    pyautogui.typewrite(user_to_add) 
    pyautogui.press('enter')
    time.sleep(4)
    click_on_image('images/add_button.PNG', confidence=0.999)
    click_on_image('images/save_button.PNG', confidence=0.8)
    pyautogui.typewrite("Adding user to record")
    click_on_image('images/save_button_second_step.PNG') #TODO: Test if it finds the right one 
    click_on_image('images/close_button.PNG')


def move_record_forward(approve, sign_off_message):

    ### UNTESTED

    """
    This function moves a record to the next step (approves it). You need to be inside a search and only have one record returned in your search
    
    Inputs:
    - approve (bool): True if need to approve the record, false if need to reject the record
    - sign_off_message (string): string containing the text to write in the comments when moving the record
    """

    click_on_image('images/open_task_button.PNG')
    click_on_image('images/sign_off_button.PNG', confidence=0.8)
    click_on_image('images/empty_space_below_status.PNG', confidence=0.8) #TODO: Test whether you can see this, since you'd need to click on empty space
    if approve:
        click_on_image('images/data_approval.PNG', confidence=0.8) #TODO: Check if it works because it changes when hovering over it with the cursor
    else:
        click_on_image('images/data_rejection.PNG', confidence=0.8) #TODO: Check if it works because it changes when hovering over it with the cursor
    click_on_image('images/empty_space_below_electronic_signature.PNG', confidence=0.8)
    click_on_image('images/my_saved_password.PNG', confidence=0.8)    
    click_on_image('images/empty_space_below_comments.PNG', confidence=0.8) #TODO: Test whether you can see this, since you'd need to click on empty space
    pyautogui.typewrite(sign_off_message)
    click_on_image('images/sign_off_button_second_step.PNG', confidence=0.8) #TODO: Check whether I need to add a comment or if it can be e




print("Mouse is now at")
print(pyautogui.position())


#search_record('OOS-OOT-2023-0404')
#add_user_to_record("Eugenio")
#search_record('OOS-OOT-2023-0404')
move_record_forward(approve=False, sign_off_message="Testing")
#search_record('OOS-OOT-2023-0404')
#add_user_to_record("Eugenio")


### Testing box
x, y = look_for_image('images/empty_space_below_status.PNG', confidence=0.8)
pyautogui.moveTo(x, y, duration=1)



