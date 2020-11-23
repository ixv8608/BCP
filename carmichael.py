import multiprocessing.dummy as mp
import numpy as np
import math



Clist = []
def generateCarmichaelNumber(num):
    if math.gcd(2,num) == 1 and all(math.gcd(k,num) == 1 for k in
                                    range(3, int(round(num**0.5)), 2)):
        return 'Prime'
    elif math.gcd(num, 2) == 1 and all(pow(b, num, num)==b for b in
                                       range(1, num)):
        Clist.append(num)
    return 'Composite'  # implicit "else" return

def run():
    generateCarmichaelNumber(1000000)

def compute():
    print(2/(np.log(2048)))
    print(2/(np.log(3072)))
    print(2/(np.log(8192)))

if __name__ == "__main__":

    # p = mp.Pool(4)
    # p.map(run, range(1000000))  # range(0,1000) if you want to replicate your example
    # p.close()
    # p.join()
    # p = mp.Pool(4)
    # p.map(carm_math_reorder, range(10000000))  # range(0,1000) if you want to replicate your example
    # p.close()
    # p.join()
    # for i in range(2000):
    #     carm_math_reorder(i)
    #
    # print(Clist)
    pass