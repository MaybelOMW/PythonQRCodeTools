from qr_generator import QRGenerator
from qr_reader import QRReader
from qr_labeling import *

def main():
    txt_file = "persistent_data.txt"

    with open(txt_file) as f:
        content = f.readlines()
        data_len = len(content)
        content = [x.strip() for x in content]

    for index in range(1, data_len + 1):
        QRGenerator(content, index)

        img_obj, _ = ReadImage(index)
        AddWhiteSpace(index, img_obj)
        
        img_obj_wspace, cvread_img = ReadImage(index)
        LabelQRcode(index, img_obj_wspace, cvread_img)

        QRReader(index)
  
main()