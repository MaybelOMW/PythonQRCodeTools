import qrcode
import json

def QRGenerator(content, index):
    item = content[index-1]
    item = json.loads(item.strip())

    filename = 'QRcode_' + str(index) + '.png'
    data = item
    data_str = json.dumps(data)
    test = qrcode.make(data_str)
    test.save(filename)
    print("\nQR Code Generated: ", filename)