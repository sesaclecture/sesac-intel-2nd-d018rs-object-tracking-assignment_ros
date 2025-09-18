import torch
import cv2

# Model​
model = torch.hub.load("ultralytics/yolov5", "yolov5m")

# Video capture
cap = cv2.VideoCapture(0)

# TODO: Loop for camera frames


# Read frame (BGR to RGB)
ret, frame = cap.read()
# TODO: break the loop on error

# 추론 실행 (BGR -> RGB)
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
results = model(rgb_frame)

# TODO: Boudning box 그리기
for i, obj in enumerate(results.xyxy[0]):
    # TODO: 인식결과를 표시하기 위한 좌표를 얻음

    # TODO: 인식된 정확도(confidence)와 클래스를 label로 구성

    # TODO: OpenCV를 이용해서 해당 좌표에 사각형과 text를 출력
    obj_info = list(map(int, obj))
    print(f"Object {i}: {model.names[obj_info[5]]}")

# TODO: 화면 표시

# TODO: 종료를 위한 key 처리

cap.release()
cv2.destroyAllWindows()
