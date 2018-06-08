import re
from itertools import combinations
from collections import deque


def choose_best_sum(t, k, ls):
    # your code
    try:
        return max([sum(item) for item in combinations(ls, k) if sum(item) <= t])
    except:
        return None
        pass
    pass


import itertools


def choose_best_sum1(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None


def domain_name(url):
    result = re.match(r'(http|https)://(www.|)(.*)\.', url)
    return result.groups()[2] if result else ''
    pass


def domain_name1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def perimeter(n):
    # your code
    i = 1
    j = 1
    ls = [1, 1]

    for item in range(n - 1):
        i, j = i + j, i
        ls.append(i)
        pass
    return 4 * sum(ls)
    pass


def perimeter1(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)



def whoIsNext(names, r):
    # your code

    queue = deque(names)

    while r:
        item = queue.popleft()
        queue.append(item)
        queue.append(item)
        r -= 1
    return item
    pass

def whoIsNext2(names, r):
    # your code
    names = [[1, i] for i in (names)]
    queue = deque(names)
    result = ""
    while r:
        if not queue[0][0] - 1:
            if queue[-1][1] is queue[0][1]:
                queue[-1][0] += 1
                result = queue[0]
            else:
                queue.append(queue[0])
                result = queue.popleft()
        else:
            queue[0][0] -= 1
            result = queue[0]
        r -= 1
    return result[1]
    pass


if __name__ == '__main__':
    # xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

    # print(choose_best_sum1(230, 4, xs))
    # print(choose_best_sum(230, 4, xs))
    # url1 = "http://github.com/carbonfive/raygun"
    # url2 = "http://www.zombie-bites.com"
    # url3 = "https://www.cnet.com"
    #
    # url4= 'https://xakep.ru/'
    #
    # print(domain_name(url1))
    # print(domain_name(url2))
    # print(domain_name(url3))
    # print(domain_name(url4))

    # print(perimeter(5))
    # print(perimeter1(5))
    # print(perimeter(100))
    # print(perimeter1(100))
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    print(whoIsNext2(names, 1))
    print(whoIsNext2(names, 52))
    # print(whoIsNext(names, 7230702951))

    pass
