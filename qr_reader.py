import cv2
import json

def QRReader(index):
    img = cv2.imread('QRcode_' + str(index) + '.png')
    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    if bbox is not None:
        print("Reading QR Code\n---------------")
        print("data:", data)
        res = json.loads(data)
        parent_key = str(*res)
        children_key = (*res[parent_key],)
        print(children_key)
        print("{0}: {1}".format(children_key[0], res[parent_key][children_key[0]]))
        print("{0}: {1}".format(children_key[1], res[parent_key][children_key[1]]))

        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=5)

    # display the result
    cv2.imshow('image', img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()