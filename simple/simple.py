s ="QllB^pvCloQebCfopqCi^d"
flag = ""
for i in range(len(s)):
	flag += chr(ord(s[i]) + 3)
print(flag)