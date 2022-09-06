# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:59:02 2022

@author: Saubhik
"""
'''
Number of best-of-5 set matches won
Number of best-of-3 set matches won
Number of sets won
Number of games won
Number of sets lost
Number of games lost

Zverev 3 0 10 104 11 106
Medvedev 1 2 11 106 10 104
Osaka 0 4 9 76 8 74
Barty 0 2 8 74 9 76
'''
# with open('test_scores.txt') as f:
#     table= f.readlines()
# table=[i.rstrip() for i in table]

data=input()
table=[]
while data:
    table.append(data.split('\n')[0])
    data=input()
players={}

for match in table:
    match=match.split(":")
    winner=match[0]
    loser=match[1]
    scores=match[2].split(',')
    tally={winner:{'set_w':0,'game_w':0,'set_l':0,'game_l':0},
           loser:{'set_w':0,'game_w':0,'set_l':0,'game_l':0}}
    for game in scores:
        if int(game.split('-')[0])-int(game.split('-')[1])>0:
            tally[winner]['set_w']+=1
            tally[loser]['set_l']-=1            
        else: 
            tally[loser]['set_w']+=1
            tally[winner]['set_l']-=1
        tally[winner]['game_w']+=int(game.split('-')[0])
        tally[winner]['game_l']-=int(game.split('-')[1])
        tally[loser]['game_l']-=int(game.split('-')[0])
        tally[loser]['game_w']+=int(game.split('-')[1])
            
    for keys in tally:
        if keys not in players.keys():
            players[keys]=[]
            if tally[keys]['set_w']>2:
                players[keys].append(1)
                players[keys].append(0)
            else:
                players[keys].append(0)
                if keys==winner:
                    players[keys].append(1)
                else:players[keys].append(0)
            players[keys][2:]=list(tally[keys].values())
        
        else:
            if tally[keys]['set_w']>2:
                players[keys][0]+=1
            elif tally[keys]['set_w']==2 and keys==winner:
                players[keys][1]+=1
            players[keys][2:]=[i+j for i,j in zip(list(tally[keys].values()),
                                                  list(players[keys][2:]))]
        
    
statlist = [(stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],name) for name in players.keys() for stat in [players[name]]]
statlist.sort(reverse = True)
for entry in statlist:
    print(entry[6],entry[0],entry[1],entry[2],entry[3], -entry[4], -entry[5])



