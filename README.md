# Korean Speech Emotion Recognition
Application of Machine Learning and Deep Learning Modules in Multi-Class Speech Emotion Classification<br>
(2021.05.03 ~ 2021.07.22)

## Data
AI-Hub 의 KETI R&D 데이터 중 [감정 분류를 위한 음성 데이터셋](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-002)을 이용해 학습하였다.<br>
해당 데이터셋은 감성대화 어플리케이션을 이용해 수집된 후 정제 작업을 거쳐 7가지 감정(happiness, angry, disgust, fear, neutral, sadness, surprise)에 대해 5명이 라벨링한 데이터이다. 5개의 라벨 중 가장 빈도수가 높은 감정을 최종 라벨값으로 사용하였다. 자세한 전처리 과정은 [preprocess](./preprocess/README.md)에서 확인할 수 있다. 

## Contributors
김태희 