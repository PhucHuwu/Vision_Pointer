import cv2
import mediapipe
import pyautogui
from PIL import Image

face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks = True)
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
ratio = 0.15
right_eye_up_x_tmp, right_eye_up_y_tmp = 0, 0

while True:
    _, image = cap.read()
    image = cv2.flip(image, 1)
    image_h, image_w, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    key = cv2.waitKey(1)

    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks
    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark
        #441, 261
        right_eye_up_x = int(one_face_landmark_points[54].x * image_w)
        right_eye_up_y = int(one_face_landmark_points[54].y * image_h)

        wratio, hratio = int(screen_w * ratio), int(screen_h * ratio)
        cv2.rectangle(image, (right_eye_up_x_tmp, right_eye_up_y_tmp), (right_eye_up_x_tmp + wratio, right_eye_up_y_tmp + hratio), (255, 0, 0), 2)

        right_eye = [one_face_landmark_points[374], one_face_landmark_points[386]]

        mouth = [one_face_landmark_points[13], one_face_landmark_points[14]]
        for landmark_point in mouth:
            x = int(landmark_point.x * image_w)
            y = int(landmark_point.y * image_h)
            cv2.circle(image, (x, y), 3, (255, 0, 0))

        for id, landmark_point in enumerate(one_face_landmark_points[473:478]):
            x = int(landmark_point.x * image_w)
            y = int(landmark_point.y * image_h)
            cv2.circle(image, (x, y), 4, (0, 255, 0))

            if id == 1:
                if (right_eye[0].y - right_eye[1].y < 0.01) and not (mouth[1].y - mouth[0].y < 0.01):
                    right_eye_up_x_tmp = right_eye_up_x
                    right_eye_up_y_tmp = right_eye_up_y

                if x > right_eye_up_x_tmp and x < right_eye_up_x_tmp + wratio:
                    if y > right_eye_up_y_tmp and y < right_eye_up_y_tmp + hratio:
                        mouse_x = (x - right_eye_up_x_tmp) / ratio
                        mouse_y = (y - right_eye_up_y_tmp) / ratio
                        pyautogui.moveTo(mouse_x, mouse_y)
        
        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]
        for landmark_point in left_eye:
            x = int(landmark_point.x * image_w)
            y = int(landmark_point.y * image_h)
            cv2.circle(image, (x, y), 3, (255, 0, 0))

        for landmark_point in right_eye:
            x = int(landmark_point.x * image_w)
            y = int(landmark_point.y * image_h)
            cv2.circle(image, (x, y), 3, (255, 0, 0))

        if (left_eye[0].y - left_eye[1].y < 0.01):
            #pass
            pyautogui.click()
            #pyautogui.sleep(2)

    cv2.imshow("Eye control pointer", image)
    if key == 27:
        break

cv2.destroyAllWindows()