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

# with open("result.json") as jsonFile:
#     jsonObject = json.load(jsonFile)
#     jsonFile.close()
# dict_er = {}
# dict1 = {}
# for num, strtrack in jsonObject.items():
#     try:
#         tr = vka.search(q=strtrack,count=2)
#         trdata = list(tr)
#         dict1[num] = trdata[0]
#         # print(trdata[0])
#         print(1)
#     except:
#         dict_er[num] = strtrack
#         print(2)

# with open('trvk.json', 'w') as fp:
#     json.dump(dict1, fp)

# with open('errors.json', 'w') as ep:
#     json.dump(dict_er, ep)


track = 'BLAGOIBLAGO-СПАСАТЕЛЬНЫЙ КРУГ'
# tr = vka.search(track)
# trdata = list(tr)
# print(trdata[0])

vk = vk_audio.VkAudio(vk=vk_session)
owner = vk.uid
data = vk.load(owner)#получаем наши аудио
# print(data)

# second_audio = data.Audios[1]#берем вторую аудиозапись
# first_playlist = data.Playlists[0] #берем первый плейлист
# print(list(first_playlist))
# format_string = "{title} - {artist} ({owner_id}_{id}) -> {url}"
# print("2.",format_string.format(
#     title=second_audio.title, #так же можно second_audio['title']
#     artist=second_audio.artist,
#     owner_id = second_audio.owner_id,
#     id=second_audio.id,
#     url=second_audio.url# url - property, при ее получении посылается запрос в вк
#     ))
# print("1.",format_string.format(**first_playlist.Audios[0].toArray()))



# dict_er = {}
# for num, strtrack in jsonObject.items():
#     try:
#         print(num)
#         print(strtrack)
#     except:
#         dict_er[num] = strtrack




# with open('errors.json', 'w') as fp:
#     json.dump(dict_er, fp)