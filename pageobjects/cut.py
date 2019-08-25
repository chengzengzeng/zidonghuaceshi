#coding=utf-8
from PIL import Image
from collections import defaultdict
import pytesseract

def get_threshold(image):
    pixel_dict=defaultdict(int)
    rows,cols=image.size
    for i in range(rows):
        for j in range(cols):
            pixel = image.getpixel((i,j))
            pixel_dict[pixel]+=1
    count_max =max(pixel_dict.values())
    pixel_dict_reverse={v:k for k,v in pixel_dict.items()}
    threshold=pixel_dict_reverse[count_max]
    print('threshold',threshold)
    return  threshold


def cut_noise(image):
    rows,cols =image.size
    change_pos =[ ]
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            pixel_set=[]
            for m in range(i-1,i+2):
                for n in range(j-1,j+2):
                    if image.getpixel((m,n))!=1:
                        pixel_set.append(image.getpixel((m,n)))
            if len(pixel_set)<=4:
                change_pos.append((i,j))
    for pos in change_pos:
        image.putpixel(pos,1)
    return image


def get_bin_table(threshold):
    table=[]
    for i in range(256):
        rate=0.2
        if threshold *(1-rate) <=i<= threshold*(1+rate):
            table.append(1)
        else:
            table.append(0)
    return table


def OCR_lmj(img_path):
    image=Image.open(img_path)
    region = (662,322, 740, 356)
    # 裁切图片
    image = image.crop(region)
    imgry=image.convert('L')
    table= get_bin_table(threshold=210)
    out=imgry.point(table,'1')
    out=cut_noise(out)
    text=pytesseract.image_to_string(out)
    exclude_char_list =' .,:\\|\'\"?![]（）()!@#$%^&*_+{};<>/¥'
    text = ''.join([x for x in text if x not in exclude_char_list])
    return text.replace('¥','y')