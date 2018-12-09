import json 
import pdb
import urllib.request

d_text = []
d_pic = []

with open("data/friends_timeline_20181123.out.json") as f:
	d_json = json.load(f)

dog_num = 1

for weibo in d_json["statuses"]:
	#print(weibo["text"])
	d_text.append(weibo["text"])
	if "original_pic" in weibo.keys():
		pic_addr = weibo["original_pic"]
		#print(pic_addr)
		#urllib.request.urlretrieve(pic_addr, "data/"+str(dog_num)+".jpg")

	dog_num = dog_num + 1

#pdb.set_trace()
print(d_text)