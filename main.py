from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


app = FastAPI()

prod_model = tf.keras.models.load_model("/models/1")
beta_model = tf.keras.models.load_model("/models/2")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray :
    image = np.array(Image.open(BytesIO(data)))
    return image

# Upload file is the datatupe in this an image
@app.post("/predict")
async def predict(
    file: UploadFile = File(...) # File as an input
):
  image = read_file_as_image(await file.read()) # Await is sed when lot of request is send
  img_batch = np.expand_dims(image, 0) # It just adds one more dimesion eg: 1d to 2d
  predictions = MODEL.predict(img_batch)
  predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
  confidence = np.max(predictions[0])
  return {
      'class': predicted_class,
      'confidence': float(confidence)
  }

if __name__ == "__main__" :
    uvicorn.run(app, host='localhost', port=8080)  # You can run it by http://localhost:8000/ping

