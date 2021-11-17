api_key = ""

from apiclient.discovery import build
from datetime import datetime
import requests
import json
import pprint
import time

youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_comments(idkeyword, idproject, keyword, project_name, **kwargs):
    comments = []
    try:
        results = youtube.commentThreads().list(**kwargs).execute()
        while results:
            for item in results['items']:
                username = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                idcomment = str(item['snippet']['topLevelComment']['id'])+"_"+str(idproject)
                profiluser = item['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
                idvideo = item['snippet']['topLevelComment']['snippet']['videoId']
                datecomment = str(item['snippet']['topLevelComment']['snippet']['publishedAt'])
                userid = item['snippet']['topLevelComment']['snippet']['authorChannelId']
                channelURL = item['snippet']['topLevelComment']['snippet']['authorChannelUrl']
                # comments.append(comment)
                # comments.extend([(title, comment)])
                split_postingdate = datecomment[:10]
                posts = {
                   
                }
                print(posts)
                res = requests.post("", data=json.dumps(posts))
                time.sleep(5)
            if 'nextPageToken' in results:
                kwargs['pageToken'] = results['nextPageToken']
                results = youtube.commentThreads().list(**kwargs).execute()
            else:
                break
        return comments
    except:
        print("error")
        time.sleep(5)
    

if __name__ == '__main__':
    project = requests.get('')
    json_project = project.json()
    idkeyword = json_project['idkeyword']
    idproject = json_project['idproject']
    keyword = json_project['alias_kyword']
    project_name = json_project['project_name']
    response = requests.get("")
    json_response = response.json()
    for item in json_response['hits']['hits']:
        videoId = item['_source']['code']
        comments = get_video_comments(idkeyword, idproject, keyword, project_name, part='snippet', videoId=videoId, textFormat='plainText')

    formatted_json = pprint.pformat(response.json())
    print(formatted_json)
    videoId = response['_source']['code']
    print(videoId)
    comments = get_video_comments(part='snippet', videoId=videoId, textFormat='plainText')

# print(len(comments),comments)