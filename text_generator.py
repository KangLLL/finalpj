import pandas as pd


def generate_txt_csv(df_all, df, path):
    result = df_all.loc[df_all['Image Index'].isin(df['FileName'].values)]
    result = result.loc[:, ['Image Index', 'Follow-up #', 'Patient Age', 'Patient Gender']]
    result = result.rename(index=str,
                           columns={"Image Index": "FileName", "Follow-up #": "#", "Patient Age": "Age",
                                    "Patient Gender": "Gender"})
    result['Gender'] = result['Gender'].apply(lambda x: 1 if x == 'M' else 0)
    result.to_csv(path, index=False)


df_all = pd.read_csv('./Data_Entry_2017.csv')
df_train = pd.read_csv('./train.csv')
df_test = pd.read_csv('./test.csv')

generate_txt_csv(df_all, df_train, './train_text.csv')
generate_txt_csv(df_all, df_test, './test_text.csv')
