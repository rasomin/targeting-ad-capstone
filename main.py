import os
import random

import lib
import ad
import camera

import traceback


if __name__ == '__main__':
    # while True:
    try:
        current_path = os.getcwd()
        sub_path = os.path.join(current_path, 'ad')
        
        data = camera.camera()
        
        if type(data) is list:
            data = random.choice(data)
        
        age = lib.age(lib.parse_age(data)).strip()
        gender = lib.parse_gender(data).strip()
        
        temp_path = ad.search(sub_path, age)
        ad_path = ad.search(temp_path, gender)
        
        ad.play_ad(ad_path)
        
    except Exception as e:
        trace_back = traceback.format_exc()
        msg = str(e) + "\n" + str(trace_back)
        
        print(msg)
        with open('error.txt', 'a') as log:
            log.write(msg + '\n\n')
            
        # continue