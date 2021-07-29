import instaloader

app = instaloader.Instaloader()
username=input("user name:")
app.download_profile(username,profile_pic_only=True)