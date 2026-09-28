import time
import sys

lirik = [
    "알고리즘엔 잘된 사람만"
    "수도 없이 뜨네요"
    "뭐 이대로 계속해서"
    "살아만 있으면 언젠가"
    "저런 날이 올까요"
    "May I be happy?"
    "매일 웃고 싶어요"
    "걱정 없고 싶어요"
    "아무나 좀 답을 알려주세요"
    "So help me"
    "주저앉고 있어요"
    "눈물 날 것 같아요"
    "그러니까"
    "Tell me, it's okay to be happy"
 ]

for baris in lirik:
     for huruf in baris:
         print(huruf, end="", flush=True)
         time.sleep (0.07)
     print()
     time.sleep(1.4)
