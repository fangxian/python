import os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
class Pict:
    def __init__(self,w,h,r,g,b):
        self.image=Image.new('RGB',(w,h),(r,g,b))
    
    def random_char(self):
        return chr(random.randint(65,90))
    
    def random_color(self):
        return (random.randint(50,200),random.randint(50,200),random.randint(50,200))

    def random_color2(self):
        return (random.randint(25,100),random.randint(25,100),random.randint(25,100))
    def savefunc(self):
        self.image.save('/users/yufangxian/Documents/exercise/image3.jpg','jpeg')

picture=Pict(240,40,255,255,255)
#width=240
#height=60
#image=Image.new('RGB',(width,height),(255,255,255))

font=ImageFont.truetype('Arial.ttf',20)
draw=ImageDraw.Draw(picture.image)

for x in range(240):
    for y in range(40):
        draw.point((x,y),fill=(0,0,0))

draw.text((200,5),picture.random_char(),font=font,fill=(200,200,200))

picture.savefunc()
        
#image=image.filter(ImageFilter.BLUR)
#picture.image.save('/users/yufangxian/Documents/exercise/image2.jpg','jpeg')
