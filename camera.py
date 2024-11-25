def camera(picam2):
    import cv2
    from picamera2 import Picamera2
    
    # 변수 선언
    x = y = w = h = 0

    # 얼굴 탐지 및 성별, 나이 인식을 위한 설정 파일 및 모델 로드
    cascade_filename = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
    cascade = cv2.CascadeClassifier(cascade_filename)

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

    age_net = cv2.dnn.readNetFromCaffe(
        'model/deploy_age.prototxt',
        'model/age_net.caffemodel'
    )

    gender_net = cv2.dnn.readNetFromCaffe(
        'model/deploy_gender.prototxt',
        'model/gender_net.caffemodel'
    )

    age_list = ['(0 ~ 2)', '(4 ~ 6)', '(8 ~ 12)', '(15 ~ 20)',
                '(25 ~ 32)', '(38 ~ 43)', '(48 ~ 53)', '(60 ~ 100)']
    gender_list = ['Male', 'Female']

    # 성별과 나이를 저장할 리스트 초기화
    gender_age_data = []
    ga_data = dict()

    while True:
        # 이미지 캡처
        img = picam2.capture_array()

        # RGB 이미지를 BGR로 변환
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        # 상하 반전
        img = cv2.flip(img, 0)
        
        # 4채널 이미지를 3채널로 변환 (필요한 경우)
        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 얼굴 감지
        results = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20)
        )

        # 감지된 얼굴에 나이와 성별 인식
        for box in results:
            x, y, w, h = box
            face = img[y:y+h, x:x+w].copy()
            blob = cv2.dnn.blobFromImage(face, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

            # 성별 예측
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = gender_preds.argmax()
            gender_text = gender_list[gender]

            # 나이 예측
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = age_preds.argmax()
            age_text = age_list[age]

            # 인식 정보 표시
            info = f"{gender_text} {age_text}"
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)
            cv2.putText(img, info, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            # 성별과 나이를 콘솔에 출력
            print(f"Detected: {gender_text}, Age: {age_text}")
            print(f"Width: {w}, Height: {h}")

            # 성별과 나이를 리스트에 저장
            ga_data = {
                'gender' : gender_text,
                'age' : age_text
            }
            gender_age_data.append(ga_data)

        # 결과 이미지 표시
        cv2.imshow('Age and Gender Recognition', img)

        # 'q' 키를 누르면 종료하거나, 얼굴이 가까이 인식되면 종료
        if cv2.waitKey(1) == ord('q') or (w >= 280 and h >= 280) :
            break

    cv2.destroyAllWindows()
    
    return gender_age_data

