import requests
import json

def ryd_getvideoinfo(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    return data

def ryd_getvideolikes(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    likes = data['likes']
    return likes

def ryd_getvideodislikes(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    dislikes = data['dislikes']
    return dislikes

def ryd_getvideorating(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    rating = data['rating']
    return rating

def ryd_getvideoviews(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    views = data['viewCount']
    return views

def ryd_isvideodeleted(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    deleted = data['deleted']
    return deleted

def ryd_getvideodatecreated(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response)
    dataCreated = data['dateCreated']
    return dataCreated