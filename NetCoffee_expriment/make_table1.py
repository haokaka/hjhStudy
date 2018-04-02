#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:38:08 2018

@author: hjh
"""

import Consistency
import Coverage
import matplotlib.pyplot as plt
import numpy as np

isoRank_cov = [0.08109, 0.06740, 0.05597, 0.0723 , 0.1250, 0.1595 , 0.0975, 0.1097]
isoRank_ME = [1.1506, 1.0718, 1.1811, 1.2083, 1.0933, 1.0700, 1.1994, 1.2089]
isoRank_NME = [0.5804, 0.5985, 0.5399, 0.6061, 0.5846, 0.5666, 0.6068, 0.5842]

NetCoffee_cov = [0.3624, 0.3237, 0.3454, 0.4255, 0, 0, 0.3442, 0.3355]
NetCoffee_ME = [0.9900, 0.8540, 1.0508, 1.0028, 0, 0, 1.0743, 1.1708]
NetCoffee_NME = [0.5496, 0.5413, 0.5360, 0.5554, 0, 0, 0.5890, 0.5739]

multiMAG_cov = [0.8305, 0.8503, 0.5613, 0.7283, 0.4952, 0.5022, 0.8731, 0.7897]
multiMAG_ME = [0.9157, 0.9325, 0.9853, 1.0094, 0.9440, 0.9417, 1.1616, 1.1884]
multiMAG_NME = [0.5355, 0.5803, 0.5258, 0.5709, 0.5516, 0.5478, 0.6309, 0.5902]

path = '/home/hjh/桌面/workshop/my_study/NetCoffee2/testdata'

def make_table(dataset, evalue, alpha):
    ali_path = path + '/dataset%s/evalue%s/alpha%s/Result.ali' %(dataset, evalue, alpha)
    net_path = path + '/dataset%s/dataset%s_nets.txt' %(dataset, dataset)
    go_path = path + '/result_validate/go_dick.txt'
    
    print('dataset:%s, evalue:%s, alpha:%s' % (dataset, evalue, alpha))
    _coverage = Coverage.coverage(ali_path, net_path)
    _ME = Consistency.mean_entropy(go_path, ali_path)
    _NME = Consistency.normalized_mean_ent(go_path, ali_path)
    
    return _coverage, _ME, _NME

    
make_table(1, '1.0000000', '.1')

dataset = [1, 2, 3, 4, 5, 6, 7, 8]
evalue = ['1.0000000', '.1000000', '.0100000', '.0010000',
          '.0001000', '.0000100', '.0000010', '.0000001']
alpha = ['.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9']

coverage_1_05 = []
ME_1_05 = []
NME_1_05 = []
for each in dataset:
    res = make_table(each, '.0010000', '.6')
    coverage_1_05.append(res[0])
    ME_1_05.append(res[1])
    NME_1_05.append(res[2])
    
iso_width = 0.2
net_width = -0.2
mag_width = 0.2
net2_width = -0.2

ind1 = np.arange(8)
ind2 = ind1 + 0.4   # the x locations for the groups

ax1 = plt.subplot(311)
p1 = plt.bar(ind1, isoRank_cov, iso_width, align='edge')
p2 = plt.bar(ind1, NetCoffee_cov, net_width, align='edge')
p3 = plt.bar(ind2, multiMAG_cov, mag_width, align='edge')
p4 = plt.bar(ind2, coverage_1_05, net2_width, align='edge')

plt.ylabel('coverage')
plt.title('Coverage in four algorithms')
#plt.xticks(ind1, ['dataset1', 'dataset2', 'dataset3', 'dataset4', 'dataset5',
#          'dataset6', 'dataset7', 'dataset8'])

plt.xticks(ind1, ['1', '2', '3', '4', '5', '6', '7', '8'])
plt.yticks(np.arange(0, 1, 0.1))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('isoRank', 'NetCoffee', 'multiMAGNA++', 'NetCoffee2'))
# ('isoRank', 'NetCoffee', 'multiMAGNA++', 'NetCoffee2')

ax2 = plt.subplot(312, sharex = ax1)
p1 = plt.bar(ind1, isoRank_ME, iso_width, align='edge')
p2 = plt.bar(ind1, NetCoffee_ME, net_width, align='edge')
p3 = plt.bar(ind2, multiMAG_ME, mag_width, align='edge')
p4 = plt.bar(ind2, ME_1_05, net2_width, align='edge')

plt.ylabel('ME')
plt.title('ME in four algorithms')
# plt.xticks(ind1, ['dataset1', 'dataset2', 'dataset3', 'dataset4', 'dataset5',
#          'dataset6', 'dataset7', 'dataset8'])
plt.yticks(np.arange(0, 1, 0.1))
plt.legend((p1[0], p2[0], p3[0], p4[0]),('isoRank', 'NetCoffee', 'multiMAGNA++', 'NetCoffee2'))


ax3 = plt.subplot(313, sharex = ax1)
p1 = plt.bar(ind1, isoRank_NME, iso_width, align='edge')
p2 = plt.bar(ind1, NetCoffee_NME, net_width, align='edge')
p3 = plt.bar(ind2, multiMAG_NME, mag_width, align='edge')
p4 = plt.bar(ind2, NME_1_05, net2_width, align='edge')

plt.ylabel('ME')
plt.title('ME in four algorithms')
plt.yticks(np.arange(0, 1, 0.1))
plt.legend((p1[0], p2[0], p3[0], p4[0]),('isoRank', 'NetCoffee', 'multiMAGNA++', 'NetCoffee2'))



plt.show()
plt.savefig('e001_a06.png')