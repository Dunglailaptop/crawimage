from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import io
from PIL import Image


def download_image(download_path, url,file_name):
  try:
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name

    with open(file_path, "wb") as f:
        image.save(f,"JPEG")
    
    print("success")
  except Exception as e:
     print("falied-",e)

url = "https://scontent-iad3-2.cdninstagram.com/v/t39.30808-6/451434605_18009978725612819_8955400465035953635_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDc5eDEwNzkuc2RyLmYzMDgwOCJ9&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_ohc=yXG5SQLh9O0Q7kNvgEcC53c&edm=APs17CUAAAAA&ccb=7-5&ig_cache_key=MzQxMzE4OTI5NDQ5ODQ4NTcxOA%3D%3D.2-ccb7-5&oh=00_AYB57ZvAR2_SDDqiSTi6ZtquARIfAttvvLVBToZ_HzHRrw&oe=669DBF5F&_nc_sid=10d13b"

download_image("",url,"TEXT.jpg")
# Set the path to the Chrome WebDriver executable
chrome_driver_path = "chromedriver.exe"

# Initialize the Chrome service with the correct path to Chrome executable
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome WebDriver with the service
driver = webdriver.Chrome(service=service)

# Open the desired URL
driver.get("https://www.thegioididong.com")

driver.maximize_window()


time.sleep(10)

driver.quit()
