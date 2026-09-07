form operators impot *
exec("p=True") # 어떠한 메모리를 변화시키는 구문
exec("q=False")
print ("When p is True and q is False,")
ret=eval("not p") # 논리 연산
print ("not p is {}".format(ret))
ret=eval("p and q")
print ("p and q is {}".format(ret))
ret=eval("p or q")
print ("p or q is {}".format(ret))
ret = eval("p xor q")
print ("p xor q is {}".format(ret)) #SyntaxError : 문법 이슈가 있다는 것
