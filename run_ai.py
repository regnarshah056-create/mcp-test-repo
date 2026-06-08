from ultralytics import YOLO
import cv2

# 1. LOAD YOUR CUSTOM MODEL
# Make sure 'pothole_model.pt' is in the same folder!
model = YOLO("pothole_model.pt")

# 2. SOURCE SETUP
# Option A: Run on an Image
source_path = "images-2.jpeg" 

# Option B: Run on a Video (Uncomment to use)
# source_path = "pothole_video.mp4"

# Option C: Run on Webcam (Uncomment to use)
# source_path = 0  

# 3. RUN INFERENCE
results = model.predict(source=source_path, show=True, conf=0.25, save=True)

# The 'show=True' part opens a window automatically.
# The 'save=True' part saves the result in a folder called 'runs/detect/predict'.

print("Processing complete. Check the popup window or the 'runs' folder.")

# Keep window open until a key is pressed (Only needed for images)
cv2.waitKey(0)
cv2.destroyAllWindows()