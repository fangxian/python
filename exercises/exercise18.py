from PIL import Image
import glob,os
'''
size=200,300
for infile in glob.glob('/users/yufangxian/Documents/exercise/picture/*.jpg'):
    file,ext=os.path.splitext(infile)
    im=Image.open(infile)
    im1=im.resize(size)
    im1.save(file+'_thumbnail.jpg','JPEG')
    print(im.mode)
'''

im3=Image.open('/users/yufangxian/Documents/exercise/picture/1_thumbnail.jpg').convert('RGBA')
im4=Image.open('/users/yufangxian/Documents/exercise/picture/2_thumbnail.jpg').convert('RGBA')
im5=Image.open('/users/yufangxian/Documents/exercise/picture/3_thumbnail.jpg')
source=im5.split()
R,G,B=0,1,2
mask1=source[G].point(lambda i:i*0.7).convert('L')
print(mask1.mode)
#mask1.show()
mask2=source[B].point(lambda i:i*0.5).convert('L')
#mask2.show()
mask3=source[R].point(lambda i:i*0.6).convert('L')
im_merge=Image.merge('RGB',[mask1,mask2,mask3,])
im_merge.show()
#mask3=Image.alpha_composite(mask1,mask2)
#mask3.show()
#img=Image.composite(im3,im4,mask1)
#img.save('/users/yufangxian/Documents/exercise/picture/11.jpg','JPEG')

