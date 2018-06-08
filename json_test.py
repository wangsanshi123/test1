import json

import requests


def test1():
    with open("ips.json", "r") as f:
        # print json.load(f)
        results = json.load(f)["result"]
        for result in results:
            print result, "\n"

    pass


def getIpFromJson():
    with open("ips.json", "r") as f:
        results = json.load(f)[u"result"]
        print results
        with open("ips2.json", "w") as f2:
            f2.write(json.dumps(results))


def getIpFromMipu():
    with open("ips.json", "w") as f:
        result = requests.get(
            "http://proxy.mimvp.com/api/fetch.php?orderid=860170907095435229&num=500&country_group=3&http_type=1&result_fields=1,2,8&result_format=json").text

        f.write(str(result))


def test2():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, {'ticket': 1}]
    print json.dumps(data)


if __name__ == '__main__':
    # test1()
    test2()
    # getIpFromJson()
