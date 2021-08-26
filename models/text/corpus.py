from konlpy.tag import Komoran

def make_corpus(text):
    komoran = Komoran()
    corpus = []
    for s in text:
        s = s.rstrip()
        # 불용어 제거
        corpus.append(' '.join([p[0] for p in komoran.pos(s) 
        if (p[0]!= '.' and p[1][0] != "J" and p[1] not in ['EP','EC', 'EF', 'ETN', 'ETM', 'XSN', 'XSV', 'XSA'])]))
    return corpus