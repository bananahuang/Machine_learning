import numpy as np

def true_or_false(out,ans):
    if out == ans:
        return 'true'
    else:
        return 'false'
#讀檔
f = open('pla.dat','r')
line = f.read()
 #切割字串並轉成數字
inputs = line.split()
count = 0
k=np.array([])
for i in range(len(inputs)):
    inputs[i] = float(inputs[i])
    if i % 5 == 4:
        k= np.append(k,inputs[i])
        count =count+1
array_input = np.array(inputs)
#宣告初始權重
w = np.zeros(5)
#調整輸入numpy array 格式
true_input = np.resize(array_input,(400,5))
ans = np.resize(k,(400,1))
#讓x0為1，其餘四個input分別為x1-x4所以要平移
for k in range(400):
    true_input[k][4]=true_input[k][3]
    true_input[k][3]=true_input[k][2]
    true_input[k][2]=true_input[k][1]
    true_input[k][1]=true_input[k][0]
    true_input[k][0]=1
#開始訓練，訓練四次
for i in range(4):
    for j in range(400):
        output = np.sign(np.matmul(true_input[j],w))
        if output != ans[j]:
            if output > ans[j]:
                w = w - true_input[j]
            else:
                w = w + true_input[j]
#驗證答案
for ii in range(400):
    true_or_false(np.sign(np.matmul(true_input[ii],w)),ans[ii])
print(w)

        
    
    



