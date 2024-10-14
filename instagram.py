from instabot import Bot

bot=Bot()
bot.login(username="yourusername",password="yourpassword")
bot.follow('id_account_you_want_to_follow')

#upload photo
bot.upload_photo('path',caption="caption")

#unfollow account
bot.unfollow('account_to_unfollow')

#message to multiple users
bot.send_messages("Your Message",['username','username2'])

#instagram detail profile info,follower and similarly for following
followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

