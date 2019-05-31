

f = []          # 存储每个文档词频的list 形如 [{文档1里的词频}, {文档2里的词频}, {文档3里的词频}]
df = {}         # 每次词出现的文档的个数
idf = {}        # 每次词的idf  逆词频


def cumpute_idf(corpus):
    '''
    计算每个词的idf
    :param corpus:
    :return:
    '''
    import math
    corpus_size = len(corpus)

    for doc in corpus:                  # 遍历语料库
        freq = {}
        for word in doc:                # 遍历每个文档
            if word not in freq:        # 统计词频
                freq[word] = 0
            freq[word] += 1

        f.append(freq)                  # 每个文档的词频[{}{}{}]

        for word, _ in freq.items():    # 遍历词频list里的词，没有对应的词频
            if word not in df:
                df[word] = 0
            df[word] += 1               # 放到df里，每次词出现的文档的个数

    for word, fre in df.items():
        # corpus_size   文档总数
        # fre           包含词条的文档数
        idf[word] = math.log(corpus_size / (fre + 1))


def f_avgdl(src_corpus):
    '''
        计算语料库中的平均文档长度
        每个文档分词后的词个数总和 除以 文档数
    :param src_corpus: 语料库
    :return:
    '''
    return sum([len(doc) + 0.0 for doc in src_corpus]) / len(src_corpus)


def get_BM25_score(text, src_corpus, index):
    '''
    :param text: 待测试的文档
    :param index: 文档对应存储文档list的index

    一般k1=2,b=0.75. dl是文档d的长度, avgdl是所有语料文档的平均长度.fi表示词qi在文档d中的频率
    公式：
    sum(idf*f1*(k+1)/(f1+k*(1-b+b*(dl/avgdl))))
    :return:
    '''
    k = 1.5
    b = 0.75
    score = 0
    avgdl = f_avgdl(src_corpus)
    for word in text:               # 遍历测试文档里的词
        if word not in f[index]:    # 测试文档里的词不在
            continue
        dl = len(text[index])
        score += (idf[word]*f[index][word] * (k + 1) /
                  (f[index][word] + k * (1 - b + b * (dl / avgdl))))

    return score


'''
print(f)
print(df)
print(idf)
'''


def BM25similarity(test_text, src_corpus):
    '''
    :param test_text:       测试文档（1个）
    :param src_corpus:      源文档 （多个）
    :return:
    '''
    cumpute_idf(src_corpus)

    res = []
    for index in range(len(src_corpus)):
        scor = get_BM25_score(test_text, src_corpus, index)
        res.append(scor)
    print(res)
    return res


corpus = [['这是', '一只', '分木', '易', '阿斯顿', '发', '傻傻', '广发', '斯蒂芬', '这是', '这是'],
        ['今天', '是', '一个', '发', '傻傻', '史蒂芬', '这是', '不错']
        ]
text = ['今天', '来', '一个', '傻傻', '阿斯顿', '嗯嗯啊啊']


r = BM25similarity(text, corpus)
if r[0] > r[1]:
    print('B')
else:
    print('C')


