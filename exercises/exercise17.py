from __future__ import print_function
import os,sys
from PIL import Image,PSDraw
from PIL import ImageFilter
from PIL import ImageEnhance
#import PSDraw
'''
size=(128,128)

f=os.path.splitext('/users/yufangxian/Documents/exercise/picture/2.jpg')[0]+'thumbnail.jpg'
im=Image.open('/users/yufangxian/Documents/exercise/picture/2.jpg')
im.thumbnail(size)
im.save(f,'JPEG')
#print(f,e)
#outfile=f+'.jpg'
'''
'''
try:
    Image.open('/users/yufangxian/Documents/exercise/picture/2.bmp').save(outfile)
except IOError:
    print('cannot convert','/users/yufangxian/Documents/exercise/picture/2.bmp')
'''
'''
with Image.open('/users/yufangxian/Documents/exercise/picture/2.jpg') as im:
    print(im.format,"%d*%d" % im.size,im.mode)
    box=(500,500,1400,1400)
    region=im.crop(box)
    region=region.transpose(Image.ROTATE_90)
    region.show()
    #im.paste(region,box)
    region.save('/users/yufangxian/Documents/region.jpg','JPEG')
'''
with Image.open('/users/yufangxian/Documents/exercise/picture/2.jpg') as im:
    im.size
    im.load(scale=2)
    im.size
    im.show()
    
'''
    r,g,b=im.split()
    im=Image.merge('RGB',(b,g,r))
    im.show()
    out=im.resize((128,128))
    out=im.rotate(45)
    out.show()
    out=im.transpose(Image.FLIP_LEFT_RIGHT)
    out.show()
    out=im.transpose(Image.FLIP_TOP_BOTTOM)
    out.show()
    out=im.convert('L')
    out.show()
    out=im.filter(ImageFilter.DETAIL)
    out.show()
    out=im.point(lambda i:i*1.2)
    out.show()
    source=im.split()
    print(source)
    R,G,B=0,1,2
    mask=source[G].point(lambda i:i*0.7)
    print(mask)
    out=source[R].point(lambda i:i<200 and 255)
    out.show()
    print(out)
    source[G].paste(out,None,mask)
    source[G].show()
    print(source[G])
    print(source)
    im=Image.merge(im.mode,source)
    im.show()
    enh=ImageEnhance.Contrast(im)
    enh.enhance(1.3).show()
'''
   
   
    #im.draft("L",(100,100))
    #im.show()
