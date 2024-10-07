import json

#oben raw data
raw_possible = json.load(open('words.json', encoding='utf-8'))
raw_historic = json.load(open('old_words.json', encoding='utf-8'))

#prepare raw data
data_possible=[]
data_historic=[]
for word in raw_possible:
    temp={}
    temp['word']=word
    for letter in word:
        try:
            temp[letter]+=1
        except:
            temp[letter]=1
    data_possible.append(temp)
for word in raw_historic:
    temp={}
    temp['word']=word
    for letter in word:
        try:
            temp[letter]+=1
        except:
            temp[letter]=1
    data_historic.append(temp)

#calculate results
#result_possible is the result when you use every possible word as an data base and try every possible word on it
result_possible=[]
#result_historic is the result when you use every historically used word as an data base and try every possible word on it
result_historic=[]

#calculate yellow spaces for all possible words as base
for scoring_word in data_possible:
    score = 0
    for base_word in data_possible:
        temp_score = 0
        for key in scoring_word:
            if key != 'word':
                try:
                    base_word[key]
                    if scoring_word[key] <= base_word[key]:
                        temp_score += scoring_word[key]
                    else:
                        temp_score += base_word[key]
                except:
                    pass
        score += temp_score
    
    result_possible.append({
        "word":scoring_word['word'],
        "yellow_score": score,
    })

#calculate yellow spaces for all historic words as base
for scoring_word in data_possible:
    score = 0
    for base_word in data_historic:
        temp_score = 0
        for key in scoring_word:
            if key != 'word':
                try:
                    base_word[key]
                    if scoring_word[key] <= base_word[key]:
                        temp_score += scoring_word[key]
                    else:
                        temp_score += base_word[key]
                except:
                    pass
        score += temp_score
    result_historic.append({
        "word":scoring_word['word'],
        "yellow_score": score,
    })


#calculate green spaces for all possible words as base
j=0
for scoring_word in data_possible:
    score = 0
    for base_word in data_possible:
        for i in range(5):
            if(scoring_word['word'][i]==base_word['word'][i]):
                score += 1
    result_possible[j]["green_score"]=score
    j+=1

#calculate green spaces for all historic words as base
j=0
for scoring_word in data_possible:
    score = 0
    for base_word in data_historic:
        for i in range(5):
            if(scoring_word['word'][i]==base_word['word'][i]):
                score += 1
    result_historic[j]["green_score"]=score
    j+=1

#save results
with open('results_possible.json', 'w', encoding='utf-8') as f:
        json.dump(result_possible, f, ensure_ascii=False, indent=4)
with open('results_historic.json', 'w', encoding='utf-8') as f:
        json.dump(result_historic, f, ensure_ascii=False, indent=4)