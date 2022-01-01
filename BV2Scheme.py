#一个将BV号转为av号并改写为 Scheme URI 的简单程序
from json.decoder import JSONDecodeError
import requests

BV2AV_API = 'https://api.bilibili.com/x/web-interface/view'  # ?bvid=
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

def bv2av(bv):
    r = requests.get(BV2AV_API, {'bvid': bv}, headers=HEADER)
    response = decode_json(r)
    try:
        return str(response['data']['aid'])
    except (KeyError, TypeError):
        return '获取av号失败'

def decode_json(r):
    try:
        response = r.json()
    except JSONDecodeError:
        return -1
    else:
        return response

def main():
    bv = input('请输入BV号:')
    print('对应 Scheme URI   bilibili://video/' + bv2av(bv))
    input('按回车键退出')

if __name__ == '__main__':
    main()