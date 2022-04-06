from tracemalloc import start
import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshotTaken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = "sl.BFMKWWXIKY3eTtXTPwFPdKaTKkaEW5Q96YVWJcQatVzrNwQJJIRIsXpY4DkUzqo8ISMXsdTqILScrTIyIvlFDlK4NPjJmzuPA6zmwxaiOH01VRH7HxL529yfJn2UaqmAc4KlXYdz8vxI"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 500000):
            name = take_snapshot()
            upload_file(name)

main()
