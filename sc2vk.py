import json
import vk_api
import vk_audio
from vk_api.audio import VkAudio

with open("data.json") as jsonFile:
    authdata = json.load(jsonFile)
    jsonFile.close()


vk_session = vk_api.VkApi(login=authdata['login'],password=authdata['password'],token=authdata['vk_access_token'])
vk_session.auth(token_only=True)
vka = VkAudio(vk_session)

track = {"id": 456244623, "owner_id": 269964069, "track_covers": [], "url": "https://cs1-49v4.vkuseraudio.net/s/v1/ac/IC0fPEG_HQ1B312N6ZQP3__BCh3uHtCzk6A1N1TNGKyhzKSsbL3SGVEwlu-HJW50q4kAoD0w0_Ja4Xmr4DipWAXVJN0cC9mmFLg8PYQL89-kl5rzL66a9op2Bh3edIFC-p7kYJBqocwNhkbGri1zqWyhCLDl7j1NbCk7x5oVIUq1yw8/index.m3u8", "artist": "ca$pr", "title": "midnight creepa", "duration": 127}

track2 = "CA$PR-Midnight Creepa"
vka2 = vk_audio.MyAudio(vkaudio=vk_session,owner_id=79827261)
vka2.create_playlist(title = 'spotifytovktest',audios=track2)
