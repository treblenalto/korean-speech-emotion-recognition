import os
import pandas as pd
from collections import Counter

df = pd.read_csv('../data/5차_10011.csv',encoding='CP949')
columns = ['1번 감정', '2번 감정', '3번 감정', '4번 감정', '5번 감정']
df_em = df[columns]

# 가장 많이 나왔던 라벨 값 
label = []
for i in range(len(df_em)):
  emotions = Counter(df_em.iloc[i])
  label.append(emotions.most_common(1)[0][0])

speech = df['발화문']
most_common = {'speech': speech, 'emotion' : label}
most_common = pd.DataFrame(most_common)

# 감정 >> 인덱스 값으로 변환하기
cat_to_id = {'Angry': 0,
            'Disgust': 1,
            'Fear': 2,
            'Happiness': 3,
            'Neutral': 4,
            'Sadness': 5,
            'Surprise': 6}

most_common['emotion'].map(cat_to_id)
most_common.to_csv("../data/most_common.csv", index = False)