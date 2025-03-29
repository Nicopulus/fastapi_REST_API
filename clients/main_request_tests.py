import requests
import os

def get_data(url, item_id):
    get_url = url + str(item_id)
    response = requests.get(get_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with code: {response.status_code}")
        return None

def post_data(url, data=None):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with code: {response.status_code}")
        return None
    
def post_2d_plot(url, plotdata=None):
    response = requests.post(url, json=plotdata)
    if response.status_code == 200:
        with open(os.path.join(os.path.dirname(__file__), "post_plot_received.png"), "wb") as file:
            file.write(response.content)
        file.close()
        print("Plot received successfully")
    else:
        print(f"Request failed with code: {response.status_code}")
        return None

def get_2d_plot(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(os.path.dirname(__file__), "get_plot_received.png"), "wb") as file:
            file.write(response.content)
        file.close()
        print("Plot received successfully")
    else:
        print(f"Request failed with code: {response.status_code}")
        return None

class RequestTests:
    def __init__(self, base_url):
        self._base_url = base_url
    
    def get_data(self, item_id, url_str="/items/"):
        get_url = self._base_url + url_str +str(item_id)
        response = requests.get(get_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with code: {response.status_code}")
            return None
    
    def post_data(self, url_str="/items/", data=None):
        if data is None:
            raise ValueError("Data cannot be None.")
        response = requests.post(self._base_url + url_str, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with code: {response.status_code}")
            return None
        
    def post_2d_plot(self, url_str="plot_snp/", plotdata=None):
        response = requests.post(self._base_url + url_str, json=plotdata)
        if response.status_code == 200:
            dir_path = os.path.dirname(__file__)
            file_path = os.path.join(dir_path, "post_plot_received.png")
            if os.path.exists(file_path):
                os.remove(file_path)

            with open(file_path, "wb") as file:
                file.write(response.content)
            file.close()
            info_out = "Plot information received successfully with code: "
        else:
            info_out = "Request failed with code: "
        return f'{info_out}{response.status_code}'

    def get_2d_plot(self, url="plot_snp/"):
        get_url = self._base_url + url	
        response = requests.get(get_url)
        if response.status_code == 200:
            dir_path = os.path.dirname(__file__)
            file_path = os.path.join(dir_path, "get_plot_received.png")
            if os.path.exists(file_path):
                os.remove(file_path)

            with open(file_path, "wb") as file:
                file.write(response.content)
            file.close()
            info_out = "Plot received successfully with code: "
        else:
            info_out = f"Request failed with code: "
        return f'{info_out}{response.status_code}'
    
if __name__ == "__main__":
    ###POST/GET_TESTS####
    # base_url = "http://127.0.0.1:8000/"
    # general_url = base_url+"/items/"
    # data = {'name' : 'nico', 'price':100}
    # print(post_data(general_url, data))
    # print(get_data(general_url, 10))
    ###POST/GET_PLOT_FUNCTIION_TESTS####
    # general_url = base_url+"/plot_snp/"
    # plotdata = {'x_data' : [0, 1, 2, 3, 4, 5], 'y_data' : [0, 1, 2, 3, 4, 5]}
    # post_2d_plot(general_url, plotdata=plotdata)
    # get_2d_plot(general_url)


#######POST/GET TEST CLASSES#############################################
    tester = RequestTests("http://localhost:8000/")
    # print(tester.get_data(10))

    # data = {'name' : 'nico', 'price':100}
    # print(tester.post_data(data=data))
    
    # # plotdata = {'x_data' : [0, 1, 2, 3, 4, 5], 'y_data' : [0, 1, 2, 3, 4, 5], 'args': {'color': 'blue', 'label': 'Test'}}
    plotdata = {'x_data' : [0, 1, 2, 3, 4, 5], 'y_data' : [0, 1, 2, 3, 4, 5]}
    print(tester.post_2d_plot(plotdata=plotdata))

    print(tester.get_2d_plot())