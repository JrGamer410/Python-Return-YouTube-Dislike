import requests
import json

def ryd_getvideoinfo(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def ryd_getvideolikes(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    likes = data['likes']
    return likes

def ryd_getvideodislikes(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    dislikes = data['dislikes']
    return dislikes

def ryd_getvideorating(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    rating = data['rating']
    return rating

def ryd_getvideoviews(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    views = data['viewCount']
    return views

def ryd_isvideodeleted(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    deleted = data['deleted']
    return deleted

def ryd_getvideodatecreated(video_id):
    url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(url)
    data = json.loads(response.text)
    dataCreated = data['dateCreated']
    return dataCreated