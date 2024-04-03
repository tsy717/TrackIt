# -- coding: utf-8 --
# @Time    : 2024/3/31 18:17
# @Author  : TangKai
# @Team    : ZheChengData

import pandas as pd


def cut_group(obj_list: list[object] = None, n: int = None) -> list[list[object]]:
    df = pd.DataFrame({'obj': obj_list})
    df['id'] = [i for i in range(1, len(df) + 1)]
    df['label'] = list(pd.cut(df['id'], bins=n, labels=[i for i in range(1, n + 1)]))
    return [df[df['label'] == i]['obj'].to_list() for i in range(1, n + 1)]


def cut_group_for_df(df:pd.DataFrame = None, n: int = None) -> list[pd.DataFrame]:
    df['id'] = [i for i in range(1, len(df) + 1)]
    df['label'] = list(pd.cut(df['id'], bins=n, labels=[i for i in range(1, n + 1)]))
    del df['id']
    return [df[df['label'] == i] for i in range(1, n + 1)]
