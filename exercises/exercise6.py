from PIL import Image
import os.path
import glob  #文件路径查找

def change_size(file,dir,width=700,height=720):
    image=Image.open(file)
    #new_image=img.resize((width,height),Image.BILINEAR)
    image.thumbnail((width,height))
    image.save(os.path.join(dir,os.path.basename(file)))



for file in glob.glob('/users/yufangxian/Documents/exercise/picture/*.jpg'):
    change_size(file,'/users/yufangxian/Documents/exercise/')
