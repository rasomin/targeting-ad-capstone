import cv2
import random
import os

def search(path, word):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if word in dir_name:
                return os.path.join(root, dir_name)
    return False

def play_ad(path):
    ad_files = [f for f in os.listdir(path)]
    if ad_files:
        random_choice = random.choice(ad_files)
        if random_choice.endswith(".mp4"):
            play_vid(path, random_choice)
        else:
            play_photo(path, random_choice)
    else:
        print("nofile")
    return
        
def play_vid(path, name):
    cap = cv2.VideoCapture(os.path.join(path, name))
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        cv2.imshow("Video", frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return
    
def play_photo(path, name):
    img = cv2.imread(os.path.join(path, name))
    
    cv2.imshow("Image", img)
    
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    return
        
