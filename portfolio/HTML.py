from bs4 import BeautifulSoup
import os

class HTML:
    IMG_TEMPLATE_TAG = """
    \n <div> 
    <img class ="gallery-image" src="" title="{imageName}"> 
    </div>"""

    def __init__(self) -> None:
        self.indexPath:str = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'template')) + '\index.html'
        self.indexContent = open(self.indexPath, 'r')
        self.soup = BeautifulSoup(self.indexContent, 'html.parser')
        
    def dynamic_image_loader(self):
        print(self.soup.find(id="Gallery"))

html = HTML()
html.dynamic_image_loader()
