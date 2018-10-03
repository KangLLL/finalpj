import pandas as pd
import numpy as np

def generate_txt_csv(df_all, df, path):
    result = df_all.loc[df_all['Image Index'].isin(df['FileName'].values)]
    result = result.loc[:, ['Image Index', 'Follow-up #', 'Patient Age', 'Patient Gender']]
    result = result.rename(index=str,
                           columns={"Image Index": "FileName", "Follow-up #": "#", "Patient Age": "Age",
                                    "Patient Gender": "Gender"})
    for i in range(0, 100):
        result["#" + str(i)] = pd.Series(np.zeros(result.shape[0]), index=result.index)
        result["Age" + str(i)] = pd.Series(np.zeros(result.shape[0]), index=result.index)

    result['Gender'] = result['Gender'].apply(lambda x: 1 if x == 'M' else 0)

    for index, row in result.iterrows():
        if int(row['Age']) > 0 and int(row['Age']) < 100:
            row['Age' + str(row['Age'])] = 1
        else:
            row['Age' + '0'] = 1
    print(result)

    # result.to_csv(path, index=False)

    print(result['#'].unique())


df_all = pd.read_csv('./Data_Entry_2017.csv')
# df_train = pd.read_csv('./train.csv')
# df_test = pd.read_csv('./test.csv')

df_train = pd.read_csv('./Train_Label.csv')
df_test = pd.read_csv('./Test_Label.csv')

generate_txt_csv(df_all, df_train, './train_text.csv')
generate_txt_csv(df_all, df_test, './test_text.csv')


