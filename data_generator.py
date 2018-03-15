import numpy as np
import csv
import random

def writeFile(data, row, columns, writer, counter, max_no):
    temp = np.array(data[1:])
    if (row[1] == 'No Finding' and counter['NoFinding'] < max_no) or sum(temp == 1) > 0:
        if random.randint(1, 20) > 17:
            if row[1] == 'No Finding':
                counter['NoFinding'] += 1
            else:
                if counter['Infiltration'] > counter['Effusion'] + 5 and temp[2] == 1:
                    return None
                if counter['Infiltration'] > counter['Atelectasis'] + 5 and temp[2] == 1:
                    return None
                if counter['Effusion'] > counter['Atelectasis'] + 5 and temp[1] == 1:
                    return None
                for i in range(len(temp)):
                    if temp[i] > 0:
                        counter[columns[i+1]] += 1
            writer.writerow(data)

def checkValid(counter, title):
    print(title + '========================')
    min = 10000
    max = 0
    for key, val in counter.iteritems():
        if val < min:
            min = val
        if val > max:
            max = val
        print('{}: {}'.format(key, val))
    return max - min <= 100

def transformFile(train_array, test_array, train_file_name, test_file_name):
    new_columns = ['FileName',
                   'Atelectasis',
                   'Effusion',
                   'Infiltration',
                   ]

    train_count = {'NoFinding': 0}
    test_count = {'NoFinding': 0}
    for col in new_columns[1:]:
        train_count[col] = 0
        test_count[col] = 0

    while(1):
        with open('./Data_Entry_2017.csv') as f:
            with open(train_file_name, "w+") as wf_train:
                with open(test_file_name, "w+") as wf_test:
                    writer_train = csv.writer(wf_train)
                    writer_test = csv.writer(wf_test)

                    writer_train.writerow(new_columns)
                    writer_test.writerow(new_columns)

                    lines = f.read().splitlines()
                    del lines[0]

                    for i in range(len(lines)):
                        data = []
                        row = lines[i].split(',')

                        data.append(row[0])
                        for col in new_columns[1:]:
                            if col in row[1]:
                                data.append(1)
                            else:
                                data.append(0)

                        if data[0] in test_array:
                            writeFile(data, row, new_columns, writer_test, test_count, 360)
                        else:
                            writeFile(data, row, new_columns, writer_train, train_count, 1100)

        if checkValid(train_count, 'train') and checkValid(test_count, 'test'):
            break
        else:
            train_count = dict.fromkeys(train_count, 0)
            test_count = dict.fromkeys(test_count, 0)

def getTxtContent(txt_file):
    with open(txt_file) as file:
        result = file.read().splitlines()
    return result


train_txt = getTxtContent('./train_val_list.txt')
test_txt = getTxtContent('./test_list.txt')

transformFile(train_txt, test_txt, './train.csv', './test.csv')

