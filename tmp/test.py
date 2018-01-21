#!/usr/bin/env python
# encoding: utf-8
'''
@author: leiweijie
Create on2018年1月21日
'''
import urllib,urllib2,ssl
import base64
import json
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 
def get_my_token():
    '''获取百度AI自己的token 30天需要从新获取一次'''
    ak = 'hDPGm4xLD42ZmDFzeLtM8SLM'
    sk = 'DX2j2ANwIFiFz5gCPlNYDeTgEhybRBhs'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' %(ak,sk)
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        print(content)
# 
# my_token={"access_token":"24.e9bacddd3b972b1487bda9f9a5cb6e9c.2592000.1519103086.282335-10723956","session_key":"9mzdXvzPHCWRxKRPOM1DD89ddbjYetb11EzowiShCB\/QdxY0DuPz2J\/PrtjdtmS3cAeAhepjcHWMZp153dIKSFy28PX3mQ==","scope":"public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic brain_ocr_general_enhanced vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower bnstest_fasf lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission","refresh_token":"25.634adbfced0015e7c79511962005e805.315360000.1831871086.282335-10723956","session_secret":"33eede8c79f266a8821cbe089422dd89","expires_in":2592000}
# for k,v in my_token.items():
#     print k,my_token[k]
def pic_change_base64():
    '''将图片转为base64编码'''
    with open('tt.jpg','rb') as f:
        data = base64.b64encode(f.read())
    return data

def my_send_post():
    '''调用百度AI接口返回图片内容'''
    image_data = pic_change_base64()
    data = {'image':image_data,'access_token':'24.e9bacddd3b972b1487bda9f9a5cb6e9c.2592000.1519103086.282335-10723956'}
    data = urllib.urlencode(data)
    host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request,data=data)
    my_data = response.read()
    my_data = json.loads(my_data)
    return my_data
  
if __name__ == '__main__':
    text = my_send_post()
    for x in text['words_result']:
        print x['words']
        with open('my_text.txt','a+') as f:
            f.write(x['words'].encode())