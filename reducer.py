#!/usr/bin/python
import sys


stat = {}
# get the keys and values
for line in sys.stdin:
    line = line.strip()
    pair, shot_raw = line.split('\t')
    a, b = shot_raw.split('m')
    shot = (int(a), int(b))
    # combaine them
    if pair not in stat.keys():
        stat[pair] = shot
    else:
        stat[pair] = tuple((stat[pair][0]+shot[0], stat[pair][1]+shot[1]))


dict_player = {}
for pair, shot in stat.items():
    # cut the pair into shooter and defender, and calculate the hit rate
    shooter, defender = pair.split('@')
    rate = int(shot[0])/int(shot[1])
    # store the (key: defender, value: hit rate) by shooter
    if shooter not in dict_player.keys():
        dict_player[shooter] = {defender: (rate, shot[1])}
    else:
        dict_player[shooter][defender] = (rate, shot[1])


# sort the data for each shooter
for player, records in dict_player.items():
    rate_rank = sorted(records.items(), key = lambda item:item[1][0])
    good_defender = []
    try:
        for record in rate_rank:
            if record[1][0] == 0.0:
                good_defender.append(record)
        shot_rank = sorted(good_defender, key = lambda item:item[1][1], reverse=True)
        print '%s\t%s' % (player, shot_rank[0]) # print the most unwanted defender for each shooter
    except:
        print '%s\t%s' % (player, rate_rank[0])  # print the most unwanted defender for each shooter

