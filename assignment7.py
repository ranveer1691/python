##ASSIGNMENT-7

#Question-1

dic = {'girls':9,'boys':6,'choclate':20,'mango':15}
for i,j in dic.items():
    print(i)


#Question-2

student={'gabru':{'eng':37,'hindi':43,'Punjabi':99},'jatt':{'eng':33,'hindi':67,'Punjabi':97},'chobber':{'eng':19,'hindi':81,'Punjabi':100}}
x = (input("Name of student u want to know marks: "))

for k,v in student.items():
    if k==x:
        print(v)