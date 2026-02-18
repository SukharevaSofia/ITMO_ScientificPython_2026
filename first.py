import sys
import base64

def to_text():
    for file in ['1_1.jpg', '1_2.jpg']:
        with open(file, 'rb') as f:
            data = base64.b64encode(f.read()).decode()
        with open(file.replace('.jpg', '.txt'), 'w') as f:
            f.write(data)

def to_pic():
    for file in ['1_1.txt', '1_2.txt']:
        with open(file, 'r') as f:
            data = base64.b64decode(f.read())
        with open(file.replace('.txt', '.jpg'), 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'to_text':
            to_text()
        elif sys.argv[1] == 'to_pic':
            to_pic()
