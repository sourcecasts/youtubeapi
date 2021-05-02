from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client import tools
import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload


def main():
	flow = OAuth2WebServerFlow(
		client_id='ваш id',
    	client_secret='секретный ключ',
    	scope ='https://www.googleapis.com/auth/youtube.upload',
    	user_agent ='youtube-api-v3-awesomeness'
    )

	token = 'C:/Users/Скрипт/Downloads/api/analytics.dat' #создайте пустой файл в папке скрипта с именем analytics.dat

	storage = Storage(token)
	credentials = storage.get()

	api_service_name = "youtube"
	api_version = "v3"

	body = {
    	'snippet': {
        	'categoryI': 19,
        	'title': 'Upload Testing',
        	'description': 'Hello World Description',
        	'tags': ['Travel', 'video test', 'Travel Tips']
    	},
    	'status': {
        	'privacyStatus': 'private',
        	'selfDeclaredMadeForKids': False, 
    	},
    	'notifySubscribers': False
	}


	if not credentials or credentials.invalid:
  		credentials = tools.run_flow(flow, storage)

	youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials = credentials)
	request = youtube.videos().insert(part='snippet,status', body = body, media_body = MediaFileUpload("video.mp4"))
	response = request.execute()
	if response:
    		print("Видео загружено")

if __name__ == "__main__":
    main()
