# File: main.py
# Aim: Load schedule and visualize

# %%
import matplotlib.pyplot as plt
import pandas as pd
import random

from pprint import pprint
from color_convert import hsv2rgb

# %%


class Color(object):
    def __init__(self):
        self.default_value = 0.8
        self.default_saturation = 0.7

    def generate(self, hue=0, value=None, saturation=None):
        if value is None:
            value = self.default_value
        if saturation is None:
            saturation = self.default_saturation

        h, s, v = hue, saturation, value
        r, g, b = hsv2rgb(h, s, v)

        c = '#'
        for e in [r, g, b]:
            s = hex(e).replace('x', '')[-2:]
            c += s
        return c


def parse_clock(string):
    start, stop = string.split('-')
    return [float(e.replace(':', '.')) for e in [start, stop]]


class Uniques(object):
    def __init__(self):
        self.locations = dict()
        self.num_loc = 0
        self.dates = dict()
        self.num_date = 0

    def new_loc(self, name):
        if name not in self.locations:
            self.locations[name] = self.num_loc
            self.num_loc += 1

    def new_date(self, name):
        if name not in self.dates:
            self.dates[name] = self.num_date
            self.num_date += 1

    def display(self):
        print('-------------------------------')
        print('Locations: ')
        pprint(self.locations)
        print('Dates: ')
        pprint(self.dates)
        print()


# %%
# Settings
URL = 'http://chinavis.org/2020/program.html'

# %%
# Fetch schedule from [URL]

raw_tables = pd.read_html(URL)
tables = [e.copy() for e in raw_tables]

for table in tables:
    date = table.columns[0]
    table.columns = ['Clock', 'Subject', 'Location']
    print(date)
    table['Date'] = date
    table.dropna(axis=0, inplace=True)
    # table = table.loc[pd.notna(table['Clock'])]
    display(table)

table = pd.concat(tables)
table.index = range(len(table))
table.to_json('table.json')
print('-----------------------------------')
display(table)

# Walk through
# %%
uniques = Uniques()
color = Color()

for loc in table.Location:
    uniques.new_loc(loc)

num = uniques.num_loc
for loc in uniques.locations:
    x = uniques.locations[loc]
    hue = x / num * 360
    print(x, x/num * 360)
    uniques.locations[loc] = color.generate(hue)

for date in table.Date:
    uniques.new_date(date)

uniques.display()

# %%
plt.style.use('ggplot')
font = {
    'family': 'SimHei',
    'weight': 'bold'
}
plt.rc('font', **font)
fig, axes = plt.subplots(uniques.num_date + 1, 1, figsize=(14, 20))
for ax in axes:
    ax.y_offset = 1

for j in range(len(table)):
    se = table.iloc[j]
    start, stop = parse_clock(se.Clock)
    subject = se.Subject
    loc = se.Location
    date = se.Date

    ax = axes[uniques.dates[date]]
    color = uniques.locations[loc]
    ax.set_title(date)

    y = ax.y_offset
    ax.plot([start, stop], [y, y], c=color, label=loc)
    ax.text(21, y, subject, c=color)
    ax.y_offset += 1

for ax in axes:
    ax.set_xlim(8, 21)

ax = axes[-1]
ax.set_title('Location label')

for loc in uniques.locations:
    color = uniques.locations[loc]
    y = ax.y_offset
    ax.plot([8, 20], [y, y], c=color)
    ax.text(21, y, loc, c=color)
    ax.y_offset += 1

fig.tight_layout()

# %%
