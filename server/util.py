import json
import pickle
import numpy as np

__locations = None
__data_column = None
__model = None

def get_estimated_price(location,area,bhk):

    try:
        loc_index = __data_column.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_column))
    x[0] = area
    x[1] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

        return (__model.predict([x])[0])

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts....start")
    global __data_column
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_column = json.load(f)['data_column']
        __locations = __data_column[2:]

    global __model
    with open("./artifacts/delhi price prediction.pickle",'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('dwarka',1000,2))
