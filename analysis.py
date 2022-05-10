import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_excel('Insead_dataset_modified.xlsx', sheet_name='Data')
from collections import Counter

import re
import numpy as np
from scipy import stats
from factor_analyzer import FactorAnalyzer

import pingouin as pg




N = (919 - 1) / 2  # 459
name_id_dict = {'HBS': 1,
                'HEC': 2,
                'IESE': 3,
                'INSEAD': 4,
                'Kellogg': 5,
                'LBS': 6,
                'Stanford': 7,
                'Wharton': 8}


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


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


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

    print('Insead First Impression: {} out of {} = {:.2f}%'.format(insead_cnt, N, 100 * insead_cnt / N))

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

    insead_4_cnt = 0
    hbs_4_cnt = 0
    wharton_4_cnt = 0
    lbs_4_cnt = 0

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

    y_ratio = [insead_4_cnt / N, hbs_4_cnt / N, wharton_4_cnt / N, lbs_4_cnt / N]
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


def get_insead_competitor(q17cols, comp, save=False):
    # instance: insead(4) vs harvard(1)/ lbs(6) / wharton(8)
    comp_idxes = []
    insead_idxes = []
    for i in range(0, 2 * int(N), 2):
        rows = q17cols.iloc[i:i + 2, :]
        if rows.iloc[0, 1] == comp and rows.iloc[1, 1] == 4:
            comp_idxes.append(i)
            insead_idxes.append(i + 1)
        elif rows.iloc[0, 1] == 4 and rows.iloc[1, 1] == comp:
            insead_idxes.append(i)
            comp_idxes.append(i + 1)
        else:
            continue
    comp_rows = q17cols.iloc[comp_idxes]
    insead_rows = q17cols.iloc[insead_idxes]
    if save and comp == 1: q17cols.iloc[comp_idxes + insead_idxes].to_csv('havard_insead.csv')
    if save and comp == 6: q17cols.iloc[comp_idxes + insead_idxes].to_csv('lbs_insead.csv')
    if save and comp == 8: q17cols.iloc[comp_idxes + insead_idxes].to_csv('wharton_insead.csv')
    return comp_rows, insead_rows


def question2_deprec():
    # Q17
    q17cols = df.iloc[:, [0, *range(71, 102, 1)]]
    q17cols.to_csv('q17.csv')
    # instance: insead(4) vs harvard(1)/ lbs(6) / wharton(8)
    '''harvard_rows, insead_rows = get_insead_competitor(q17cols, 1, save=True)
    print(pg.cronbach_alpha(data=pd.concat([harvard_rows, insead_rows])[['Q17_9','Q17_11','Q17_15','Q17_21','Q17_24','Q17_28','Q17_29']]))
    print(pg.cronbach_alpha(data=pd.concat([harvard_rows, insead_rows])[['Q17_2', 'Q17_5', 'Q17_6', 'Q17_12', 'Q17_13', \
                                                                         'Q17_14', 'Q17_17', 'Q17_18', 'Q17_22', 'Q17_30']]))
    print(pg.cronbach_alpha(data=q17cols.loc[(df['SchoolRated'] == 8) | (df['SchoolRated'] == 6) | (df['SchoolRated'] == 4) | (df['SchoolRated'] == 1)][
        ['Q17_9', 'Q17_11', 'Q17_15', 'Q17_21', 'Q17_24', 'Q17_28', 'Q17_29']]))
    print(pg.cronbach_alpha(data=q17cols.loc[(df['SchoolRated'] == 8) | (df['SchoolRated'] == 6) | (df['SchoolRated'] == 4) | (df['SchoolRated'] == 1)][['Q17_2', 'Q17_5', 'Q17_6', 'Q17_12', 'Q17_13', \
                                                                         'Q17_14', 'Q17_17', 'Q17_18', 'Q17_22',
                                                                         'Q17_30']]))

    print(pg.cronbach_alpha(data=q17cols[['Q17_9', 'Q17_11', 'Q17_15', 'Q17_21', 'Q17_24', 'Q17_28', 'Q17_29']]))
    print(pg.cronbach_alpha(data=q17cols[['Q17_2', 'Q17_5', 'Q17_6', 'Q17_12', 'Q17_13', \
         'Q17_14', 'Q17_17', 'Q17_18', 'Q17_22',
         'Q17_30']]))
    # get_insead_competitor(q17cols, 6, save=True)
    # get_insead_competitor(q17cols, 8, save=True)

    # Create factor analysis object and perform factor analysis
    # fa = FactorAnalyzer(rotation='varimax')
    # fa.fit(q17cols.iloc[hbs_idxes+insead_idxes, 2:])
    # fa.get_eigenvalues()

    # interested = q17cols.loc[(df['SchoolRated'] == 8) | (df['SchoolRated'] == 6) | (df['SchoolRated'] == 4) | (df['SchoolRated'] == 1)]
    # interested.to_excel('interested.xlsx')
    # interested.to_csv('interested.csv')
    pass'''


def gen_ndim(*category_lst):
    q17cols = df.iloc[:, [0, *range(71, 102, 1)]]
    ret_vec_lst = []

    for category in category_lst:
        print(pg.cronbach_alpha(data=q17cols[category]))

    for name, idx in name_id_dict.items():
        vec = []
        rows = q17cols.loc[q17cols['SchoolRated'] == idx]
        for category in category_lst:
            cols = rows[category]
            avg_val = cols.mean(axis=1).mean(axis=0)
            vec.append(avg_val)
        ret_vec_lst.append(vec)
    return pd.DataFrame(ret_vec_lst, columns=['x', 'y', 'z', 'w'])

