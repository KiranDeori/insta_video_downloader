import pip
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import webbrowser



def get_url(url , option):
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


# url = 'https://www.instagram.com/p/CRY9PR7nBDo/?utm_source=ig_web_copy_link'

url = input('Enter Your Url :')
while True:
    option = int(input('Image [0]\nVideo [1] : '))
    if (option == 1 or option == 0):
        break
    else:
        continue
 

object_url = get_url(url , option)
webbrowser.open(object_url , new=0 , autoraise=True)