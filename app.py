from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from google.cloud import bigquery, storage
from google.oauth2 import service_account

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    with open('templates/index.html','r') as file:
        content = file.read()
    return HTMLResponse(content=content)

key_path = "cloudkarya-internship-c0091c2ca6dc.json"
bigquery_client = bigquery.Client.from_service_account_json(key_path)
storage_client = storage.Client.from_service_account_json(key_path)  

bucket_name="hand-sketches"
bucket= storage_client.get_bucket(bucket_name)

@app.post("/upload")
async def upload_image(image: UploadFile = Form(...)):
    ############preprocess
    models= "model_0002000.h5"
    blob = bucket.blob(models)
    blob.download_to_filename(models)

    model = tf.keras.models.load_model(models)
    predictions = model.predict(image)

    print(predictions)