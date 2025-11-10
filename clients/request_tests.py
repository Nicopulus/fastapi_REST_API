import requests
import os
import sys

def get_data(url, item_id):
    get_url = url + str(item_id)
    response = requests.get(get_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with code: {response.status_code}")
        return None

def post_create_item(url, data=None):
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
    def __init__(self, server_address="localhost", port="8000"):
        self._platform = sys.platform
        if self._platform.startswith("win32") or self._platform.startswith("win64"):
            server_address="pi.hole"
        self._base_url = f'http://{server_address}:{port}/'
    
    def get_root(self):
        get_url = self._base_url
        response = requests.get(get_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with code: {response.status_code}")
            return None

    def get_read_item(self, item_id):
        get_url = self._base_url + "items/" + str(item_id['id_number'])
        response = requests.get(get_url, json=item_id)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with code: {response.status_code}")
            return None
    
    def post_create_item(self, data=None):
        if data is None:
            raise ValueError("Data cannot be None.")
        response = requests.post(self._base_url  + "items/", json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with code: {response.status_code}")
            return None

    def get_temperature(self, sensor_id):
        get_url = self._base_url + "temperature/" + sensor_id
        response = requests.get(get_url)
        return self._checking_response(response)
        
    def _checking_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with code: {response.status_code}")
            return None

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

####################################################
<<<<<<< HEAD
    tester = RequestTests()
=======
    tester = RequestTests("http://localhost:8000/")#
>>>>>>> 12d2763 (merging from windows)
    print(tester.get_root())
    test_data_get = {'id_number': 100}
    print(tester.get_read_item(test_data_get))
    test_data_post = {'name': 'nico', 'id_number': 100}
    print(tester.post_create_item(data=test_data_post))
    test_sensor_id = {'sensor_id': 'temp_simulated'}
    print(tester.get_temperature(test_sensor_id['sensor_id']))
