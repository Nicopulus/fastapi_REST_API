# https://medium.com/@ramjoshi.blogs/building-rest-apis-with-python-and-fastapi-f0e9ae19905c

# https://stackoverflow.com/questions/2337281/how-do-i-do-an-initial-push-to-a-remote-repository-with-git

from fastapi import FastAPI, File, UploadFile, responses
from pydantic import BaseModel
import matplotlib as plt #-> TODO install it
import io
import matplotlib.pyplot as plt
import os
import uvicorn

class ItemAsId(BaseModel):
    id_number: int


class Item(ItemAsId):
    name: str


class PlotData(BaseModel):
    x_data: list
    y_data: list


# app = FastAPI()

# @app.get("/items/{id_number}")
# async def read_item(id_number: int):
#     return id_number

# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item

# @app.get("/temperature/{sensor_id}")
# async def temperature(sensor_id: str = None):
#     if sensor_id is None:
#         temperature = -1.1
#     elif sensor_id == "temp_simulated":
#         temperature = 25.5  #     # Simulate fetching temperature data from a sensor
#     else:    
#         temperature = -2.2
#     return {"sensor_id": sensor_id, "temperature": temperature}

# @app.post("/plot_snp/")
# async def create_plot(plot: PlotData):
#     plt.plot(plot.x_data, plot.y_data)
#     plt.xlabel("X-label")
#     plt.ylabel("Y-label")
#     img_path = r"2Dplot\plot.png"
#     plt.savefig(img_path, format = 'png')
#     return responses.FileResponse(img_path, media_type="image/png")

# @app.get("/plot_snp/")
# async def get_created_plot():
#     img_path = r"2Dplot\plot.png"
#     return responses.FileResponse(img_path, media_type="image/png")

class ServerAndEndpoints():
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 8000
        self.app = FastAPI()
        self.endpoints = {
            "root": "/",
            "items": "/items/",
            "temperature": "/temperature/",
            "plot_snp": "/plot_snp/"
            }
        self.setup_routes()

    def setup_routes(self):
        """
        Define the routes for the FastAPI application.
        """
        @self.app.get(self.endpoints['root'])
        async def read_root():
            return {"message": "Welcome to the FastAPI server!"}

        @self.app.get(self.endpoints['items']+'{itemasid}')
        async def read_item(itemasid):
            return itemasid

        @self.app.post(self.endpoints['items'])
        async def create_item(item: Item) -> Item:
            return item

        @self.app.get(self.endpoints['temperature']+'{sensor_id}')
        async def get_temperature(sensor_id: str = None):
            if sensor_id is None:
                temperature = -1.1
            elif sensor_id == "temp_simulated":
                temperature = 25.5
            else:    
                temperature = -2.2
            return {"sensor_id": sensor_id, "temperature": temperature}

        # @self.app.post(self.endpoints['plot_snp'])
        # async def create_plot(plot: PlotData):
        #     plt.plot(plot.x_data, plot.y_data)
        #     plt.xlabel("X-label")
        #     plt.ylabel("Y-label")
        #     img_path = r"2Dplot\plot.png"
        #     plt.savefig(img_path, format = 'png')
        #     return responses.FileResponse(img_path, media_type="image/png")

        # @self.app.get(self.endpoints['plot_snp'])
        # async def get_created_plot():
        #     img_path = r"2Dplot\plot.png"
        #     return responses.FileResponse(img_path, media_type="image/png")


#to start the app in development mode: fastapi dev .main.py / also fastapi dev
#to start the app in production mode: uvicorn main:app --reload / also fastapi run

#to run in win:D:\repos\fast_api_devs\fastapi_REST_API\.venv\Scripts> .\activate
#to run in linux: .venv/bin/python -m fastapi run

if __name__ == "__main__":
    server = ServerAndEndpoints()
    uvicorn.run(app=server.app, host=server.host, port=server.port)
