import imageio
import os

from PIL import Image

images = []
path="Path\To\Folder\with\Folders\with\images"
folders = os.listdir(path)

def gen_frame(path):
    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)

    # The transparency index is 255
    im.info['transparency'] = 255

    return im



for folder in folders:
    baseImage = 0
    appendix = []
    for filename in os.listdir(path+"\\"+folder):
        if baseImage==0:
            baseImage = gen_frame(path+"\\"+folder+"\\"+filename)
        else:
            appendix.append(gen_frame(path+"\\"+folder+"\\"+filename))

    baseImage.save("Path\To\Folder\with\Folders\with\images\\"+folder+".gif", save_all=True, append_images=appendix, loop=0, duration=30,optimize=False,disposal=2)
