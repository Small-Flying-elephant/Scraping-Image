步骤：
1，使用urllib2.Request(url)来请求网站地址。
2，使用urllib2.urlopen(url)来打开网站
3，读取网站
4，设置正则用来找取图片
5，使用re.compile(reg)将正则表达式的字符串形式编译为Pattern实例
6，寻找html网页中的图片
7，使用for循环，如果查到的数据上面是以http开头那么就使用urllib2.urlopen打开地址，然后读取
代码：
        #!/usr/bin/env python3
        #coding: utf-8
        import urllib
        import urllib2
        import re
        #爬取图片
        def getview(html):
            request=urllib2.Request(url)
            page=urllib2.urlopen(url)
            html=page.read()

            reg=r'<img.*src="(.*?)".*?/>'
            imge=re.compile(reg)
            imglist=re.findall(imge,html)
            x=0
            for imgurl in imglist:
                if imgurl.startswith("http"):
                    resp=urllib2.urlopen(imgurl)
                    respHtml=resp.read()
                    picFile=open('%s.jpg' % x,"wb")
                    picFile.write(respHtml)
                    picFile.close()
                    x =x+1
            print 'done'
        # main
        if __name__ == "__main__":
            url="http://www.ivsky.com/"
            getview(url)



使用文件的方式存储网站地址：
        #!/usr/bin/env python3
        #coding: utf-8
        import urllib
        import urllib2
        import re
        #爬取视频
        x=0
        def getfile(wenjian):

            f=open(wenjian)
            line=f.readlines()
            for lins in line:
                getview(lins)
            f.close()
        def getview(lins):
            global x
            request=urllib2.Request(lins)
            page=urllib2.urlopen(lins)
            html=page.read()

            reg=r'<meta.*content="(.*?)".*?/>'
            imge=re.compile(reg)
            imglist=re.findall(imge,html)

            for imgurl in imglist:
                if imgurl.startswith("http") and imgurl.endswith(".mp4"):
                    resp=urllib2.urlopen(imgurl)
                    respHtml=resp.read()
                    picFile=open('%s.mp4' % x,"wb")
                    picFile.write(respHtml)
                    picFile.close()
                    x =x+1
            print 'done'
        # main
        if __name__ == "__main__":
        #     url="https://www.instagram.com/p/BB0YPXBG4sN/"
            wenjian="C:/Users/pc/Desktop/videlurl.txt"
            getfile(wenjian)
        #     getview(url)
