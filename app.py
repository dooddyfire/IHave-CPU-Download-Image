import pandas as pd 
import requests 
from io import BytesIO
from PIL import Image

def download_img(pic_url):
    fname = pic_url.split("/")[-1].strip()
    print('fname : ',fname)
    save_path = fname 

    response = requests.get(pic_url)
    if response.status_code == 200:
        image_bytes = BytesIO(response.content)
        
        try:
            # Open the image using PIL (Pillow) with explicit format
            image = Image.open(image_bytes).convert("RGB")
            
            # Now you can work with the image, save it, display it, etc.
            image.save(save_path)
        except Exception as e:
            print(f"Failed to open image: {e}")
            return None
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return None
    print("DOwnload : {} success".format(fname))

# 'notebookfull.xlsx'
filename = input("Excel Filename : ")+".xlsx"
df = pd.read_excel(filename)

for url in df['ลิงค์รูป']: 
    lis_url = url.split("\n")
    print(lis_url)
    for item in lis_url:
        print(item)
        download_img(item)
