# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fun(x):
    print(x.name1, x.amount)
    if x['name2'] == '1':
        return x.amount

    else:
        return 20




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # df = pd.DataFrame([0.14, 0.16, 0.20, 0.30, 0.80], index=['a', 'b', 'c', 'd', 'e'], columns=['xx'])
    # df.plot.pie(subplots=True)
    # plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    data = {'amount': [100, 200, 300, 400, 500],
            'name1': ['1', '2', '2', 'ooo4', 'ppp5'],
            'name2': ['1', '2', '0', 4, 5]}

    df = pd.DataFrame(data)

    # 杨航锋的方法
    # df1 = df.apply(lambda x: x['amount'] if x['name'] == 5 else 'd20', axis=1)
    # print(df1)

    # df1 = df.apply(lambda x: x.amount if x['name1'].contains('4') else 'd30', axis=1)
    # print(df1)
    df1 = df.apply(lambda x: x.amount if x['name1'].find('oo') >= 0 else 'd30', axis=1)
    print(df1)

    # df['x1'] = df.apply(fun, axis=1)
    #
    # print(df)

    df1 = df[df['name1'].str.contains('1') | df.name2.str.endswith('0')]
    print(df1)

    df1 = df[(df['name1'].str.contains('1')) | (df['amount'] == 300)]
    print(df1)

