# https://medium.com/@ramjoshi.blogs/building-rest-apis-with-python-and-fastapi-f0e9ae19905c

# https://stackoverflow.com/questions/2337281/how-do-i-do-an-initial-push-to-a-remote-repository-with-git

from fastapi import FastAPI, File, UploadFile, responses
from pydantic import BaseModel
import matplotlib as plt #-> TODO install it
import io
import matplotlib.pyplot as plt
import os

class Item(BaseModel):
    name: str
    price: float

class PlotData(BaseModel):
    x_data: list
    y_data: list

class PlotDiagram(BaseModel):
    x_data: dict
    y_data: dict
    args: any

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
    # plot = PlotData(x_data=[0, 1, 2, 3, 4, 5], y_data=[0, 1, 2, 3, 4, 5])
    plt.plot(plot.x_data, plot.y_data)
    plt.xlabel("X-label")
    plt.ylabel("Y-label")
    dir_path = os.path.dirname(__file__)
    subdir_name = os.path.join(dir_path, r"2Dplot")
    
    if not os.path.exists(subdir_name):
        os.makedirs(subdir_name)
    img_path = os.path.join(subdir_name, r"plot.png")
    
    if os.path.exists(img_path):
        os.remove(img_path)
    plt.savefig(img_path, format = 'png')
    return responses.FileResponse(img_path, media_type="image/png")

@app.get("/plot_snp/")
async def get_created_plot():
    dir_path = os.path.dirname(__file__)
    img_path = os.path.join(dir_path, r"2Dplot\\plot.png")
    return responses.FileResponse(img_path, media_type="image/png")

#to start the app in development mode: fastapi dev .main_server.py / also fastapi dev
#to start the app in production mode: uvicorn main_server:app --reload / also fastapi run
#D:\repos\fast_api_devs\fastapi_REST_API\.venv\Scripts> .\activate