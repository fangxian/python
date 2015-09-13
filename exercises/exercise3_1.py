from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

image=Image.open('/users/yufangxian/Documents/exercise/image.jpg')

width,height=image.size
print('the size of this image is %d * %d' % (width,height))

font=ImageFont.truetype('Arial.ttf',20)

draw=ImageDraw.Draw(image)
draw.text((width//2,height//2),chr(random.randint(50,100)),font=font,fill=(255,255,255))

image.save('/users/yufangxian/Documents/exercise/image1.jpg')
