import jieba


def Jaccrad_similarity(model, reference):  # terms_reference为源句子，terms_model为候选句子
    '''
    Jaccard Similarity 杰卡德相似度计算

    计算公式 A与B的交集 除以 A与B的并集

    :param model:
    :param reference:
    :return:
    '''
    terms_reference = jieba.cut(reference)  # 默认精准模式
    terms_model = jieba.cut(model)
    grams_reference = set(terms_reference)  # 去重；如果不需要就改为list
    grams_model = set(terms_model)
    temp = 0
    for i in grams_reference:
        if i in grams_model:
            temp = temp + 1
    fenmu = len(grams_model) + len(grams_reference) - temp  # 并集
    jaccard_coefficient = float(temp / fenmu)  # 交集
    return jaccard_coefficient


a = "香农在信息论中提出的信息熵定义为自信息的期望"
b = "信息熵作为自信息的期望"
c = "信息论中的定义是香农提出的"

jaccard_coefficient_1 = Jaccrad_similarity(a, b)
jaccard_coefficient_2 = Jaccrad_similarity(a, c)

if jaccard_coefficient_1 > jaccard_coefficient_2:
    print('---->1')
else:
    print('---->2')


# print(jaccard_coefficient)



