# -*- coding: utf-8 -*-
# Copyright 2020 FUJITSU SOFTWARE TECHNOLOGIES LIMITED.
# System: レセプト診断予測AI
# Date: 2020/6/30

import pandas as pd
import glob
import os

def split_by_month(input_path, output_path):
    """
    電子カルテファイルを、月毎のファイルに分割する。
    """
    karute = 'カルテ番号等'
    data_column_name = "_date"

    df = pd.read_csv(input_path, engine='python', encoding="cp932", dtype={karute: 'object'})

    # 月毎にぶんｋatu 
    for month in df[data_column_name].str[0:7].unique():

        # 出力パス
        out_path = output_path + '/カルテ_全結合_'+month.replace("/","")+'.csv'
        # 出力
        df[df[data_column_name].str.startswith(month)].to_csv(out_path, index=False, encoding='cp932')



if __name__ == "__main__":

    input_path = "カルテ_全結合.csv"
    output_path = "."

    result = split_by_month(input_path, output_path)
