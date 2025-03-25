import pandas as pd

def process_financial_data(input_file, intermediate_file):
    # データの読み込み
    df = pd.read_csv(input_file)
    
    # 各通番の前年と次年のデータが存在する場合にのみのレコードにフィルタリング
    df['年度'] = df['年度'].astype(int)
    df_prev = df.copy()
    df_prev['年度'] += 1
    df_next = df.copy()
    df_next['年度'] -= 1
    
    # 前年と次年のデータが存在する通番を取得
    valid_ids = set(df['通番']).intersection(set(df_prev['通番'])).intersection(set(df_next['通番']))
    df = df[df['通番'].isin(valid_ids)]
    
    # 前年のデータをマージ
    df_prev = df_prev[['通番', '年度'] + A + B]
    df_prev.columns = ['通番', '年度'] + [f'{col}_prev' for col in A + B]
    df = df.merge(df_prev, on=['通番', '年度'], how='inner')
    
    # 必要なカラムのみを選択
    df = df[['通番', '年度', '月', '日'] + C + A + B + [f'{col}_prev' for col in A + B]]
    
    # CSVに出力
    df.to_csv(intermediate_file, index=False)