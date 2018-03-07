#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 演示csv读写

import csv
import time

# write stocks data as comma-separated values
writer = csv.writer(open('stock.csv', 'wb', buffering=0))
writer.writerows([
    ('GOOG', 'Google, Inc.', 505.24, 0.47, 0.09),
     ('YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22),
    ('CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.49)
])

# read stocks data, print status messages
stocks = csv.reader(open('stock.csv', 'rb'))
status_labels = {-1: 'down', 0:'unchanged', 1:'up'}
for ticker, name, price, change, pct in stocks:
    status = status_labels[cmp(float(change), 0.0)]
    print('%s is %s (%s%%)' %(name, status, pct))


def write_by_csv_lib(datas):
    start = time.time()
    writer = csv.writer(open('csv_lib.csv', 'wb'))
    writer.writerows(datas)
    print('write_by_csv_lib cost {0} seconds'.format(time.time()-start))


def write_by_file_lib(datas):
    start = time.time()
    with open('file_lib.csv', 'wb') as f:
        for data in datas:
            f.write('{0},{1}\n'.format(data[0], data[1]))
    print('write_by_file_lib cost {0} seconds'.format(time.time()-start))

if __name__ == '__main__':
    datas = [(x, x) for x in range(1000)]
    write_by_csv_lib(datas)
    write_by_file_lib(datas)
