import urllib.request as req
import bs4
output = []

def getData(url):
    # url="https://www.ptt.cc/bbs/Lottery/index.html"
    request=req.Request(url, headers={
        "Cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章的標題
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    likes=root.find_all("div", class_="nrec")
    # print(titles["href"])
    n=0
    while(n < len(titles)):
        if titles[n].a != None:
            singleTitle=titles[n].a.string
        likeCount = likes[n].string
        if likeCount == None:
            likeCount=0   
        #點進每篇貼文，取得發布時間
        articleLink=titles[n].find("a",string=singleTitle)
        if articleLink != None:
            singleArticleURL = "https://www.ptt.cc"+ articleLink["href"]
        
        articleRequest=req.Request(singleArticleURL, headers={
            "Cookie":"over18=1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        })
        with req.urlopen(articleRequest) as response:
            articleData=response.read().decode("utf-8")
        articleRoot=bs4.BeautifulSoup(articleData, "html.parser")
        articlePublishTime=articleRoot.find_all("span", class_="article-meta-value")

        if articlePublishTime != []:
            articlePublishTime=articlePublishTime[3].string
        else:
             articlePublishTime="No Publish Time"
        ## 判斷文章未被刪除
        if singleTitle:
            output.append(singleTitle + "," + str(likeCount) + "," + articlePublishTime + "\n")
        n=n+1
        singleTitle = ""  #重置
    # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")
    # print(nextLink)
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
    print("-----page" + str(count) + " done. -----")

with open("article.txt", mode="w") as f:
    f.writelines(output)


