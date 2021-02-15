
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for i in word:
        if i in ["'", '"', ",", ".", "!", ":", ";", '#', '@']:
            word = word.replace(i, '')
    return word

def get_pos(sentence):
    count = 0
    for i in sentence.split():
        stripped = strip_punctuation(i)
        lower = stripped.lower()
        if lower in positive_words:
            count += 1
    return count

def get_neg(sentence):
    
    count = 0
    for i in sentence.split():
        stripped = strip_punctuation(i)
        lower = stripped.lower()
        if lower in negative_words:
            count += 1
    return count

def erase(word):
    return word.strip('\n')

with open('resulting_data.csv', 'w') as res_dat:
    title = 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score'
    res_dat.write(title)
    res_dat.write('\n')
    with open('project_twitter_data.csv', encoding='utf8') as twi_dat:
        next(twi_dat)
        for line in twi_dat:
            if line.startswith('tweet_text,retweet_count,reply_count'):
                continue
            words = line.split(',')
            sentence = words[0].split()
            for i in range(len(sentence)):
                sentence[i] = sentence[i].replace(sentence[i], strip_punctuation(sentence[i]))
            joined = ' '.join(sentence)
            words[0] = joined
            
            retweets = str(words[1])
            replies = str(erase(words[2]))
            neg = str(get_neg(words[0]))
            pos = str(get_pos(words[0]))
            net = str(get_pos(words[0]) - get_neg(words[0]))
            res_dat.write('{}, {}, {}, {}, {}'.format(retweets, replies, neg, pos, net))
            res_dat.write('\n')
            
        
            
            
            
        
        
            



            
            
            
        
        
        