def plot2d(xs, ys, xl, yl):
    plt.scatter(xs, ys)
    plt.xlim(3.2, 4.5)
    plt.xlabel(xl)
    plt.ylim(3.2, 4.5)
    plt.ylabel(yl)
    for i, name in enumerate(name_id_dict):
        plt.annotate('{}({:.2f},{:.2f})'.format(name, xs[i], ys[i]), (xs[i], ys[i]))
    plt.show()

def question2():
    course = ['Q17_2', 'Q17_12', 'Q17_13', 'Q17_14', 'Q17_17', 'Q17_18', 'Q17_22']
    employ = ['Q17_4', 'Q17_8', 'Q17_15', 'Q17_28', 'Q17_29']
    ability = ['Q17_9', 'Q17_16', 'Q17_19', 'Q17_21', 'Q17_24']
    image = ['Q17_1', 'Q17_3', 'Q17_6', 'Q17_23', 'Q17_26']
    vecs = gen_ndim(course, employ, ability, image)

    plot2d(vecs.x, vecs.y, 'course', 'employ')
    plot2d(vecs.x, vecs.z, 'course', 'ability')
    plot2d(vecs.x, vecs.w, 'course', 'image')
    plot2d(vecs.y, vecs.z, 'employ', 'ability')
    plot2d(vecs.y, vecs.w, 'employ', 'image')
    plot2d(vecs.z, vecs.w, 'ability', 'image')

    '''
    cirr = ['Q17_2', 'Q17_5', 'Q17_6', 'Q17_12', 'Q17_13', 'Q17_14', 'Q17_17', 'Q17_18', 'Q17_22', 'Q17_30']
    ena = ['Q17_9', 'Q17_11', 'Q17_15', 'Q17_21', 'Q17_24', 'Q17_28', 'Q17_29']
    '''
def barplot(xs, ys, xl, yl, title):
    plt.bar(xs, ys)
    plt.bar_label(plt.bar(xs, ys))
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(title)
    plt.show()

def smr_plot(sr, min, max, xl, yl, title):
    xs = [*range(min, max+1, 1)]
    ys = []
    for i in xs:
        ys.append(len(sr[sr==i]))
    barplot(xs, ys, xl, yl, title)
    return xs, ys

def question3():
    know_insead = df.loc[df.Q22.notna()]
    N_know_insead = len(know_insead)
    print('Know Insead Ratio: {}'.format(len(know_insead)/ N))

    oneyear_adv = know_insead.loc[know_insead.Q26a.notna()]
    xs0, ys0 = smr_plot(oneyear_adv.Q26a, 1, 5, 'Q26a', 'Count', 'One Year MBA Positive Influence')
    oneyear_dev = know_insead.loc[know_insead.Q26b.notna()]
    xs1, ys1 = smr_plot(oneyear_dev.Q26b, 1, 3, 'Q26b', 'Count', 'One Year MBA Negative Influence')
    print('One year preference:{} vs. {}'.format(len(oneyear_adv)/len(know_insead), len(oneyear_dev)/len(know_insead)))
    # Error here
    barplot(xs0 + xs1, ys0+ys1, 'Q26','Count', 'One year MBA Influence')

    know_language = know_insead.loc[know_insead.Q22 == 1]
    print('Know Language Criteria Rate: {}'.format(len(know_language) / len(know_insead)))
    crit_adv = know_language[know_language.Q25A.notna()]
    xs2, ys2 =smr_plot(crit_adv.Q25A, 1, 5, 'Q25A', 'Count', 'Language Criteria Positive Influence')
    crit_dev = know_language[know_language.Q25B.notna()]
    xs3, ys3 =smr_plot(crit_dev.Q25B, 1, 3, 'Q25B', 'Count', 'Language Criteria Negative Influence')
    print('Language Cruteria preference:{} vs. {}'.format(len(crit_adv) / len(know_language), len(crit_dev) / len(know_language)))
    # Error here
    barplot(xs2 + xs3, ys2 + ys3, 'Q25','Count', 'Language Criteria Influence')

def add_factor_avg(df_prim, *categories):
    for i, category in enumerate(categories):
        df_prim[str(i)] = df_prim[category].mean(axis=1)
    df_prim.to_csv('insead_dataset_nodul_wtavg.csv')

def question5():
    df_prim = df.loc[::2]

    # df_prim.to_csv('insead_dataset_nodul.csv')

    career_names = ['Q6_2', 'Q6_3', 'Q6_4', 'Q7_1']
    ability_names = ['Q6_5', 'Q6_6', 'Q6_7']
    incentive_names = ['Q7_2', 'Q7_5', 'Q7_6']
    add_factor_avg(df_prim, career_names, ability_names, incentive_names)
    potential_mba = df_prim.loc[(df_prim['Q2b'] == 1) | (df_prim['Q2b'] == 2)]
    former_mba = df_prim.loc[(df_prim['Q2b'] == 3) | (df_prim['Q2b'] == 4)]

    col_idxes = [7,8, *range(112, 117, 1)]
    potential_cols = potential_mba.iloc[:, col_idxes]
    former_cols = former_mba.iloc[:, col_idxes]
    potential_cols.to_csv('potential_wtavg.csv')
    former_cols.to_csv('former_wtavg.csv')

    pass
def main():
    # question1()
    # question2()
    # question3()
    question5()
if __name__ == '__main__':
    main()
