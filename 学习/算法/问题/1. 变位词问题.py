#heart与haret互为变位词。算法要求：判断输入的一组数据，是否是变位词

#该代码无法判断是否相同，且复杂度为O(nlog(n))
def position_change_word(word1,word2):
    word1_list = list(word1)
    word2_list = list(word2)
    word2_list.sort() #排序也会花很多时间
    word1_list.sort()
    pos = 0 #标记相同的字符数量
    if len(word1) == len(word2):  #判断长度是否相等
            for i in range(len(word1)):
                if word2_list[i] == word1_list[i]:
                    pos += 1
                    if pos == len(word1_list):
                        return True
                else:
                    return False
    else:
        return False


#解法2 计数法 复杂度O(n)
def position_change_word2(word1,word2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(word1)):
        pos = ord(word1[i])-ord("a")   #利用ascii算出字符所在的位置
        c1[pos] += 1
    for i in range(len(word2)):
        pos = ord(word2[i])-ord("a")   #利用ascii算出字符所在的位置
        c2[pos] += 1
    j = 0 #初始化比较的索引位置
    matches = True #初始化为全部对应，假设
    while j < 26:
        if c1[j] == c2[j] and matches:
            j += 1
        else:
            return False       #这里可以直接返回false，性能调优一丢丢
            #matches = False
    return matches


if __name__ == '__main__':
    print(position_change_word("earth","earty"))

    print(position_change_word2("earth", "eathr"))