import urllib.request as urlrequest
import json

id_list = []
with open('firstdata.txt','w') as outputfile:   #w 重新写入，a 在文末添加
    for id in id_list:
        url = 'https://.../{}'.format(id)
        url_content = urlrequest.urlopen(url)
        json_content = json.loads(url_content.decode('utf8'))
        rank = json_content['adsad']['adadad']
        outputfile.write('{} {}\n'.format(id,rank))