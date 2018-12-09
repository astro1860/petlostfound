import json 
import pdb
d_text = []
d_pic = []

with open("data/friends_timeline_20181123.out.json") as f:
    d_json = json.load(f)

for weibo in d_json["statuses"]:
    d_text.append(weibo["text"])
  #  d_pic.append(weibo["original_pic"])


pdb.set_trace()
print(d_text)