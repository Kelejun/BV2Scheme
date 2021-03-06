#一个将BV号转为av号并改写为 Scheme URI 的简单程序
from json.decoder import JSONDecodeError
import requests

BVAPI = 'https://api.bilibili.com/x/web-interface/view'  # ?bvid=
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

def bv2av(bv):
    r = requests.get(BVAPI, {'bvid': bv}, headers=HEADER)
    response = decode_json(r)
    try:
        return str(response['data']['aid'])
    except (KeyError, TypeError):
        return '获取失败'

def decode_json(r):
    try:
        response = r.json()
    except JSONDecodeError:
        return -1
    else:
        return response

def main():
    bv = input('请输入BV号:')
    av = bv2av(bv)
    if av == '获取失败':
        print('无法转换，因为无法获取视频 av 号，请检查 BV 号是否正确、网络连接是否正常')
    else:
        print('对应 Scheme URI 为： bilibili://video/' + av)
    input('按Enter退出')

if __name__ == '__main__':
    main()