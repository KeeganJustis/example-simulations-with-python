#%% 
from pandas import read_html
from modsim import *
from numpy import abs,mean,max

from os.path import basename, exists

def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)

download('https://raw.githubusercontent.com/AllenDowney/' +
         'ModSimPy/master/data/World_population_estimates.html')

filename = "World_population_estimates.html"

tables = read_html(filename,header=0,index_col=0,decimal="M")

tables2 =tables[2]

# print(tables2.head())

tables2.columns = ['census','prb','un','maddison','hyde','tanton','biraben','mj','thomlinson','durand','clark']

census = tables2.census / 1e9

print(census.tail())

un = tables2.un / 1e9

print(un.tail())

def plot_estimates(table, label):
    census.plot(label='US Census',style=':',color='black')
    un.plot(label='UN DESA',style='--',color='gray')

    decorate(xlabel='Year',
             ylabel='World population (billion)',
             title='Estimated world population')

plot_estimates(census, 'US Census')
plot_estimates(un, 'UN DESA')

# %%

abs_error = abs(un - census)

print(abs_error.tail())

# %%
mean_abs_error = abs_error.mean()

print(mean_abs_error)

# %%
max_abs_error = abs_error.max()

print(max_abs_error)

# %%

rel_error = 100* abs_error / census

print(rel_error.tail())

print(mean(rel_error))
# %%

total_growth = census[2016] - census[1950]

print(total_growth)

# %%
t_0 = census.index[0]

t_end = census.index[-1]

elapsed_time = t_end - t_0

print(elapsed_time)

# %%

p_0 = census[t_0]

p_end = census[t_end]

total_growth = p_end - p_0

print(total_growth)

annual_growth = total_growth / elapsed_time

print(annual_growth)

# %%

results = TimeSeries()

results[t_0] = p_0

print(t_0)
print(t_end)

show(results)
# %%
for t in range(t_0,t_end):
    results[t+1] = results[t] +  annual_growth

results.plot(label='model',color='gray')

plot_estimates(results, 'Proportional model')

decorate(title="Constant growth model")
# %%
#5.1

t_0 = census.index[20]
print(t_0)
t_end = census.index[-1]

p_0 = census[t_0]


p_end = census[t_end]
print(p_end)


elapsed_time = t_end - t_0

print(elapsed_time)



p_0 = census[t_0]
print(p_0)
p_end = census[t_end]

total_growth = p_end - p_0

print(total_growth)

annual_growth = total_growth / elapsed_time

print(annual_growth)



results_2 = TimeSeries()

results_2[t_0] = p_0

print(t_0)
print(t_end)

show(results)

for t in range(t_0,t_end):
    results_2[t+1] = results_2[t] +  annual_growth

results_2.plot(label='model',color='gray')

plot_estimates(results_2, 'Proportional model')

decorate(title="Constant growth model")
# %%
