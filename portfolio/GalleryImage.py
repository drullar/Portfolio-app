from bs4 import BeautifulSoup

class GalleryImage:
    
    IMG_TEMPLATE_TAG = """
    \n <div> 
    <img class ="gallery-image" src="" title=""> 
    </div>"""
    soup = BeautifulSoup(IMG_TEMPLATE_TAG, 'html.parser')
    imgTag: str
    def __init__(self, imgPath:str = "", imgTitle: str = ""):
        self.soup.img.src = "hehexd"
        print(self.soup.img)
        
image = GalleryImage()
