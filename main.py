word = input()
cipher = input()
s = 0
k = 0
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "abcdefghijklmnopqrstuvwxyz"
f = ""

for i in range(len(word)):
    if k > len(cipher)-1:
        k = 0
    s = cipher[k]
    k += 1

    if word[i] in a:
        for j in range(len(a)):
            if word[i] == a[j]:
                if j + a.find(s) > len(a):
                    f += a[len(a)-2-j+a.find(s)]
                else:
                    f += a[j+a.find(s)]
                    print(f)  
                break  

    elif word[i] in b:
        for n in range(len(b)):
            if word[i] == b[n]:
                if n + b.find(s) > len(b):
                    f += b[len(b)-2-n+b.find(s)]
                else:
                    f += b[n+b.find(s)]
                    print(f)  
                break    

    else:
        f += word[i]
print(f)