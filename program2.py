import pandas as pd

def process_intermediate_data(intermediate_file, output_file):
    # データの読み込み
    df = pd.read_csv(intermediate_file)
    
    # 変化量の計算
    for col in A + B:
        df[f'{col}_change'] = df[col] - df[f'{col}_prev']
    
    # 総資産額で割る
    for col in A:
        df[f'{col}_ratio'] = df[col] / df['総資産額']
        df[f'{col}_prev_ratio'] = df[f'{col}_prev'] / df['総資産額']
        df[f'{col}_ratio_change'] = df[f'{col}_ratio'] - df[f'{col}_prev_ratio']
    
    # 売上高で割る
    for col in B:
        df[f'{col}_ratio'] = df[col] / df['売上高']
        df[f'{col}_prev_ratio'] = df[f'{col}_prev'] / df['売上高']
        df[f'{col}_ratio_change'] = df[f'{col}_ratio'] - df[f'{col}_prev_ratio']
    
    # 売上増加のダミー変数
    df['sales_increase_dummy'] = (df['売上高'] > df['売上高_prev']).astype(int)
    
    # CSVに出力
    df.to_csv(output_file, index=False) 