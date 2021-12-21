# L15: https://reurl.cc/bnMLy3

import urllib.request as request
# import json

src = "http://www.ntu.edu.tw"
with request.urlopen(src) as response:
    data = response.read().decode( "utf-8" )
    # data = json.load(response) 
print( data )
