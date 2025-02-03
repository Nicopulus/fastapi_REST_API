# https://medium.com/@ramjoshi.blogs/building-rest-apis-with-python-and-fastapi-f0e9ae19905c
from fastapi import FastAPI, File, UploadFile, responses
from pydantic import BaseModel
import matplotlib as plt #-> TODO install it
import io
import matplotlib.pyplot as plt

class Item(BaseModel):
    name: str
    price: float

class PlotData(BaseModel):
    x_data: list
    y_data: list

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if not item_id:
        item_id = 0
    return {'item_id': item_id}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/plot_snp/")
async def create_plot(plot: PlotData):
    plt.plot(plot.x_data, plot.y_data)
    plt.xlabel("X-label")
    plt.ylabel("Y-label")
    img_path = r"2Dplot\plot.png"
    plt.savefig(img_path, format = 'png')
    return responses.FileResponse(img_path, media_type="image/png")
    # img = io.BytesIO()
    # plt.savefig(img, format = 'png')
    # img.seek(0)
    # return img

@app.get("/plot_snp/")
async def get_created_plot():
    img_path = r"2Dplot\plot.png"
    return responses.FileResponse(img_path, media_type="image/png")

#to start the app in development mode: fastapi dev .main.py / also fastapi dev
#to start the app in production mode: uvicorn main:app --reload / also fastapi run
#D:\repos\fast_api_devs\fastapi_REST_API\.venv\Scripts> .\activate