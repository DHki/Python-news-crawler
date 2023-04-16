## 청년인턴 하는 도중에.. 엄청난 엑셀 파일 중에서 다른 게 있다고 하셔서...
## 어디가 다른지 확인해야 하는데 수가 너무 많아 엄두가 나지 않음
## 그래서 파이썬으로 돌려서 확인해보기로 했지요
## 딱 그 파일들만을 위한 소스코드. (파일들은 내가 함부로 올릴 수 없기에..)
import pandas as pd

def get_dict(data, flag):
    dict_tmp = {}
        
    if flag == 1:
        for i in range (0, len(data.index)):
            tmp = str(data.loc[i, '본번'])
            tmp += '-'
            tmp += str(data.loc[i, '부번'])
            dict_tmp[tmp] = int(data.loc[i, '면적[㎡]'])
        
        dict_tmp = sorted(dict_tmp.items())
        return dict_tmp
    
    elif flag == 2:
        for i in range (0, len(data.index)):
            tmp = str(data.loc[i, '지 번'])
            if tmp[0] == '산':
               break
            dict_tmp[tmp] = int(data.loc[i, '면적(㎡)'])
    
        dict_tmp = sorted(dict_tmp.items())
        return dict_tmp


def main():
    data_1 = pd.read_excel('./2_2_1.xls')
    data_2 = pd.read_excel('./2_2_2.xlsx', skiprows = 5)
    
    dict_1 = get_dict(data_1, 1)
    dict_2 = get_dict(data_2, 2)

    for i in range (0, len(dict_1)):
        if dict_1[i][0] != dict_2[i][0]:
            print("diff at %s from 1, %s from 2, %d" % (dict_1[i][0], dict_2[i][0], i))
        else:
            if dict_1[i][1] != dict_2[i][1]:
                print("diff at %s from 1, %s from 2", dict_1[i][0], dict_2[i][0])

    print("finished")



if __name__ == '__main__':
    main()
