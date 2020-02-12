
from flask import Flask, jsonify, request 
import cv2
from pyzbar import pyzbar
import image_slicer
  
# creating a Flask app 
app = Flask(__name__) 
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    
    name = 'ttt.jpeg'
    nm = name.split(".")
    image = cv2.imread(name)

    image_slicer.slice(name, 4)
    slice_1 = nm[0] +'_01_01.png'
    slice_2 = nm[0] +'_01_02.png'
    slice_3 = nm[0] +'_02_01.png'
    slice_4 = nm[0] +'_02_02.png'
    lst = []

    i1 = cv2.imread(slice_1)

    from pyzbar.pyzbar import decode

    barcodes = pyzbar.decode(i1)
    obj = barcodes
    for barcode in obj:
        print(barcode.data)
        b1 = barcode.data
        lst.append(b1)
    
    i2 = cv2.imread(slice_2)

    barcodes = pyzbar.decode(i2)
    obj = barcodes
    for barcode in obj:
        print(barcode.data)
        b2 = barcode.data
        lst.append(b2)
    
    i3 = cv2.imread(slice_3)

    barcodes = pyzbar.decode(i3)
    obj = barcodes
    for barcode in obj:
        print(barcode.data)
        b3 = barcode.data
        lst.append(b3)
    
    i4 = cv2.imread(slice_4)

    barcodes = pyzbar.decode(i4)
    obj = barcodes
    for barcode in obj:
        print(barcode.data)
        b4 = barcode.data
        lst.append(b4)

    if(request.method == 'GET'): 
        list = []
        for data in lst:
            list.append(data.decode("utf-8"))
        return jsonify({'barcode': list}) 

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 
    
    
    

