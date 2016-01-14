import feedparser
import urllib
import os
from ftplib import FTP
from datetime import datetime

time = datetime.now()
newfolder = '{FilePath}' + str(time.month) + '-' + str(time.day) + '-' + str(time.year) + '/'

if not os.path.exists(newfolder):
    os.makedirs(newfolder)

ip_torrents_rss = "{RSS feed URL}"

feed = feedparser.parse(ip_torrents_rss)

posts = {}

# Length and items may need to be adjusted depending on how the feed is built

for i in range(0, len(feed['entries'])):
    posts[feed['{list entry name}'][i].{feed dict value}] = feed['{list entry name}'][i].{feed dict value}



for iterater in iteration:
    for key, value in posts.iteritems():
        k = key
        if iter in k:
            url = value
            urllib.urlretrieve(url, newfolder + key + 'file extension')

fileList = []

for i in os.listdir(newfolder):
    fileList.append(i)

session = FTP('{address}','{username}','{password}')
session.cwd('{location you are putting file}')

for i in fileList:
    f = open(i, 'rb')
    a = 'STOR ' + i
    session.storbinary(a, f)

session.quit()
