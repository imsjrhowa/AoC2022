# AoC 2022 Day 19
# Challenge 1 = 
# Challenge 2 = 

import os
import sys

def read_input( fname, t=lambda x: x ):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        contents = f.read()
        lines = contents.strip().split('\n')
    return list(map(t, lines))

data = read_input('sminput.txt')

for l in data:
    l = l.split(". ")
    
    sub = l[0]
    sub = sub.split(": ")
    blueprint = sub[0]
    blueprint = blueprint.replace("Blueprint ","")
    ore = sub[1].replace("Each ore robot costs ","")
    ore = ore.replace(" ore","")
    clay = l[1].replace("Each clay robot costs ","")
    clay = clay.replace(" ore", "")
    obsid = l[2].replace("Each obsidian robot costs ","")
    obsid = obsid.replace(" ore and ", ",")
    obsid = obsid.replace(" clay", "")
    obsidianOre, obsidianClay = obsid.split(",")
    geode = l[3].replace("Each geode robot costs ","")
    geode = geode.replace(" ore and ", ",")
    geode = geode.replace(" obsidian.", "")
    geodeOre, geodeObsidian = geode.split(",")

    blueprint = int(blueprint)
    ore = int(ore)
    clay = int(clay)
    obsidianOre = int(obsidianOre)
    obsidianClay = int(obsidianClay)
    geodeOre = int(geodeOre)
    geodeObsidian = int(geodeObsidian)

    print(blueprint,ore,clay,obsidianOre,obsidianClay,geodeOre,geodeObsidian)