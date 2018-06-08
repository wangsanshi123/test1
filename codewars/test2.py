import re


def alphabet_position(text):
    return " ".join(map(str, map(lambda x: x - 96 if x > 96 else x - 64,
                                 [ord(alpha) for alpha in text if re.match(r'[a-z|A-Z]', alpha)])))

    pass


def find_short(s):
    temp = map(lambda x: len(x), s.split(" "))
    temp.sort()
    return temp[0]


def song_decode(song):
    return " ".join(song.replace('WUB', ' ').split())


def song_decoder1(song):
    return re.sub(r'\s+', ' ', song.upper().replace("WUB", ' ').strip())


def solution(digits):
    nums = [int(item) for item in digits]
    nums_4 = nums[:-4]

    max = nums_4[0]
    index = [0]
    time = 0
    for i, item in enumerate(nums_4):
        if item > max:
            max = item
            index[0] = i
        elif item == max:
            index.append(i)

    temp_a = sorted([(nums[(item + 1)], item) for item in index], reverse=True)

    while True:
        time += 1
        list_temp = []
        max = temp_a[0]
        for item in temp_a:
            if item[0] == max[0]:
                list_temp.append(item)
            else:
                break
        if len(list_temp) == 1:
            break


def solution2(digits):
    nums = [int(item) for item in digits]
    nums_4 = nums[:-4]

    nums_4_index = sorted([(i, item) for i, item in enumerate(nums_4)], key=lambda x: x[1], reverse=True)
    result = []
    result.append(nums_4_index[0][0])
    time = 0
    while True:
        time += 1
        list_temp = []
        max = nums_4_index[0]
        for item in nums_4_index:
            if item[1] == max[1]:
                list_temp.append(item)
            else:
                break
        nums_4_index = sorted([(item[0], nums[item[0] + time]) for item in list_temp], key=lambda x: x[1], reverse=True)
        result.append(nums_4_index[0][0])

        if len(list_temp) == 1:
            break

    index = list_temp[0][0]

    return int("".join(str(item) for item in nums[index:(index + 5)]))
    pass


def solution3(dd):
    return max(int(dd[i:i + 5]) for i in range(len(dd) - 4))


def narcissistic(value):
    #
    list = [int(item) for item in str(value)]
    sum = 0
    for item in list:
        sum += item ** len(list)
    return sum == value


def narcissistic2(value):
    return value == sum(int(item) ** len(str(value)) for item in str(value))

    pass





if __name__ == '__main__':
    # print alphabet_position('I am yuan')
    # print solution2("12364567890")
    # print solution2("12764567890")
    # print solution2("82764567890")
    # print solution2(
    #     "7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450")
    # print solution3(
    #     "7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450")

    print narcissistic(7)
    print narcissistic(371)
    print narcissistic(122)
    print narcissistic(4887)

    pass
