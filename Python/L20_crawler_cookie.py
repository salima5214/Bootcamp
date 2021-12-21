# L19: https://reurl.cc/Xlo7X0

# pip install beautifulsoup4
import urllib.request as req



def getData(url):
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode( "utf-8" )
    print( data )

    # with req.urlopen(url) as response:
    #     data = response.read().decode( "utf-8" )
    # print( data ) 

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root.title.string)

    # titles = root.find("div", class_ = "title")
    # print(titles.a.string)

    titles = root.find_all("div", class_ = "title")
    # print(titles)
    for title in titles:
        if title.a != None:
            print(title.a.string)


    nextLink = root.find("a", string ="‹ 上頁")
    # print(nextLink["href"])
    return nextLink["href"]


pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
pageURL = "https://www.ptt.cc" + getData(pageURL)
print("####################################")
pageURL = getData(pageURL)
print(pageURL)

pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1

