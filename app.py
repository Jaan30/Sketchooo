from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from google.cloud import bigquery, storage
from google.oauth2 import service_account
import tensorflow
from fastapi import FastAPI, UploadFile, File, Request,Form
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name="static")

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
    
    #preprocess
    image = load_img(filename, target_size=256)
    image = img_to_array(image)
    image = (image - 127.5) / 127.5
    image = expand_dims(pixels, 0)


    models= "model_0002000.h5"
    blob = bucket.blob(models)
    blob.download_to_filename(models)

    model = tf.keras.models.load_model(models)
    predictions = model.predict(image)

    # print(predictions)
    return templates.TemplateResponse("index.html", {"request": request, "img":predictions})