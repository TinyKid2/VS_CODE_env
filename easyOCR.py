import easyOCR
import easyocr
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import Levenshtein
reader = easyocr.Reader(['ko','en'])


def play(impath):

  img = cv2.imread(impath)
  result = reader.readtext(impath)
  #데이터 가지고 오기.
  df = pd.read_excel('/Users/stone/programing/vscode/OCR/종합설계_cosmetic/종합설계_스킨케어 제품 목록_수정.xlsx', header=None)
  df[1] = df[1].astype(str)
  # 사진에서 Threshhold 가져오기.
  THR = 0.5
  result1 = ''
  for bbox, text, conf in result:
  
    if conf > THR:
      result1 = result1 + text
  # print(result1)
  result = result1.split(' ')
  dic = {}
  for i in range(len(result)):
      dic[i] = result[i]
  print(dic) 
  # {0: 'DrGRED', 1: 'BLEMISHMULTI', 2: 'FLUIDMoisture', 3: 'soothing', 4: 'solutionMessageDATE100', 5: 'mL3,38MY', 6: 'SKIN', 7: "MENTOR부스터'DrG"}
  #{0: '레드', 1: '불레미쉬', 2: '클리어', 3: '수딩', 4: '토너5가지', 5: '시카', 6: '핵심마데카소andcalming', 7: 'toner', 8: 'thatskinApDly', 9: 'enough', 10: 'toner', 11: 'on', 12: 'theTap', 13: 'the', 14: 'remainingproduct성분인soothes', 15: 'sensitive', 16: "'cotfon", 17: '=contents'}
  
  # dic에서 원하는 부분만 선택받기
  choose = input('제품의 제목이 들어있는 숫자를 모두 입력해주세요. 띄어쓰기로 구분해서 ex) 0 1 2 3')
  chose = [int(x) for x in choose.split()]
  
  
  # dic에서 원하는 문장 만들기
  sen = ''
  for i in chose:
    sen = sen + dic[i] + ' '
  # print(sen)
  
  similarity = df[1].apply(lambda x: Levenshtein.distance(x, sen)).idxmin()

  print(df.loc[similarity]) 
  
  return(df.loc[similarity])




play("/Users/stone/programing/vscode/OCR/종합설계_cosmetic/dr.G_red_toner.jpeg")

