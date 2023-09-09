import os



target_file_path=r"D:\code\py\尝试3-图片图片匹配\data\map1"
file_name_list=os.listdir(target_file_path)
dict={}
f=open("target.txt",'r')
source=f.read().split('\n')
source_list=source[:len(source)-1]
dit={}
index_list=[]
for i in source_list:
    a,b=i.split(':')
    dit[a]=b
    index_list.append(b)
    print(a,b)
res_dict={}
for i,j in enumerate(file_name_list):
    # print("index+{}，name+{}".format(i,j))
    # if i==340:
    #     print(j+"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    res_dict[i-5]=j
# print(res_dict)

ff=open("res_target",'w')
for i in dit.keys():
    tmp=res_dict[int(dit[i])]
    print(i,tmp)
    ff.write(str(i+" "+tmp+"\n"))
