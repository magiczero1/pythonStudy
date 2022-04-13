str = "III"  #罗马数字

def RomaNum(str):
    tempNum = [0, 0]
    theSum = 0
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
           "CD": 400, "CM": 900}
    for i in range(len(str)):
        if len(str) == 1:
            return map.get(str)
        else:
            if map.get(str[i-1]) >= map.get(str[i]):
                theSum = theSum+map.get(str[i-1])
            else:
                tempNum[0] = -map.get(str[i-1])
                tempNum[1] = map.get(str[i])
                theSum = theSum + sum(tempNum)
    return theSum

print(RomaNum("VX"))

