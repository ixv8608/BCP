import base64
import random
import math

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def xPowermod(x,m):
    lst = []
    for a in range(m):
        value = (x**a) % m
        lst.append(value)
    return lst


def orderOf(a, m):
   lst = []
   if GCD(a, m) != 1:
       return 0, []
   value = 1
   for i in range(1, m + 1):
       value = (value * a) % m
       lst.append(value)
       if value == 1:
           return i, lst


def GCD(a, b):
   if b == 0:
       return a
   else:
       return GCD(b, a % b)




def decimalToBinary(n):
    if (n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n // 2)

    print(n % 2, end=' ')




def GFMutliplication(firstHex, secondHex, galoisField):
   overflow = int(hex(galoisField), 16)
   firstHex = int(firstHex, 16)
   secondHex = int(secondHex, 16)
   moduloValue= 0x11B

   sum = 0
   while (secondHex > 0):
       if (secondHex & 1):
           sum = sum ^ firstHex
       secondHex = secondHex >> 1 # divide b by 2, discarding the last bit
       firstHex = firstHex << 1 # multiply a by 2
       if (firstHex & overflow):
           firstHex = firstHex ^ moduloValue    # reduce a modulo the AES polynomial

   return hex(sum)

def mixColumnsMultiplication():
    resultingMatrix = []
    stateMatrix = ["0x87","0x6E","0x46","0xA6"]
    constantMatrix = [
                        ["0x02", "0x03", "0x01", "0x01"],
                        ["0x01", "0x02", "0x03", "0x01"],
                        ["0x01", "0x01", "0x02", "0x03"],
                        ["0x03", "0x01", "0x01", "0x02"]
                    ]
    accumulator = 0
    for row in constantMatrix:
        for i in range(len(row)):
            value = GFMutliplication(row[i], stateMatrix[i], 256)
            # print(bin(value))
            hexValue = int(value, 16)
            accumulator ^= hexValue
        resultingMatrix.append([hex(accumulator)])
        accumulator = 0
    print(resultingMatrix)

def inverseMixColumnsMultiplication():
    resultingMatrix = []
    stateMatrix = ["0x47","0x37","0x94","0xED"]
    constantMatrix = [
                        ["0x0E", "0x0B", "0x0D", "0x09"],
                        ["0x09", "0x0E", "0x0B", "0x0D"],
                        ["0x0D", "0x09", "0x0E", "0x0B"],
                        ["0x0B", "0x0D", "0x09", "0x0E"]
                    ]
    accumulator = 0
    for row in constantMatrix:
        for i in range(len(row)):
            value = GFMutliplication(row[i], stateMatrix[i], 256)
            # print(bin(value))
            hexValue = int(value, 16)
            accumulator ^= hexValue
        resultingMatrix.append([hex(accumulator)])
        accumulator = 0
    print(resultingMatrix)


def findMatches():
    SBox = [
                0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
                0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
                0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
                0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
                0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
                0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
                0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
                0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
                0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
                0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
                0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
                0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
                0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
                0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
                0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
                0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    ]
    SBox2D = [
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    ]
    counter = 0
    for i in range(0, 16):
        for j in range(0, 256):
            if hex(SBox2D[0][i] ^ SBox[j]) == hex(SBox[(i^j)]):
                print("Left Side", hex(SBox2D[0][i] ^ SBox[j]), "x1", hex(i), "x2", hex(j))
                print("Right Side", hex(SBox[(i ^ j)]))
                counter += 1
    print(counter, counter/(16*256) * 100)


def modInverse(a, m):
    a = a % m;
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

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

# A simple method to evaluate
# Euler Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

# Driver Program

def isPrime(p, s):
    if p == 2 or p == 3:
        return True

    elif p % 2 == 0:
        return False

    for i in range(s):
        a = random.randint(2, p - 2)
        if (gcd(a, p) == 1):
            if pow(a, p - 1) % p != 1:
                return False
    return True, p

def isCarmichaelNumber(n):
    b = 2
    for i in range(n):
        if(gcd(b, n) == 1):
            if pow(b, n - 1) % n != 1:
                return False
        b += 1
    return n, True

def squareAndMultiply(number, exponent):
   binaryString = str(bin(exponent))[2:]
   result = 0
   for i in range(len(binaryString)):
       if i == 0 and binaryString[0] == '1':
           result = number
       elif binaryString[i] == '0':
           result = result**2
       elif binaryString[i] == '1':
           result = (result**2) * number
   return result

def run():
    CList = []

    for i in range(1000000):
        print(i)
        CList.append(isCarmichaelNumber(1000000))
    print(CList.pop(-3))

def createCodeBook(e, n):
    array = []
    tupleArray = []
    for i in range(65, 65+26):
        y = pow(i, e) % n
        array.append(y)

    for i in zip("abcdefghijklmnopqrstuvwxyz", array):
        tupleArray.append(i)

    return tupleArray

def decryptMessage(codebook, y):

    decryptedArray = []
    for el in y.split(";"):
        for i, j in codebook:
            if str(j) == str(el):
                decryptedArray.append(i)
    print("".join(decryptedArray))

def discreteLogSolver(base, power, mod):
    count = 0
    while(True):
        if pow(base, count, mod) == power:
            print(count)
            break
        count += 1


def powmod(x, y, p):
    res = 1;  # Initialize result

    x = x % p;  # Update x if it is more
    # than or equal to p

    while (y > 0):

        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p;

            # y must be even now
        y = y >> 1;  # y = y/2
        x = (x * x) % p;
    return res;

def ElGamalDecrypt(key, y, mod):
    k_m_inverse = modInverse(key, mod)
    x = (k_m_inverse * y % mod)
    return x

def printAlphabet(integer):
    alphabetarray = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        if i == integer:
            print(alphabetarray[i])

def birthdayParadoxNoCollisionProbability(tValue):
    result = 1
    for i in range(tValue):
        result *= 1 - (i/365)
    print(result)

def applyAlpha(i):
    k_e = pow(2, i, 29)
    printAlphabet(k_e)

def findCollisionProbability(power, percentage):
    powerProduct = pow(2,(power + 1))
    naturalLogProduct =  math.log(1 / (1/1 - percentage))
    numberOfBits = math.log2(math.sqrt(powerProduct * naturalLogProduct))
    print(numberOfBits, end="\t")


def countOperations(form, exponent):
    if form == "first":
        val = str(bin(pow(2, exponent) + 1))[3:]
        countOperations = 0
        for exponent in val:
            if exponent == '1':
                countOperations += 2
            if exponent == '0':
                countOperations += 1
        print(countOperations)
    elif form == "second":
        val = str(bin(pow(2, exponent) - 1))[3:]
        countOperations = 0
        for exponent in val:
            if exponent == '1':
                countOperations += 2
            if exponent == '0':
                countOperations += 1
        print(countOperations)


if __name__ == '__main__':
    # nums = set()
    # countGenerators = 0
    # listGenerators = []
    # for a in range(999, 4969):
    #     orderValue, lst = (orderOf(a, 4969))
    #     # print(a, orderValue, lst)
    #     if orderValue == 4968:
    #         countGenerators += 1
    #         listGenerators.append(a)
    #     nums.add(orderValue)
    # print(countGenerators)
    # print(listGenerators)
    # print("----------------------------------------------------")

    # for i in range(1, 1000):
    #    if pow(7, i, 13) == 11:
    #        print(i)
    #        break
    # Worksheet 3 Answers:
    # # -------------Question 1------------------
    # birthdayParadoxNoCollisionProbability(10)
    # birthdayParadoxNoCollisionProbability(25)
    # birthdayParadoxNoCollisionProbability(40)
    # print("-----------------------------------")
    # # -------------Question 2------------------
    # findCollisionProbability(64, 0.1)
    # findCollisionProbability(128, 0.1)
    # findCollisionProbability(256, 0.1)
    # print("\n-----------------------------------")
    # # -------------Question 2------------------
    # findCollisionProbability(64, 0.5)
    # findCollisionProbability(128, 0.5)
    # findCollisionProbability(256, 0.5)
    # print("\n-----------------------------------")
    # # -------------Question 2------------------
    # findCollisionProbability(64, 0.99)
    # findCollisionProbability(128, 0.99)
    # findCollisionProbability(256, 0.99)
    # print("\n-----------------------------------")

    # discreteLogSolver(2, 3, 19)
    # discreteLogSolver(3, 3, 97)
    # # discreteLogSolver(4, 3, 97)
    # discreteLogSolver(3, 4, 97)
    # discreteLogSolver(3, 43, 97)
    # print(orderOf(28, 29))
    # def solver(returnVal):
    #     for i in range(1, 100000):
    #         if pow(2, i, 29) == returnVal:
    #             return i


    # print(modInverse(3, 29))

    # value = GFMutliplication("0x1E", "0x37", 256)
    # print(hex(value))

    # mixColumnsMultiplication()
    # mixColumnsMultiplication()
    # inverseMixColumnsMultiplication()
    # findMatches()
    # print(phi(55))
    # print(gcd(32, 7))
    # print(isPrime(1000000, 3))

    codeBook = createCodeBook(11, 3763)
    print(codeBook)
    y = "2912;2929;3368;153;3222;3335;153;1222"
    decryptMessage(codeBook, y)

    # (3, 15), (19, 14), (6, 15), (1, 25), (22, 13), (4, 7),
    # (13, 25), (3, 21), (18, 12), (26, 4), (7, 12)
    #
    # print(printAlphabet(ElGamalDecrypt(28, 15, 29)))
    # print(printAlphabet(ElGamalDecrypt(28, 14, 29)))
    # print(printAlphabet(ElGamalDecrypt(28, 15, 29)))
    # print(printAlphabet(ElGamalDecrypt(28, 25, 29)))
    # print(printAlphabet(ElGamalDecrypt(28, 13, 29)))
    # print(printAlphabet(ElGamalDecrypt(28, 7, 29)))
    # print(printAlphabet((ElGamalDecrypt(28, 25, 29))))
    # print(printAlphabet((ElGamalDecrypt(28, 21, 29))))
    # print(printAlphabet((ElGamalDecrypt(28, 12, 29))))
    # print(printAlphabet((ElGamalDecrypt(28, 21, 29))))
    # print(printAlphabet((ElGamalDecrypt(28, 12, 29))))
    # print(printAlphabet((ElGamalDecrypt(28, 4, 29))))
    # print(printAlphabet((ElGamalDecrypt(28, 12, 29))))
    # print("------------------------------------")
    # print(printAlphabet((ElGamalDecrypt(1, 15, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 14, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 15, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 25, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 13, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 7, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 25, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 21, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 12, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 4, 29))))
    # print(printAlphabet((ElGamalDecrypt(1, 12, 29))))

    # for i in range(2, 28):
    #     print(pow(28, i, 29))

    # firstForm = []
    # for i in range(1, 17):
    #     val = str(bin(pow(2, i) + 1))[2:]
    #     firstForm.append(val)
    # secondForm = []
    # for i in range(1, 17):
    #     val = str(bin(pow(2, i) - 1))[2:]
    #     secondForm.append(val)
    # # print(firstForm)
    # # print(secondForm)
    #


    # if __name__ == "__main__":
        # decryptRSA129()
    countOperations("first", 17)
    countOperations("second", 17)
    countOperations("first", 101)
    countOperations("second", 101)
    countOperations("first", 1001)
    countOperations("second", 1001)

    #
    #     codebook = createCodeBook(11, 3763)
    #     y = "2912;2929;3368;153;3222;3335;153;1222"
    #     print(decryptMessage(codebook, y))
    #
    #     for i in range(1000000, 0, -3):
    #         val = isCarmichaelNumber(i)
    #         print(val)
    #         break
