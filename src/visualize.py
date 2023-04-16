#!/usr/bin/env python3

# command line args
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items:
#    print(k,':',v)

items = sorted(counts[args.key].items(), key=lambda item: item[1], reverse=True)[:10]
keys = [item[0] for item in items]
values = [item[1] for item in items]

df = pd.DataFrame(dict(keys = list(keys),values = list(values)))
print(df)

df_sorted = df.sort_values('values')
# create the bar graph

fig, ax = plt.subplots()
ax.bar(keys, values, data = df_sorted)
if 'en' in keys:
    xlabel = 'Language'
    name = 'language'
else:
    xlabel = 'Country'
    name = 'country'

if str(args.key) == '#coronavirus':
    pngkey = '_' + str(args.key)[1:]
else:
    pngkey = '_chinese'

plt.xlabel(xlabel)
plt.ylabel('Times Mentioned in Tweets')
plt.savefig(name + pngkey + 'test.png')
