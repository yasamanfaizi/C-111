import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv('studentMarks.csv')
avg = df['Math_score'].tolist()
fig = ff.create_distplot([avg],['avg'],show_hist=False)
#fig.show()

import random
import statistics
meanlist = []
for i in range(0,1000):
    data = []
    for h in range(0,100):
        idx = random.randint(0,len(avg)-1)
        value = avg[idx]
        data.append(value)
    mean = statistics.mean(data)
    meanlist.append(mean)
pm = statistics.mean(avg)
sm = statistics.mean(meanlist)
print(pm)
print(sm)
ps = statistics.stdev(avg)
ss = statistics.stdev(meanlist)
print(ps)
print(ss)
s1start, s1end = sm - ss, sm+ss
s2start, s2end = sm - (2*ss), sm+(2*ss)
s3start, s3end = sm - (3*ss), sm+(3*ss)

df1 = pd.read_csv('data1.csv')
avg1 = df1['Math_score'].tolist()
m1 = statistics.mean(avg1)

df2 = pd.read_csv('data2.csv')
avg2 = df2['Math_score'].tolist()
m2 = statistics.mean(avg2)

df3 = pd.read_csv('data3.csv')
avg3 = df3['Math_score'].tolist()
m3 = statistics.mean(avg3)


fig2 = ff.create_distplot([meanlist],['avg'],show_hist=False)

fig2.add_trace(go.Scatter(x = [sm, sm], y = [0,0.3],mode = 'lines', name = 'mean'))
fig2.add_trace(go.Scatter(x = [m1, m1], y = [0,0.3],mode = 'lines', name = 'mean1'))
fig2.add_trace(go.Scatter(x = [m2, m2], y = [0,0.3],mode = 'lines', name = 'mean2'))
fig2.add_trace(go.Scatter(x = [m3, m3], y = [0,0.3],mode = 'lines', name = 'mean3'))

fig2.add_trace(go.Scatter(x = [s1start, s1start], y = [0,0.3],mode = 'lines', name = 's1start'))
fig2.add_trace(go.Scatter(x = [s1end, s1end], y = [0,0.3],mode = 'lines', name = 's1end'))

fig2.add_trace(go.Scatter(x = [s2start, s2start], y = [0,0.3],mode = 'lines', name = 's2start'))
fig2.add_trace(go.Scatter(x = [s2end, s2end], y = [0,0.3],mode = 'lines', name = 's2end'))

fig2.add_trace(go.Scatter(x = [s3start, s3start], y = [0,0.3],mode = 'lines', name = 's3start'))
fig2.add_trace(go.Scatter(x = [s3end, s3end], y = [0,0.3],mode = 'lines', name = 's3end'))
fig2.show()

z1 = (m1-sm)/ss
z2 = (m2-sm)/ss
z3 = (m3-sm)/ss

print(z1)
print(z2)
print(z3)