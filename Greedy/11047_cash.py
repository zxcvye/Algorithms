N, K = map(int, input().split())
a=[]
val=0

for i in range(N):
  a.append(int(input()))

a.sort(reverse=True)

for i in a:
  val=val+K//i
  K=K%i
  if(K==0):
      break

print(val)