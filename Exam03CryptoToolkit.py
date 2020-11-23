from random import random
import math
import random
from math import perm

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# Euler Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result


def computeInverseFermat(aValue, pValue):
    print(pow(aValue, pValue-2, pValue))

def computeEuler(aValue, mValue):
    print(pow(aValue, phi(mValue), mValue))

def countSquareAndMultiplyOperations(eValue):
        # if form == "first":
        #     val = str(bin(pow(2, exponent) + 1))[3:]
        #     countOperations = 0
        #     for exponent in val:
        #         if exponent == '1':
        #             countOperations += 2
        #         if exponent == '0':
        #             countOperations += 1
        #     print(countOperations)
        # elif form == "second":
        #     val = str(bin(pow(2, exponent) - 1))[3:]
        #     countOperations = 0
        #     for exponent in val:
        #         if exponent == '1':
        #             countOperations += 2
        #         if exponent == '0':
        #             countOperations += 1
        #     print(countOperations)
        countOperations = 1
        val = str(bin(eValue))[2:]
        for i in range(2, len(val)):
            if val[i] == '1':
                countOperations+=2
            if val[i] == '0':
                countOperations += 1
        print(countOperations)

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

def encryptRSA(x, e, p, q):
    nValue = p * q
    yValue = pow(x, e, nValue)
    return yValue

def decryptRSA(y, d, p, q):
    nValue = p * q
    xValue = pow(y, d, nValue)
    return xValue

def chineaseRemainderTheorem(a, b, modulo1, modulo2):
    # Check if GCD is not 1, needs to be 1 or else problems
    if gcd(modulo1, modulo2) != 1:
        return "ERROR"
    if a == 1 and b == 0:
        OneZeroVector = a * modulo2 * modInverse(modulo2, modulo1) % (modulo1 * modulo2)
        print(OneZeroVector)
    elif a == 0 and b == 1:
        ZeroOneVector = b * modulo1 * modInverse(modulo1, modulo2) % (modulo1 * modulo2)
        print(ZeroOneVector)
    else:
        OneZeroVector = a * modulo2 * modInverse(modulo2, modulo1)
        ZeroOneVector = b * modulo1 * modInverse(modulo1, modulo2)
        result = OneZeroVector + ZeroOneVector
        print(result % (modulo1 * modulo2))


def squareAndMultiply(base, exponent, modulus):
    return pow(base, exponent, modulus)

def squareAndMultiply(base, exponent, modulus):
    #Converting the exponent to its binary form
    binaryExponent = [int(i) for i in bin(exponent)[2:]]
    #Application of the square and multiply algorithm
    result = 1
    for i in binaryExponent:
        if i ==0:
            result = (result*result) % modulus
        else:
            result = (result*result*base) % modulus

    return result


CarmichaelNumberList = []
def isCarmichaelNumber(num):
    if math.gcd(2,num) == 1 and all(math.gcd(k,num) == 1 for k in range(3, int(round(num**0.5)), 2)):
        return 'Prime'
    elif math.gcd(num, 2) == 1 and all(pow(b, num, num)==b for b in range(1, num)):
        CarmichaelNumberList.append(num)
    return 'Composite'  # implicit "else" return

def findAllCarmichaelNumbers(startValue, endValue):
    for i in range(startValue, endValue):
        isCarmichaelNumber(i)


def decryptRSA129():
    p = 3490529510847650949147849619903898133417764638493387843990820577
    q = 32769132993266709549961988190834461413177642967992942539798288533

    totient = (p-1)*(q-1)
    e = 9007
    n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541

    # from stack overflow
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    d = modinv(e,totient)
    ciphertext = 91045328916998417442482698097341808065794629308863274299915006508648723904695483923175519319873972294295937946793571148693700025

    p = str(pow(ciphertext,d,n))
    res = ""
    for i in range(0, len(p), 2):
      v = p[i:i+2]
      if v == '00':
        res +=  ' '
      else:
        res += chr(int(v)+97-1)

    print(res)

def isPrime(p, s):

    # The number 2 is not composite, it is prime.
    if p == 2:
        return True
    # All even numbers are composite, check for them
    elif p % 2 == 0:
        return False
    # Check if the
    for i in range(1, s):
        a = random.randint(2, p - 2)
        if pow(a, p - 1) % p != 1:
            return False
    return True, p


# In practice, it is often desirable to have
# a DLP in groups with prime cardinality in
# order to prevent attacks
def discreteLogSolver(base, power, mod):
    count = 0
    for i in range(1, mod - 1):
        if pow(base, count, mod) == power:
            print(count)
            break
        count += 1
    Exception("Solution Does Not Exist")


# P should have a similar length as
# the RSA modulus n, i.e., 1024 or beyond, in order to provide strong security.
# ALPHA needs to have a special property: It should be a primitive element
def computeB_Diffe_Hellman(p, b, alpha):
    B = pow(alpha, b, p)
    return B

def computeA_Diffe_Hellman(p, a, alpha):
    A = pow(alpha, a, p)
    # k = pow(B, a, p)
    return A


def orderOf(a, m):
   lst = []
   if math.gcd(a, m) != 1:
       return 0, []
   value = 1
   for i in range(1, m + 1):
       value = (value * a) % m
       lst.append(value)
       if value == 1:
           return i, lst


def findCollisionProbability(power, percentage):
    powerProduct = pow(2,(power + 1))
    naturalLogProduct =  math.log(1 / (1/1 - percentage))
    numberOfBits = math.log2(math.sqrt(powerProduct * naturalLogProduct))
    print(numberOfBits, end="\t")

def birthdayParadoxNoCollisionProbability(tValue):
    # result = 1
    # for i in range(tValue):
    #     result *= 1 - (i/365)
    # print(result)
    print("Probability that there is no birthday collision", perm(365, tValue) / pow(365, tValue))
    print("Probability that there is at least 1 birthday collision", 1 - (perm(365, tValue) / pow(365, tValue)))
if __name__ == '__main__':
    # print(squareAndMultiply(1234567, 2345678, 3333337))
    # findAllCarmichaelNumbers(1, 500)
    # print(CarmichaelNumberList)
    # computeInverseFermat(2, 7)
    eValue = modInverse(7, phi(3*11))
    yValue = encryptRSA(5, eValue, 3, 11)
    xValue = decryptRSA(yValue, 7, 3, 11)

    # chineaseRemainderTheorem(1, 0, 13, 17)
    # chineaseRemainderTheorem(0, 1, 13, 17)
    # chineaseRemainderTheorem(4,5, 13, 17)
    # chineaseRemainderTheorem(5,4, 13, 17)

    countSquareAndMultiplyOperations(2048)
    # for i in [5413, 81083,14699,21569,68279,54721,33589,4153,4339,26497]:
    #     print(isPrime(i, 15))
    discreteLogSolver(2, 36, 47)
    birthdayParadoxNoCollisionProbability(10)

    AValue = print(computeA_Diffe_Hellman(29, 5, 2))
    kValue = print(computeB_Diffe_Hellman(29, 12, 2))