#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world!!!")


# In[ ]:


money=True

if money


# In[23]:


no=0

while True:
    print(no)
    no=no+1
    
    if no>10:
        break


# In[11]:


no=1
sum=0

while no <= 100:
    if no % 3 == 0:
       sum = sum + no
       
    no = no + 1 # no +=1
        
        
print(sum)
        


# In[ ]:


# For 구문 


# In[14]:


for i in [1,2,3,4,5,6,7,8,9,10]:
  print(i)


# In[18]:


math=[80,90,70,70,100]

j=1
for i in math:
    if i>=90:
       print(j, "번째 학생은 합격입니다.")
    else:
        print(j, "번째 학생은 불합격입니다.")
    j +=1


# In[41]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i % 2 == 0:
        
        print(i) 


# In[42]:


for i in [1,2,3,4,5,6,7,8,9,10]:
     if i % 2 ! == 0:
        continue
        
           print(i)


# In[ ]:


# range 함수

# 숫자를 자동으로 생성해준다. for문과 함께 사용되는 경우가 아주 많다.


# In[ ]:


print(range(1,11))
range(1,11)


# In[40]:


for i in range(1,11): # 두번째 수는 미만
    print(i)


# In[56]:


# for문으로 구구단 출력하기(많이 쓰여서 외우기)

for i in range(2,10):     # i는 단을 표현
    for j in range(1,10):
        print(i*j, end="\t")
    print()


# In[57]:


for i in range(1,10):     # i는 단을 표현
    for j in range(2,10):
        print(i*j, end="\t")
    print()


# In[73]:


# range를 사용하여 100이하의 수중 짝수들만의 합계를 구하세요


# range(start,stop,step)

# for i in range(1,11): # start를 생략하면 0에서 시작
#      print(i)

for i in range(0,11,2): # stop을 생략하면 1씩 증가
    print(i)


# In[77]:


# 리스트 축약 / 내포 List Comprehension
# 리스트를 좀더 편리하고 직관적으로 만드는 방법이다.

list1=[1,2,3,4]

print(list1)

list2=[num      for num in list1]

print(list2)

list3=[num*2      for num in list1] # for에 있는거 하나씩 꺼내다가 앞에 num*2에 적용

print(list3)

list4=[num      for num in list1   if num%2==0] # for->if->num으로 던지기

print(list4)


# In[84]:


no=70

if no>=70: #(넘버)
    print("합격입니다")
else:
    print("불합격입니다")   # 여기까지가 제일 좋긴 하다! 밑에는 그냥 참고만! 비추!
    

print("합격입니다"     if no>=80    else "불합격입니다.")    

