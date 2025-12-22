#/tailwind
def CodelandUsernameValidation(strParam):

  if len(strParam)>=4 and len(strParam)<=25 and strParam[0].isalpha() and strParam[-1]!="_":
    flag = 1 #flag initiated
    for s in strParam[1:]:
      if s.isalnum() or s=="_":
        flag=1
        continue
      else:
        flag=0
        break
  else:
    flag=0
  if flag==0:
    return 'false'
  else:
    return 'true'

print(CodelandUsernameValidation(input()))
