import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Insead_dataset_modified.xlsx', sheet_name='Data')
from collections import Counter

import re
import numpy as np
from scipy import stats

N = 919

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


def q1():
    # Q3 first come to mind
    # Deifine keywords
    insead_kw = ['insead']
    hbs_kw = ['harvard', 'hbs', 'havard', 'harward', 'howard', 'harvoud', 'haverd', 'haward']
    wharton_kw = ['wharton', 'warton', 'wharthon']
    lbs_kw = ['lbs', 'london']
    ttl_kw = hbs_kw + wharton_kw + insead_kw + lbs_kw

    q3col = df.loc[::2]

    ttl_mask = (df['Q3'].str.lower()).str.contains('harvard|hbs|wharton|insead|lbs|london', na=False)
    df_subset = df[ttl_mask]
    df_subset_complement = df[~ttl_mask]

    ctr = Counter(df['Q3'].str.lower())

    insead_count = 0
    hbs_count = 0
    wharton_count = 0
    lbs_count = 0
    cmpl_count = 0
    insead_ck = []
    hbs_ck = []
    wharton_ck = []
    lbs_ck = []
    cmpl_ck = []

    for name, times in ctr.most_common():
        if isinstance(name, float): continue
        flag = False

        for i in insead_kw:
            if i in name:
                insead_count += times
                insead_ck.append(name)
                flag = True
        for i in hbs_kw:
            if i in name:
                hbs_count += times
                hbs_ck.append(name)
                flag = True
        for i in wharton_kw:
            if i in name:
                wharton_count += times
                wharton_ck.append(name)
                flag = True
        for i in lbs_kw:
            if i in name:
                lbs_count += times
                lbs_ck.append(name)
                flag = True
        if not flag:
            cmpl_count += times
            cmpl_ck.append(name)

    print('Insead First Impression: {} out of {} = {:.2f}%'.format(insead_count, len(df), 100*insead_count/len(df)))
    # Perhaps not pie chart (some duplicate answers)
    labels = ['Insead', 'HBS', 'Wharton', 'LBS', 'others']
    sizes = [insead_count, hbs_count, wharton_count, lbs_count, cmpl_count]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    # Q3, Q4: totaled 4 preferred schools
    q3q4cols = df[['Q3', 'Q4_1_TEXT', 'Q4_2_TEXT', 'Q4_3_TEXT']]

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
    plt.xlabel('School')
    plt.ylabel('Recall Times')
    plt.show()

    y_ratio = [insead_4_cnt/N, hbs_4_cnt/N, wharton_4_cnt/N, lbs_4_cnt/N]
    plt.xlabel('School')
    plt.ylabel('Recall Ratio')
    plt.bar(x, y_ratio)
    plt.show()

    # Q5
    yname = ['Havard', 'LBS', 'Wharton', 'Insead']
    plt.plot(conf_itvl(df['Q5_1']), (0, 0), 'ro-')
    plt.plot(conf_itvl(df['Q5_2']), (1, 1), 'ro-')
    plt.plot(conf_itvl(df['Q5_3']), (2, 2), 'ro-')
    plt.plot(conf_itvl(df['Q5_4']), (3, 3), 'ro-')
    plt.yticks(range(4), yname)
    plt.title('95% interval of preference in Q5')
    plt.show()
    print('Q5 t-test')
    print('t-test: insead, Harvard', stats.ttest_ind(df['Q5_1'], df['Q5_4']))
    print('t-test: insead, LBS', stats.ttest_ind(df['Q5_2'], df['Q5_4']))
    print('t-test: insead, Wharton', stats.ttest_ind(df['Q5_3'], df['Q5_4']))

    # Q15
    yname = ['Havard', 'LBS', 'Wharton', 'Insead']
    plt.plot(conf_itvl(df['Q15_1'].dropna()), (0, 0), 'ro-')
    plt.plot(conf_itvl(df['Q15_2'].dropna()), (1, 1), 'ro-')
    plt.plot(conf_itvl(df['Q15_3'].dropna()), (2, 2), 'ro-')
    plt.plot(conf_itvl(df['Q15_4'].dropna()), (3, 3), 'ro-')
    plt.yticks(range(4), yname)
    plt.title('95% interval of Recommendation in Q15')
    plt.show()
    print('Q15 t-test')
    print('t-test: insead, Harvard', stats.ttest_ind(df['Q15_1'].dropna(), df['Q15_4'].dropna()))
    print('t-test: insead, LBS', stats.ttest_ind(df['Q15_2'].dropna(), df['Q15_4'].dropna()))
    print('t-test: insead, Wharton', stats.ttest_ind(df['Q15_3'].dropna(), df['Q15_4'].dropna()))
    pass



def main():
    q1()


if __name__ == '__main__':
    main()
