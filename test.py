import requests
import re

if __name__ == "__main__":
    s = [0xfb,0x9E, 0x67, 0x12, 0x4E, 0x9D, 0x98, 0xAB, 0, 6, 0x46, 0x8A, 0xF4, 0xB4, 6, 0xB, 0x43, 0xDC, 0xD9, 0xA4, 0x6C,
         0x31, 0x74, 0x9C, 0xD2, 0xA0]
    key = [0xab, 0xdd, 0x33, 0x54, 0x35, 0xef]
    ans = []
    for i in range(26):
        ans.append(chr(s[i] ^ key[i % 6]))
    print(''.join(ans))