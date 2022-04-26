import random as rd
from PIL import Image
import requests
import numpy as np

D = [(0,3),(2,0),(0,4),(4,1)]

def distance2(a,b):
  dis = 0
  for i in range(len(a)):
    dis += (a[i]-b[i])**2
  return dis

def argminDistance(p,mu):
  id = -1
  mindis = 0
  for i in range(len(mu)):
    dis = distance2(p,mu[i])
    if id ==-1 or mindis>dis:
      mindis = dis
      id = i
  return id  

def mysum(a,b):
  s = [0]*len(a)
  for i in range(len(a)):
    s[i] = a[i]+b[i]
  return s

def kmean(D,k):
  n = len(D)
  # B1: chọn ngẫu nhiên k phần tử để làm tâm của k nhóm
  mu = rd.sample(D,k)
  C = [0]*n
  while True:
    cothaydoi = False
    # B2: phân nhóm theo nguyên tắc gần trọng tâm nhóm nào thì phân vào nhóm đó
    for i in range(n):
      c = argminDistance(D[i],mu)
      if (C[i]!=c):
        cothaydoi = True
      C[i] = c
    if not cothaydoi:
      break
    # B3: tính lại trọng tâm của k nhóm
    mu = [tuple([0]*len(mu[0]))]*len(mu)
    sl = [0]*len(mu)
    for i in range(n):
      mu[C[i]] = mysum(mu[C[i]],D[i]) 
      sl[C[i]] +=1
    for i in range(len(mu)):
      if sl[i] == 0:
        mu[i] = rd.choice(D)
      else:
        mu[i] = [x//sl[i] for x in mu[i]]
    # B4: quay lại buoc 2 nếu như có sự thay đổi
  return C,mu

print(D)
print(kmean(D,2))

# url = "https://baoninhbinh.org.vn//DATA/ARTICLES/2021/5/17/cuoc-dua-lot-vao-top-100-anh-dep-di-san-van-hoa-va-thien-7edf3.jpg"
# im = Image.open(requests.get(url, stream=True).raw)
# pix_val = list(im.getdata())

# print("start kmean")
# C,mu = kmean(rd.sample(pix_val,1000),16)
# #C,mu = kmean(pix_val,8)
# print("end kmean")
# new_pix_val = [None]*len(pix_val)
# for i in range(len(pix_val)):
#   new_pix_val[i] = mu[argminDistance(pix_val[i],mu)]


# data = np.reshape(new_pix_val,(im.size[1], im.size[0],3))
# data = np.array(data, dtype=np.uint8)
# new_image = Image.fromarray(data)
# new_image.save('new.jpg')