import math
import saying
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import ngrams
from textblob import TextBlob
from dictsave import save, get

wordData = {}

def learning(tokens, category):
  for cur in range(len(tokens)):
    if cur == 0:
      continue
    word = tokens[cur]
    if word not in wordData:
      wordData[word] = { '$data': {}, '$cat': {}, '$sum': 0 }
      
    for i in range(cur + 1, min(len(tokens), cur + 5)):
      target = tokens[i]
      
      if target not in wordData[word]['$data']:
        wordData[word]['$data'][target] = 0
        
      if category not in wordData[word]['$cat']:
        wordData[word]['$cat'][category] = 0;
        
      value = 1 / 4 ** (i - cur - 1);
      wordData[word]['$data'][target] += value;
      wordData[word]['$sum'] += value;
      wordData[word]['$cat'][category] += 1;

#nltk.download('punkt')

sayings = saying.getData1()

#bigram = list(ngrams(tokens, 2));
#blob = TextBlob(love[0])

# Analyze and save saying data #1
categories = ['사랑',
  '인생',
  '공부',
  '성공',
  '친구',
  '독서',
  '이별',
  '시간',
  '노력',
  '희망',
  '도전',
  '자신감'];

for category in categories:
  for sentence in sayings[category]:
    tokens = word_tokenize(sentence)
    learning(tokens, category)

save(wordData, 'data/wordchain.json')