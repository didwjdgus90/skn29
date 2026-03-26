# 자료구조 : 리스트 튜플 세트 딕셔너리
# 사원관리 : 데이터는 주어질때
# {
#    'name' : '홍길동',
#    'pay' : 100000,
#    'status' : '관리자',
# }

# 1. 3명의 사원정보를 리스트에 저장해서 변수로 관리
stafe = [
   {
    'name' : '홍길동',
    'pay' : 100000,
    'status' : '관리자', 
   },
   {
    'name' : '김길동',
    'pay' : 90000,
    'status' : '대리', 
   },
   {
    'name' : '양길동',
    'pay' : 70000,
    'status' : '사원', 
   } 
]
print(stafe)

# 2. pay가 가장 큰 사원 이름을 출력
# pays = max(stafe, key=lambda x: x['pay'])['name']
# print(pays)
pays = [ i['pay'] for i in stafe]
pays.sort(reverse=True)

max_pay = pays[0]

for i in stafe:
    if i['pay'] == max_pay :
        print(i['name'])


# max_pay = max(i['pay'] for i in stafe)

# for i in stafe:
#  if i['pay'] == max_pay:
#    print(f"이름 : {i['name']}")

# import random
# a = [random.randint(1,15) for i in range(10) ]
# b = [random.randint(1,15) for i in range(10) ]

# 3. 임의 집합 두개를 만들어서 교집합 합집합 차집합
# 각 집합중 가장 큰 값과 작은 값을 찾아서 출력
import random
a = {random.randint(1,15) for i in range(10)}
b = {random.randint(1,15) for i in range(10)}

print (a.union(b))
print (a.intersection(b))
print (a.difference(b))

ab = a.union(b)

print("최댓값 :",max(ab),"최솟값 : ", min(ab))