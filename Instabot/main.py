from instabot import Bot


bot = Bot()
bot.login(username="zain_ali090", password="")
# bot.follow('wajahat.ahmed.750331')

# bot.upload_photo('')


followers = bot.get_user_followers("zain_ali090")

for follower in followers:
    x = bot.get_user_info(follower)
