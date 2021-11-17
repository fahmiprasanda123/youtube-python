api_key = ""

from apiclient.discovery import build
from datetime import datetime
import requests
import json
import time

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
    res = youtube.channels().list(
        id=channel_id,
        # forUsername=channel_id,
        part='snippet,contentDetails,statistics').execute()
    if 'items' in res.keys():
        inputanprof = {

        }
        print(inputanprof)
        postprofile = requests.post("", data=json.dumps(inputanprof))
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        videos = []
        next_page_token = None
        while 1:
            res = youtube.playlistItems().list(playlistId=playlist_id, 
                                               part='snippet', 
                                            #    maxResults=50,
                                               pageToken=next_page_token).execute()
            videos += res['items']
            next_page_token = res.get('nextPageToken')
            
            if next_page_token is None:
                break
        
        return videos
    else:
        res = youtube.channels().list(
        forUsername=channel_id,
        part='snippet,contentDetails,statistics').execute()
        inputanprof = {
           
        }
        print(inputanprof)
        postprofile = requests.post("", data=json.dumps(inputanprof))
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        videos = []
        next_page_token = None
        while 1:
            res = youtube.playlistItems().list(playlistId=playlist_id, 
                                               part='snippet', 
                                            #    maxResults=50,
                                               pageToken=next_page_token).execute()
            videos += res['items']
            next_page_token = res.get('nextPageToken')
            
            if next_page_token is None:
                break
        
        return videos
project = requests.get('')
json_project = project.json()
idkeyword = json_project['idkeyword']
idproject = json_project['idproject']
alias = json_project['alias_kyword']
keyword = json_project['keyword_youtube']
project_name = json_project['project_name']
project_type = json_project['type']
if 'Account' in project_type:
    videos = get_channel_videos(keyword)

    # print(len(videos))

for video in videos:

    videoId = video['snippet']['resourceId']['videoId']
    response = youtube.videos().list(part="snippet,contentDetails,statistics",id=videoId).execute()
    var_id = str(video['snippet']['resourceId']['videoId'])+"_"+str(idproject)
    var_code = str(video['snippet']['resourceId']['videoId'])
    var_image = str(video['snippet']['thumbnails']['default']['url'])
    var_text = str(video['snippet']['description'])
    if 'likeCount' in response['items'][0]['statistics'].keys(): 
        var_like = int(response['items'][0]['statistics']['likeCount'])
    else:
        var_like = 0
    if 'commentCount' in response['items'][0]['statistics'].keys():
        var_comment = int(response['items'][0]['statistics']['commentCount'])
    else:
        var_comment = 0
    var_view = int(response['items'][0]['statistics']['viewCount'])
    var_username = str(video['snippet']['videoOwnerChannelTitle'])
    var_usernameid = str(video['snippet']['videoOwnerChannelId'])
    var_postingdate = str(video['snippet']['publishedAt'])
    var_postingtime = str(video['snippet']['publishedAt'])
    var_keyword = str(video['snippet']['videoOwnerChannelTitle'])
    getsubs = youtube.channels().list(id=var_usernameid,part='statistics').execute()
    if 'subscriberCount' in getsubs['items'][0]['statistics'].keys():
        subscribers = getsubs['items'][0]['statistics']['subscriberCount']
    else:
        subscribers = getsubs['items'][0]['statistics']['hiddenSubscriberCount']

    split_postingdate = str(var_postingdate[:10])
    split_postingtime = str(var_postingdate[11:19])
    # print(split_postingtime)

    posts = {
        
        }
    print(posts)
    res = requests.post("", data=json.dumps(posts))
    time.sleep(5)
else:
    search_videos_by_keyword(q=keyword, part='id,snippet', eventType='completed', type='video')

    def get_videos(**kwargs):
        final_results = []
        results = youtube.search().list(**kwargs).execute()

        i = 0
        max_pages = 3
        while results and i < max_pages:
            final_results.extend(results['items'])

            if 'nextPageToken' in results:
                kwargs['pageToken'] = results['nextPageToken']
                results = youtube.search().list(**kwargs).execute()
                i += 1
            else:
                break

        return final_results


def search_videos_by_keyword(**kwargs):
    results = get_videos(**kwargs)
    final_result = []
    for item in results:
        title = item['snippet']['title']
        var_code = str(item['id']['videoId'])
        videoId = str(item['id']['videoId'])
        response = youtube.videos().list(part="snippet,contentDetails,statistics",id=videoId).execute()
        if 'likeCount' in response['items'][0]['statistics'].keys(): 
            var_like = int(response['items'][0]['statistics']['likeCount'])
        else:
            var_like = 0
        if 'commentCount' in response['items'][0]['statistics'].keys():
            var_comment = int(response['items'][0]['statistics']['commentCount'])
        else:
            var_comment = 0
        var_view = int(response['items'][0]['statistics']['viewCount'])
        var_id = str(item['id']['videoId'])+"_"+str(idproject)
        var_username = str(item['snippet']['channelTitle'])
        var_usernameid = str(item['snippet']['channelId'])
        getsubs = youtube.channels().list(id=var_usernameid,part='statistics').execute()
        if 'subscriberCount' in getsubs['items'][0]['statistics'].keys():
            subscribers = getsubs['items'][0]['statistics']['subscriberCount']
        else:
            subscribers = getsubs['items'][0]['statistics']['hiddenSubscriberCount']
        var_text = str(item['snippet']['description'])
        var_image = item['thumbnails']['default']['url']
        var_postingdate = str(item['snippet']['publishedAt'])
        var_postingtime = str(item['snippet']['publishedAt'])
        split_postingdate = str(var_postingdate[:10])
        split_postingtime = str(var_postingdate[11:19])

        posts = {
           
            }
    print(posts)
    res = requests.post("", data=json.dumps(posts))
    time.sleep(5)
