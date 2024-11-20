import os
import time
import random

import lib
import ad
import camera

import traceback


if __name__ == '__main__':
    
    current_path = os.getcwd()
    sub_path = os.path.join(current_path, 'ad')
    
    while True:
        try:
            data = camera.camera()
            
            if type(data) is list:
                data = random.choice(data)
            
            age = lib.age(lib.parse_age(data)).strip()
            gender = lib.parse_gender(data).strip()
            
            temp_path = ad.search(sub_path, age)
            
            if temp_path:
                ad_path = ad.search(temp_path, gender)
                
            if ad_path:
                ad.play_ad(ad_path)
                time.sleep(3)
                continue
            
            raise
            
        except Exception as e:
            trace_back = traceback.format_exc()
            msg = str(e) + "\n" + str(trace_back)
            
            print(msg)
            with open('error.txt', 'a') as log:
                log.write(msg + '\n\n')
                
            continue