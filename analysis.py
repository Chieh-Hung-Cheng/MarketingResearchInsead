import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Insead_dataset_modified.xlsx', sheet_name='Data')
from collections import Counter

import re
import numpy as np
from scipy import stats

N = (919-1)/2 #459

def match(str, kw_lst):
    for i in kw_lst:
        if i in str: return True
    return False

def match_strlst(str_lst, kw_lst):
    for i in str_lst:
        if match(i, kw_lst):
            return True
    return False

def conf_itvl(data):
    return stats.norm.interval(alpha=0.95, loc=np.mean(data), scale=stats.sem(data))

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])


def question1():
    # Q3 first come to mind
    # Deifine keywords
    insead_kw = ['insead']
    hbs_kw = ['harvard', 'hbs', 'havard', 'harward', 'howard', 'harvoud', 'haverd', 'haward']
    wharton_kw = ['wharton', 'warton', 'wharthon']
    lbs_kw = ['lbs', 'london']
    ttl_kw = hbs_kw + wharton_kw + insead_kw + lbs_kw

    insead_cnt = 0
    hbs_cnt = 0
    wharton_cnt = 0
    lbs_cnt = 0
    q3col = df.loc[::2]['Q3'].str.lower()
    for name in q3col:
        if match(name, insead_kw): insead_cnt += 1
        if match(name, hbs_kw): hbs_cnt += 1
        if match(name, wharton_kw): wharton_cnt += 1
        if match(name, lbs_kw): lbs_cnt += 1

    print('Insead First Impression: {} out of {} = {:.2f}%'.format(insead_cnt, N, 100*insead_cnt/N))

    y = [insead_cnt, hbs_cnt, wharton_cnt, lbs_cnt]
    x = ['Insead', 'Harvard', 'Wharton', 'LBS']
    plt.bar(x, y)
    plt.bar_label(plt.bar(x, y))
    plt.xlabel('School')
    plt.ylabel('Recall Times')
    plt.title('First Impression Times Q3')
    plt.show()

    y_ratio = [insead_cnt / N, hbs_cnt / N, wharton_cnt / N, lbs_cnt / N]
    plt.xlabel('School')
    plt.ylabel('Recall Ratio')
    plt.title('First Impression Recall Ratio Q3')
    plt.bar(x, y_ratio)
    plt.bar_label(plt.bar(x, y_ratio))
    plt.show()

    # Q3, Q4: totaled 4 preferred schools
    q3q4cols = df.loc[::2][['Q3', 'Q4_1_TEXT', 'Q4_2_TEXT', 'Q4_3_TEXT']]

    insead_4_cnt=0
    hbs_4_cnt=0
    wharton_4_cnt=0
    lbs_4_cnt=0

    for idx, row in q3q4cols.iterrows():
        tmp_lst = []
        for key, val in row.items():
            if isinstance(val, str): tmp_lst.append(val.lower())
        if match_strlst(tmp_lst, insead_kw):
            insead_4_cnt += 1
        if match_strlst(tmp_lst, hbs_kw):
            hbs_4_cnt += 1
        if match_strlst(tmp_lst, wharton_kw):
            wharton_4_cnt += 1
        if match_strlst(tmp_lst, lbs_kw):
            lbs_4_cnt += 1

    y = [insead_4_cnt, hbs_4_cnt, wharton_4_cnt, lbs_4_cnt]
    x = ['Insead', 'Harvard', 'Wharton', 'LBS']
    plt.bar(x, y)
    plt.bar_label(plt.bar(x, y))
    plt.xlabel('School')
    plt.ylabel('Recall Times')
    plt.title('Top 4 MBA Recall Times Q3Q4')
    plt.show()

    y_ratio = [insead_4_cnt/N, hbs_4_cnt/N, wharton_4_cnt/N, lbs_4_cnt/N]
    plt.xlabel('School')
    plt.ylabel('Recall Ratio')
    plt.bar_label(plt.bar(x, y_ratio))
    plt.bar(x, y_ratio)
    plt.title('Top 4 MBA Recall Ratio Q3Q4')
    plt.show()

    # Q5
    q5cols = df.loc[::2][['Q5_1', 'Q5_2', 'Q5_3', 'Q5_4']]
    yname = ['Havard', 'LBS', 'Wharton', 'Insead']
    plt.plot(conf_itvl(q5cols['Q5_1']), (0, 0), 'ro-')
    plt.plot(conf_itvl(q5cols['Q5_2']), (1, 1), 'ro-')
    plt.plot(conf_itvl(q5cols['Q5_3']), (2, 2), 'ro-')
    plt.plot(conf_itvl(q5cols['Q5_4']), (3, 3), 'ro-')
    plt.yticks(range(4), yname)
    plt.title('95% interval of Preference in Q5')
    plt.show()
    print('Q5 t-test')
    print('t-test: insead, Harvard', stats.ttest_ind(q5cols['Q5_1'], q5cols['Q5_4']))
    print('t-test: insead, LBS', stats.ttest_ind(q5cols['Q5_2'], q5cols['Q5_4']))
    print('t-test: insead, Wharton', stats.ttest_ind(q5cols['Q5_3'], q5cols['Q5_4']))

    # Q15
    q15cols = df.loc[::2][['Q15_1', 'Q15_2', 'Q15_3', 'Q15_4']]
    yname = ['Havard', 'LBS', 'Wharton', 'Insead']
    plt.plot(conf_itvl(q15cols['Q15_1'].dropna()), (0, 0), 'ro-')
    plt.plot(conf_itvl(q15cols['Q15_2'].dropna()), (1, 1), 'ro-')
    plt.plot(conf_itvl(q15cols['Q15_3'].dropna()), (2, 2), 'ro-')
    plt.plot(conf_itvl(q15cols['Q15_4'].dropna()), (3, 3), 'ro-')
    plt.yticks(range(4), yname)
    plt.title('95% interval of Recommendation in Q15')
    plt.show()
    print('Q15 t-test')
    print('t-test: insead, Harvard', stats.ttest_ind(q15cols['Q15_1'].dropna(), q15cols['Q15_4'].dropna()))
    print('t-test: insead, LBS', stats.ttest_ind(q15cols['Q15_2'].dropna(), q15cols['Q15_4'].dropna()))
    print('t-test: insead, Wharton', stats.ttest_ind(q15cols['Q15_3'].dropna(), q15cols['Q15_4'].dropna()))

def question2():
    # Q17
    q17cols = df.iloc[:, [0, *range(71, 102, 1)]]
    # instance: insead(4) vs harvard(1)
    hbs_df = None
    insead_df = None

    for i in range(0, 2*int(N), 2):
        rows = q17cols.iloc[i:i+2, :]
        hbs_row = None
        insead_row = None
        if rows.iloc[0, 1] == 1 and rows.iloc[1, 1] == 4:
            hbs_row = rows.iloc[0, :]
            insead_row = rows.iloc[1, :]
            pass
        elif rows.iloc[0, 1] == 4 and rows.iloc[1, 1] == 1:
            insead_row = rows.iloc[0, :]
            hbs_row = rows.iloc[1, :]
        else: continue

        if hbs_df is None:
            hbs_df = hbs_row
        else:
            hbs_df = pd.concat([hbs_df, hbs_row], axis=1)
        if insead_df is None: insead_df = insead_row
        else:
            insead_df = pd.concat([insead_df, insead_row], axis=1)
    pass

def main():
    # question1()
    question2()


if __name__ == '__main__':
    main()
