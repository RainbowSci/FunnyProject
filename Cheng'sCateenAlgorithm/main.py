import numpy as np


def ChengCanteenAlgo(test_num):
    res=[]
    for i in range(test_num):
        p=np.random.choice(range(1,7),4,replace=False)
        # print(p)
        tmp_res = np.sum(p) % 4
        res.append(tmp_res)

    return res

if __name__ == '__main__':
    counts=1000000
    res=ChengCanteenAlgo(counts)
    c0,c1,c2,c3=res.count(0),res.count(1),res.count(2),res.count(3)
    print(c0/counts,c1/counts,c2/counts,c3/counts)