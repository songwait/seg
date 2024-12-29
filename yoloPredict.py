from ultralytics import YOLO
def loadModel(modelPath):
    model = YOLO(modelPath)
    return model
if __name__ == "__main__":
    model = loadModel("runs/segment/train4/weights/best.pt")
    results = model("data/tennis/frame/special.0.png")
    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.show()  # display to screen
        result.save(filename="result.jpg")  # save to disk
    # Export the model to ONNX format
    success = model.export()