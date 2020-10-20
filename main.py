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


def findMatches(x1, x2):
    SBox = [
                ["0x00", "63 7C 77 7B F2 6B 6F C5 30 01 67 2B FE D7 AB 76],
                ["0X01", "0xCA", "0x82", "0xC9 7D FA 59 47 F0 AD D4 A2 AF 9C A4 72 C0]
                ["0X02", "0xB7", "0xFD", "0x93 26 36 3F F7 CC 34 A5 E5 F1 71 D8 31 15]
                ["0X03", "0x04", "0xC7", "0x23 C3 18 96 05 9A 07 12 80 E2 EB 27 B2 75]
                ["0X04", "0x09", "0x83", "0x2C 1A 1B 6E 5A A0 52 3B D6 B3 29 E3 2F 84]
                ["0X05", "0x53", "0xD1", "0x00 ED 20 FC B1 5B 6A CB BE 39 4A 4C 58 CF]
                ["0X06", "0xD0", "0xEF", "0xAA FB 43 4D 33 85 45 F9 02 7F 50 3C 9F A8]
                ["0X07", "0x51", "0xA3", "0x40 8F 92 9D 38 F5 BC B6 DA 21 10 FF F3 D2]
                ["0X0x", "0x8 ", "0xD ,"0xC 13 EC 5F 97 44 17 C4 A7 7E 3D 64 5D 19 73]
                ["0X09", "0x60", "0x81", "0x4F DC 22 2A 90 88 46 EE B8 14 DE 5E 0B DB]
                ["0X0A", "0xE0", "0x32", "0x3A 0A 49 06 24 5C C2 D3 AC 62 91 95 E4 79]
                ["0X0B", "0xE7", "0xC8", "0x37 6D 8D D5 4E A9 6C 56 F4 EA 65 7A AE 08]
                ["0X0C", "0xBA", "0x78", "0x25 2E 1C A6 B4 C6 E8 DD 74 1F 4B BD 8B 8A]
                ["0X0D", "0x70", "0x3E", "0xB5 66 48 03 F6 0E 61 35 57 B9 86 C1 1D 9E]
                ["0X0E", "0xE1", "0xF8", "0x98 11 69 D9 8E 94 9B 1E 87 E9 CE 55 28 DF]
                ["0X0F", "0x8C", "0xA1", "0x89 0D BF E6 42 68 41 99 2D 0F B0 54 BB 16]
    ]


if __name__ == '__main__':
    # lst = []
    # for i in range(2, 35):
    #     if GCD(i, 35) != 1:
    #         continue
    #     else:
    #         period = len(set(xPowermod(i, 35)))
    #         lst.append((i, period))
    # print(lst)


    # value = GFMutliplication("0x1E", "0x37", 256)
    # print(hex(value))

    # mixColumnsMultiplication()
    mixColumnsMultiplication()
    inverseMixColumnsMultiplication()