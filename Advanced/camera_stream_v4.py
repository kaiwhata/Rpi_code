import time
import picamera
import picamera.array
import cv2

test_line = 320

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (640,480)
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            '''
            print(stream.array.shape)
            print(stream.array.shape[:][:][0])
            '''
            
            
            print(len(stream.array[test_line][:]))
            
            img = stream.array
            '''
            cv2.line(img, (0, test_line), (640, test_line), (0, 0, 0), 2)
            '''
            for i in range(len(img[test_line][:])-1):
                cv2.line(img, (i, img[test_line][i][0] ), (i+1, img[test_line][i+1][0]), (255, 0, 0), 2)
                cv2.line(img, (i, img[test_line][i][1] ), (i+1, img[test_line][i+1][1]), (0, 255, 0), 2)
                cv2.line(img, (i, img[test_line][i][2] ), (i+1, img[test_line][i+1][2]), (0, 0, 255), 2)
            
            cv2.imshow('Image',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()
        cv2.destroyAllWindows()
                




    
