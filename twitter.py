import requests
from twitterAuth import headers

ans = requests.get("https://api.twitter.com/2/tweets?ids=1261326399320715264,1278347468690915330",headers=headers)

print(ans.json())