import tweepy, webbrowser, time

#Authorization
consumer_key = "<<consumer_key>>"
consumer_secret_key = "<<consumer_secret_key>>"
access_token = "<<access_token>>"
access_token_secret = "access_token_secret"

class TwitterAPI:
    '''
    A class to automate and extract data from the Twitter API.
    '''
  
    def __init__(self, consumer_key, consumer_secret_key, *args, **kwargs):
        self.consumer_key = consumer_key
        self.consumer_secret_key = consumer_secret_key
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret_key, 'oob')  #OAuth = Login service
        self.auth.set_access_token("<<access_token>>")                                   #Set access tokens to automate
        self.api = tweepy.API(self.auth)       #Twitter API


    def Authorization(self):
        '''
        Getting Pin.
        '''
        webbrowser.open(self.auth.get_authorization_url())         #Send the user to the redirect url
        self.pin = input("Enter Authorization Pin: ")

    def tweet(self, message, image=None):
        '''
        A method for tweeting. If you want to tweet with image, Enter path of image with keyword 'image'. Assign this function to a variable if you want to delete the tweet using 'variable.destroy()' method.
        '''
        if image is not None:
            img = self.api.media_upload(image)
            return self.api.update_status(message, media_ids=[img.media_id_string])  #   #Tweet
        else:
            return self.api.update_status(message)  

    def get_timeline(self, username='AnshulJawale'):
        '''
        Returns a timeline of the feed in the homepage. Enter the username of the user whose timeline you want to see.
        '''    
        user = self.api.get_user(username)
        user_timeline = user.timeline()
        for status in user_timeline:
            print("\n")
            status_dict = vars(status)
            print(status.text)
            print(f"Tweet id : {status_dict['id_str']}")


    def follow_user(self, to_follow_username):
        return self.api.create_friendship(to_follow_username)


    def unfollow_user(self, to_unfollow_username):
        return self.api.destroy_friendship(to_unfollow_username)

