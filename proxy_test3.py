# -*- coding:utf-8 -*-
header = HeaderPool.get_header()
time.sleep(random.uniform(0, 1))
response = download_session.get(url, headers=header, verify=False, proxies=proxy, timeout=5)

