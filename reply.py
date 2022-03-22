import weather_req

################

def _replyAns(user,msg):

    if msg == "你好":
        return "OUO"
    if msg == "87":
        return f"{user.mention}北七噢"
    if msg == "臭":
        return "<:kusai_1:892657327583416340>"
    if msg == "天氣":
        return weather_req.get_data() if 0 else weather_req.get_data()
    return

