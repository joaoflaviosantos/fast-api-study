import json
import pathlib
from typing import List, Union

from fastapi import FastAPI, Response

from models import Track

app = FastAPI()

data = []

''' Events: startup - shutdown '''

@app.on_event("startup")
async def startup_event():
    datapath = pathlib.Path('./data/tracks.json')
    with open(datapath, 'r') as f:
        tracks = json.load(f)
        for track in tracks:
            data.append(Track(**track).dict())
    print('\n---------------------------------------------------------------------')    
    print('------------------ STARTING FAST API (TRACKS CRUD) ------------------')
    print('---------------------------------------------------------------------\n') 


@app.on_event("shutdown")
def shutdown_event():
    print('\n---------------------------------------------------------------------') 
    print('------------------ STOPING FAST API (TRACKS CRUD) -------------------')
    print('---------------------------------------------------------------------\n') 

''' Endpoints '''

@app.get('/tracks/', response_model=List[Track])
async def get_tracks():
    return data

@app.get('/tracks/{track_id}', response_model=Union[Track, str])
async def get_track(track_id: int, response: Response):

    # find the track with the given ID, or None if it does not exist
    track = next((track for track in data if track["id"] == track_id), None)

    # return str or Track on response_model
    if track is None:
        # if a track with given ID doesn't exist, set 404 code and return string
        response.status_code = 404
        return "Track not found"
    return track

@app.post('/tracks/', response_model=Track, status_code=201)
async def create_track(track: Track):
    track_dict = track.dict()

     # assign track next sequential ID
    track_dict['id'] = max(data, key=lambda x: x['id']).get('id') + 1

    # append the track to our data and return 201 response with created resource
    data.append(track_dict)
    return track_dict

@app.put('/tracks/{track_id}', response_model=Union[Track, str])
async def change_track(track_id: int, updated_track: Track, response: Response):
    
    # find the track with the given ID, or None if it does not exist
    track = next((track for track in data if track["id"] == track_id), None)

    # return str or Track on response_model
    if track is None:
        # if a track with given ID doesn't exist, set 404 code and return string
        response.status_code = 404
        return "Track not found"
    
    for key, val in updated_track.dict().items():
        if key != 'id': # don't reset the ID
            track[key] = val

    return track

@app.delete('/tracks/{track_id}')
async def change_track(track_id: int, response: Response):
    
# get the index of the track to delete
    delete_index = next((idx for idx, track in enumerate(data) if track['id'] == track_id), None)

    # return str or Track on response_model
    if delete_index is None:
        # if a track with given ID doesn't exist, set 404 code and return string
        response.status_code = 404
        return "Track not found"

    del data[delete_index]
    response.status_code = 202
    return "Track deleted"
