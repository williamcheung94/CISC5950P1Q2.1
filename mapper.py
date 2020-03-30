#!/usr/bin/python
# --*-- coding:utf-8 --*--
import csv
import sys

reader = csv.reader(sys.stdin)

matched = {}


for row in reader:
    pair = str(row[19])+'@'+str(row[14]).replace(',', '').lower() # construct the "pair" as the key for Mapper
    result = row[13] # shot result
    if result == 'missed':
        shot = 0
    else:
        shot = 1
    if pair not in matched.keys():
        # construct a tuple (scored count, shot count) as the value
        matched[pair] = (shot, 1) #(1,1) or (0,1), means one scored in one shot / one missed in one shot 
    else:
        matched[pair] = (matched[pair][0]+shot, matched[pair][1]+1) # accumulate the score count and the shot count


for i in matched.items():
    print '%s\t%sm%s' % (i[0], i[1][0], i[1][1])

'''
# Column Number in the csv, as reference
0 GAME_ID
1 MATCHUP
2 LOCATION
3 W
4 FINAL_MARGIN
5 SHOT_NUMBER
6 PERIOD
7 GAME_CLOCK
8 SHOT_CLOCK
9 DRIBBLES
10 TOUCH_TIME
11 SHOT_DIST
12 PTS_TYPE
13 SHOT_RESULT
14 CLOSEST_DEFENDER
15 CLOSEST_DEFENDER_PLAYER_ID
16 CLOSE_DEF_DIST
17 FGM
18 PTS
19 player_name
20 player_id
'''
