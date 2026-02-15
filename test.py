from ultralytics import YOLO

model = YOLO('best.pt') 

results = model.predict(sourc='0', show=True, conf=0.4)