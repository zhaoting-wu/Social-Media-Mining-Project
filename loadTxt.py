import json
import pandas as pd
import re
from textblob import TextBlob
import time
from geopy.geocoders import Nominatim
from geopy.geocoders import ArcGIS
from geopy.exc import GeocoderTimedOut
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


def word_in_text(word, text):
    if text == None:
        return False
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    else:
        return False



def write_to_csv(raw_path):
    tweets_data_path = raw_path
    tweets_data = []

    tweets_file = open(tweets_data_path, 'r')
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            if("(US & Canada)" in tweet['user']['time_zone']):
                #print 'US tweet'
                tweet['text']=tweet['text'].replace("\n","")
                #print 'the location is',tweet['location']
                tweets_data.append(tweet)
        except:
            continue

    tweets = pd.DataFrame()


    tweets['created_at'] = map(lambda tweet: tweet['created_at'], tweets_data)
    tweets['id'] = map(lambda tweet: tweet['id'], tweets_data)

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    #print 'The orignal is',tweets['text']

    tweets['source'] = map(lambda tweet: tweet['source'], tweets_data)
    tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'], tweets_data)
    tweets['location'] = map(lambda tweet: tweet['user']['location'], tweets_data)
    tweets['followers'] = map(lambda tweet: tweet['user']['followers_count'], tweets_data)
    tweets['friends'] = map(lambda tweet: tweet['user']['friends_count'], tweets_data)
    tweets['time_zone'] = map(lambda tweet: tweet['user']['time_zone'], tweets_data)

    #print tweets
    print tweets['location'],type(tweets['location'])


    slist={ ('westlafayette','lafayette','indianapolis','indiana','in'):'IN',
            ('evanston','chicago','springfield','illinois','il'):'IL',
            ('losangeles','sanfrancisco','bayarea','sanjose','sandiego','sacramento','california','ca'):'CA',
            ('albany','brooklyn','manhattan','brooklyn','longisland','queens','bronx','newyork','ny'):'NY',
            ('cleverland','columbus','ohio','oh'):'OH',
            ('montgomery','alabama','al'):'AL',
            ('juneau','alaska','ak'):'AK',
            ('phoenix','arizona','az'):'AZ',
            ('little rock','arkansas','ar'):'AR',
            ('denver','colorado','co'):'CO',
            ('hartford','connecticut','ct'):'CT',
            ('dover','delaware','de'):'DE',
            ('tallahassee','florida','fl'):'FL',
            ('atlanta','georgia','ga'):'GA',
            ('honolulu','hawaii','hi'):'HI',
            ('boise','idaho','id'):'ID',
            ('des moines','iowa','ia'):'IA',
            ('topeka','kansas','ks'):'KS',
            ('frankfort','kentucky','ky'):'KY',
            ('baton rouge','louisiana','la'):'LA',
            ('augusta','maine','me'):'ME',
            ('annapolis','maryland','md'):'MD',
            ('boston','massachusetts','ma'):'MA',
            ('lansing','machigan','mi'):'MI',
            ('saint paul','minnesota','mn'):'MN',
            ('jackson','mississippi','ms'):'MS',
            ('jefferson city','missouri','mo'):'MO',
            ('helena','montana','mt'):'MT',
            ('lincoln','nebraska','ne'):'NE',
            ('carson city','nevada','nv'):'NV',
            ('concord','new hampshire','nh'):'NH',
            ('trenton','newjersey','nj'):'NJ',
            ('santa fe','newmexico','nm'):'NM',
            ('raleigh','new carolina','nc'):'NC',
            ('bismarck','north dakota','nd'):'ND',
            ('oklahoma city','oklahoma','ok'):'OK',
            ('salem','oregon','or'):'OR',
            ('harrisburg','pennsylvania','pa'):'PA',
            ('providence','rhode island','ri'):'RI',
            ('columbia','south carolina','sc'):'SC',
            ('pierre','south dakota','sd'):'SD',
            ('nashville','tennessee','tn'):'TN',
            ('austin','houston','texas','tx'):'TX',
            ('salt lake city','utah','ut'):'UT',
            ('montpelier','vermont','vt'):'VT',
            ('richmond','virginia','va'):'VA',
            ('seattle','olympia','washington','wa'):'WA',
            ('charleston','westvirginia','wv'):'WV',
            ('madison','wisconsin','wi'):'WI',
            ('cheyenne','wyoming','wy'):'WY',

    }
    State_list = {}
    countFreq = {}
    posFreq = {}
    negFreq = {}
    neuFreq = {}
    for k, v in slist.iteritems():
        for key in k:
            State_list[key] = v
    for value in slist.values():
        countFreq[value] = 0
        posFreq[value] = 0
        negFreq[value] = 0
        neuFreq[value] = 0

    '''
    Testing for dic creation
    loc='chicago'
    if(loc in State_list ):
        print State_list[loc]
    '''
    print countFreq
    Loc_res=[]
    textList = list(tweets['text'])
    timeList = list(tweets['created_at'])
    locList = list(tweets['location'])

    for tweet, loc in zip(textList, locList):
        testimonial = TextBlob(tweet)
        if(loc !=None):
            #print 'Loc is',loc
            loc_list1=[]
            loc_list2=[]
            if ',' in (loc):
                loc_list1=loc.lower().replace(' ','').split(',')
            else:
                loc_list2=(loc).lower().split()
            
            #print 'l2',loc_list2
            for loc in loc_list2:
                #print 'in l2',loc
                if loc in State_list: 
                    print 'State2 is',State_list[str(loc)]
                    Loc_res.append(State_list[str(loc)])
                    countFreq[State_list[str(loc)]] += 1
                    if testimonial.sentiment.polarity > 0:
                        posFreq[State_list[str(loc)]] += 1
                    elif testimonial.sentiment.polarity < 0:
                        negFreq[State_list[str(loc)]] += 1
                    else:
                        neuFreq[State_list[str(loc)]] += 1
                    break

            #print 'l1',loc_list1
            for loc in loc_list1:
                #print 'in l1',loc
                if loc in State_list: 
                    print 'State1 is',State_list[str(loc)]
                    Loc_res.append(State_list[str(loc)])
                    countFreq[State_list[str(loc)]] += 1
                    if testimonial.sentiment.polarity > 0:
                        posFreq[State_list[str(loc)]] += 1
                    elif testimonial.sentiment.polarity < 0:
                        negFreq[State_list[str(loc)]] += 1
                    else:
                        neuFreq[State_list[str(loc)]] += 1
                    break
                #else:
                    #print 'The Original location is',loc

    print countFreq

    print '\nSentiment Analysis by States:\n'
    print 'Positive: ', posFreq, '\n'
    print 'Negative: ', negFreq, '\n'
    print 'Neutral: ', neuFreq, '\n'


    time_count=[]
    time_dic={}

    for ct in tweets['created_at']:
        #print 'The ct is',ct
        ts = time.strftime('%Y-%m-%d', time.strptime(ct,'%a %b %d %H:%M:%S +0000 %Y'))
        time_count.append(ts)

    for ele in time_count:
        if ele not in time_dic:
            time_dic[ele]=1
        else:
            time_dic[ele]+=1
    print time_dic

    times = {}
    times['Date'] = []
    times['Num'] = []
    for key in time_dic.keys():
        times['Date'].append(key)
        times['Num'].append(time_dic[key])

    pd.DataFrame(times).to_csv('timeSeries.csv')

    #-------------------------------------------------------
    sent_dic = {}
    pos = 0
    neg = 0
    neu = 0
    #print type(tweets['text']), type(tweets['created_at'])
    
    for tweet, ti in zip(textList, timeList):
        #print '\n'
        #print tweet
        #print ti
        testimonial = TextBlob(tweet)
        flg = 0
        if testimonial.sentiment.polarity > 0:
            pos += 1
        elif testimonial.sentiment.polarity < 0:
            neg += 1
            flg = 1
        else:
            neu += 1
            flg = 2
        ts = time.strftime('%Y-%m-%d', time.strptime(ti,'%a %b %d %H:%M:%S +0000 %Y'))
        if ts not in sent_dic:
            sent_dic[ts] = {'pos': 0, 'neg': 0, 'neu': 0}
            if not flg:
                sent_dic[ts]['pos'] += 1
            elif flg == 1:
                sent_dic[ts]['neg'] += 1
            else:
                sent_dic[ts]['neu'] += 1
        else:
            if not flg:
                sent_dic[ts]['pos'] += 1
            elif flg == 1:
                sent_dic[ts]['neg'] += 1
            else:
                sent_dic[ts]['neu'] += 1

    print '\nSentiment Analysis by Dates:\n'
    print 'sentiment dict: ', sent_dic

    times = {}
    times['Date'] = []
    times['Pos'] = []
    times['Neg'] = []
    times['Neu'] = []
    for key in sent_dic.keys():
        times['Date'].append(key)
        times['Pos'].append(sent_dic[key]['pos'])
        times['Neg'].append(sent_dic[key]['neg'])
        times['Neu'].append(sent_dic[key]['neu'])
    pd.DataFrame(times).to_csv('SentimentCnt.csv')


    tweets.to_csv('data_frame.csv',sep='\t',encoding='utf-8')

    print 'by States: ', countFreq, '\n'

    geoRangeJ = [-124.848974, 24.396308]
    geoRangeW = [-66.885444, 49.384358]   
    res = []
    lenAll = len(locList)
    ite = 1
    for loc in locList:
        geolocator = ArcGIS()
        #geolocator = Nominatim()
        print 'Progess: ', ite, ' / ', lenAll
        ite += 1
        try:
            location = geolocator.geocode(loc) 
            if location is not None:
                if location.latitude >= geoRangeW[0] and location.latitude <= geoRangeW[1]:
                    if location.longitude >= geoRangeJ[0] and location.longitude <= geoRangeJ[1]:
                        res.append([location.latitude, location.longitude])
                        print 'Length of valid data: ', len(res)
            #time.sleep(5)
        except:
            print("Error: geocode failed on input %s"%(loc))
    print '\nGEO LOCATIONS: ', res
    X = np.array(res)
    Y = pd.DataFrame(X)
    Y.to_csv('coord.csv')
    #kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
    y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)
    #plt.subplot(221)
    plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    plt.title('Kmeans result for geo locations')
    plt.show()
    

    return countFreq, posFreq, negFreq, neuFreq


write_to_csv('./rawData.csv')