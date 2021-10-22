from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
import uuid
import wget

def get_url(url , option):
    """
    This function will get the url from user
    an according to the option given by the user 
    it will return the downlodable link for that image or video
    """

    chrome_options = Options()
    chrome_options.headless = True
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    soup = BeautifulSoup(browser.page_source , features='html5lib')

    if (option == 0):
        get_meta = soup.find('meta' , property='og:image')
        image_link = get_meta['content']
        return image_link
    elif (option == 1):
        get_meta = soup.find('meta' , property='og:video')
        video_link = get_meta['content']
        return video_link
    else:
        return None


def save_download(url_download , option):
    """
    This function will download the image
    and save it to the image folder of the current directory
    """
    # getting the current directory path
    path = os.getcwd()
    path_image = os.path.join(path , "images")
    path_video = os.path.join(path , "videos")
    
    # make a unique code for images
    unique_id = uuid.uuid4()

    # saving images to folders
    if option == 0:
        save_as_image = os.path.join(path_image , f'image_{unique_id}.jpg')
        wget.download(url_download , save_as_image)
    elif option == 1:
        save_as_video = os.path.join(path_video , f'video_{unique_id}.mp4')
        wget.download(url_download , save_as_video)
    else:
        raise ValueError('link is not valid')
        




url = input('Enter Your Url :')
while True:
    option = int(input('Image [0] Video [1] : '))
    if (option == 1 or option == 0):
        break
    else:
        continue
 

object_url = get_url(url , option)
save_download(object_url , option)