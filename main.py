import cv2
import socket
import mediapipe as md
md_drawing=md.solutions.drawing_utils
md_drawing_styles=md.solutions.drawing_styles
md_pose=md.solutions.pose
count=0
position=None
cap=cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
with md_pose.Pose(
   min_detection_confidence=0.7,
   min_tracking_confidence=0.7)as pose:

   while cap.isOpened():

       success,image = cap.read()
       if not success:
           print("empty camera")
           break
       image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
       result=pose.process(image)
       push=[]
       if result.pose_landmarks:

           md_drawing.draw_landmarks(
               image,result.pose_landmarks,md_pose.POSE_CONNECTIONS)
           for id,im in enumerate(result.pose_landmarks.landmark):
               h, w,_ = image.shape
               X, Y = int(im.x*w),int(im.y*h)
               push.append([id, X, Y])

           if len(push)!=0:

              if (push[12][2] and push[11][2] >= push[14][2] and push[13][2]):
                position = "down"
              if (push[12][2] and push[11][2] <= push[14][2] and push[13][2]) and position == "down":
                position = "up"
                count+=1
                print(count)
                sock.sendto(str.encode(str(count)), serverAddressPort)

       cv2.imshow("Push-up counter", cv2.flip(image, 1))
       key = cv2.waitKey(1)
       if key == ord('q'):
            break
   cap.release()