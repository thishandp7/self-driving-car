from flask import Flask
import socketio
import eventlet
from keras.models import load_model
import cv2
from PIL import Image
from io import BytesIO
import numpy as np
import base64

sio = socketio.Server()

app = Flask(__name__)

max_speed = 10.0

@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = preprocess_img(image)
    image = np.array([image])

    steering_angle = float(model.predict(image))
    throttle = float(1.0 - speed/max_speed)
    send_controls(steering_angle, throttle)

@sio.on('connect')
def connect(sid, environ):
    print('connected!')
    send_controls(0, 0)

def preprocess_img(img):
  cropped_img = img[60:135,: ,:]
  yuv_img = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2YUV)
  resized_img = cv2.resize(yuv_img, (200, 66))
  normalized_img = resized_img/255
  return normalized_img

def send_controls(steering_angle, throttle):
    data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    }
    sio.emit('steer', data)

if __name__ == '__main__':
    model = load_model('model.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
