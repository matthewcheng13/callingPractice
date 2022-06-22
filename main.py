import request


_INFOBLOX_LAB_INFO = {
    'url': 'https://dc01dnslab.net.adp.com/wapi/v2.6.1',
    'username': 'gnsauto',
    'password': 'gnsauto01'
}


def call(view):
    URL = f'{_INFOBLOX_LAB_INFO["url"]}/{view}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

