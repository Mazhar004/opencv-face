import cv2
import sys
import os

root = os.path.split(os.path.abspath(__file__))[0]


class Face():
    model_path = root+'/cascades'
    model = {'face': 'haarcascade_frontalface_default.xml',
             'eye': 'haarcascade_eye.xml'}

    def __init__(self, new_h=720):
        self.function = {'face': self.face, 'eye': self.eye}

    def load(self, filename):
        self.original_image = cv2.imread(filename)

    def resize(self, image, new_h=720):
        h, w, c = image.shape
        new_w = int((w/h)*new_h)
        dim = (new_w, new_h)
        new_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return new_image

    def face(self, image):
        face_cascade = cv2.CascadeClassifier(
            Face.model_path+'/'+Face.model['face'])
        faces = face_cascade.detectMultiScale(image, 1.3, 5)

        return faces

    def eye(self, image):
        eye_cascade = cv2.CascadeClassifier(
            Face.model_path+'/'+Face.model['eye'])
        eyes = eye_cascade.detectMultiScale(image)

        return eyes

    def show(self):
        while True:
            # Press 'q' for exit
            exit_key = ord('q')
            if cv2.waitKey(exit_key) & 255 == exit_key:
                cv2.destroyAllWindows()
                break
            cv2.imshow('Press "q" to Exit', self.re_image)

    def video(self, process_list=['face']):
        face_flag = 0
        eye_flag = 0

        if 'face' in process_list:
            face_flag = 1
        if 'eye' in process_list:
            eye_flag = 1

        vid = cv2.VideoCapture(0)
        while(True):
            ret, frame = vid.read()
            exit_key = ord('q')
            if cv2.waitKey(exit_key) & 255 == exit_key:
                cv2.destroyAllWindows()
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face(gray)

            for (x, y, w, h) in faces:
                if face_flag:
                    img = cv2.rectangle(frame, (x, y),
                                        (x+w, y+h), (255, 0, 0), 2)
                if eye_flag:
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    eyes = self.eye(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey),
                                      (ex+ew, ey+eh), (0, 255, 0), 2)

            cv2.imshow('Press "q" to Exit', frame)

        vid.release()
        cv2.destroyAllWindows()

    def process(self, process_list=['face'], status='image'):
        face_flag = 0
        eye_flag = 0

        if 'face' in process_list:
            face_flag = 1
        if 'eye' in process_list:
            eye_flag = 1

        self.re_image = self.resize(self.original_image)
        gray = cv2.cvtColor(self.re_image, cv2.COLOR_BGR2GRAY)
        faces = self.face(gray)

        for (x, y, w, h) in faces:
            if face_flag:
                img = cv2.rectangle(self.re_image, (x, y),
                                    (x+w, y+h), (255, 0, 127), 4)
            if eye_flag:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = self.re_image[y:y+h, x:x+w]
                eyes = self.eye(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey),
                                  (ex + ew, ey + eh), (127, 0, 255), 4)
