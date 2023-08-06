from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import base64
from google.cloud import bigquery, storage
from google.oauth2 import service_account
import tensorflow as tf
from tensorflow import keras
from fastapi import FastAPI, UploadFile, File, Request,Form
from fastapi.templating import Jinja2Templates
from typing import Annotated
from PIL import Image
import io
import numpy as np
import os
app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    with open('templates/index.html','r') as file:
        content = file.read()
    return HTMLResponse(content=content)

key_path = "cloudkarya-internship-a3650f4f3b90.json"
bigquery_client = bigquery.Client.from_service_account_json(key_path)
storage_client = storage.Client.from_service_account_json(key_path)  

bucket_name="hand_sketch"
bucket= storage_client .get_bucket(bucket_name)

img="https://storage.cloud.google.com/hand-sketches/n07739125_5365-1.png"
@app.post("/upload")
async def upload_image(request: Request,image:Annotated[UploadFile, File(...)]):
    
    data = await image.read()
    input_image = Image.open(io.BytesIO(data))
    input_image = input_image.resize((256, 256))
    input_array = np.array(input_image) - 127.5 / 127.5
    input_array = np.expand_dims(input_array, axis=0)

    model_path = "model_0002000.h5"
    blob = bucket.blob(model_path)
    blob.download_to_filename(model_path)

    model = tf.keras.models.load_model(model_path)
    predictions = model.predict(input_array)

    os.remove(model_path)
    predictions = np.reshape(predictions, (256, 256, 3))
    predictions = (predictions) / 2.0
    integer_rgb_array = np.uint8((predictions + 0.5) * 255)
    # predicted_image = Image.fromarray(integer_rgb_array, mode = "RGB")
    predicted_image = Image.fromarray(integer_rgb_array)
    byte_data=io.BytesIO()
    predicted_image.save(byte_data,format= 'PNG')
    byte_data=byte_data.getvalue()
    encoded_img=base64.b64encode(byte_data).decode('utf-8')
    # print(predictions)
    return templates.TemplateResponse("index.html", {"request": request, "img":encoded_img})

