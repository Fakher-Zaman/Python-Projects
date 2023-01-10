# $ pip install instabot

from instabot import Bot

bot = Bot()
bot.login(username = "username", password = "pass123")

# bot.follow('python_hub')
# bot.upload_photo("D:/Python Coding/Python Projects/Python_logo_icon.png", captions = "I love programing myths")
# bot.unfollow('python_hub')
# bot.send_message("Hello World! I love python", ["user1", "user2", "user3"])

followers = bot.get_user_followers("username_here")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("username_here")
for follwg in following:
    print(bot.get_user_info(follwg)) 