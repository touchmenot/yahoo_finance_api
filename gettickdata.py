import urllib
import urlparse
import urllib2
import re, sys ,string
import datetime

def getTickData(yyyymmdd):
    for line in open('code.txt').readlines():
        code = str(line.rstrip('\r\n'))
        url='http://hopey.netfonds.no/posdump.php?date=' + str(yyyymmdd) + '&paper=' + code + '.O&csv_format=txt'
        print url
        urllib.urlretrieve(
                           url = url
                           ,filename = code + '/' + code + str(yyyymmdd) + '.txt'
                           )
        print

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    d = datetime.datetime.today()
    for i in range(1,3):
        one_day = datetime.timedelta(days=i)
        dt=d-one_day
        getTickData(dt.strftime("%Y%m%d"))

if __name__== '__main__':
    main()
