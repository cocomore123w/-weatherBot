import requests

###
token = ''
channelID =
##################

##
def push(ctx):
    channel_id = channelID  # 頻道ID
    _token = "Bot "+ token  # 以Bot發送開頭須加上Bot {token}

    post = requests.post(
        url=f"https://discord.com/api/channels/{channel_id}/messages",
        headers={
            "Authorization": _token,
            "Content-Type": "application/json"
        },
        json={
            "content": ctx
        }
    )
    return post.ok

#print(push())