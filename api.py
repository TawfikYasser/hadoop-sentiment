# This file contains the logic of fetching data from YouTube API to get videos and videos comments.

# YouTube API Key: AIzaSyAz09qy3Nsg-tWxfCRfW9EJt6RGdHaxRAI

# https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyAz09qy3Nsg-tWxfCRfW9EJt6RGdHaxRAI&type=video&q=python&maxResults=50&videoType=any&pageToken=nextPageToken

import requests
import json

# print(f"STATUS CODE: {response.status_code}")
# print(f"CONTENT-TYPE: {response.headers['Content-Type']}")
# print(f"DATA: {response.json()}")
# print(response.json()['nextPageToken'])

import json
import sys

# BASE = "https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyAz09qy3Nsg-tWxfCRfW9EJt6RGdHaxRAI&type=video&q=algorithms&maxResults=50&videoType=any"
# videos = []
# for i in range(100):
#     response = requests.get(BASE)
#     json_str = json.dumps(response.json())
#     resp = json.loads(json_str)
#     npt = resp['nextPageToken']
#     BASE = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyAz09qy3Nsg-tWxfCRfW9EJt6RGdHaxRAI&type=video&q=algorithms&maxResults=50&videoType=any&pageToken={npt}"
#     with open(f"bucket{i+44}.json","w") as json_file:
#         json.dump(response.json(),json_file)
#     print(f"STATUS CODE: {response.status_code}")
    
# Get title, publish date, url

videos_titles = []
videos_pub_dates = []
videos_urls = []

for i in range(54):
    with open(f'bucket{i}.json') as json_file:
        data = json.load(json_file)
    for j in range(11):
        videos_titles.append(data['items'][j]['snippet']['title'])
        videos_pub_dates.append(data['items'][j]['snippet']['publishTime'][0:10])
        videos_urls.append(data['items'][j]['id']['videoId'])

print(len(videos_titles))

for i in range(len(videos_titles)):
    print(f"{i+1}) Title: {videos_titles[i]} - URL: {videos_urls[i]} - Publish Time: {videos_pub_dates[i]}")


# Comments code [OLD]

# for i in range(len(videos_titles)):
#     v_url = videos_urls[i]
#     URL = f"https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyAz09qy3Nsg-tWxfCRfW9EJt6RGdHaxRAI&textFormat=plainText&part=snippet&videoId={v_url}&maxResults=100"
#     response = requests.get(URL)
#     print(response.json())
#     with open(f"c_bucket{i}.json","w") as json_file:
#         json.dump(response.json(),json_file)
#         print(f"STATUS CODE: {response.status_code}")
#         print(i)

# for i in range(593):
#     with open(f'c_bucket{i}.json') as json_file:
#         data = json.load(json_file)
#     try:

#         for j in range(len(data)):
#             print(data['items'][j]['snippet']['topLevelComment']['snippet']['textOriginal'])
#     except:
#         print("NOT DATA")
#     print(i)
#     print("$"*50)
