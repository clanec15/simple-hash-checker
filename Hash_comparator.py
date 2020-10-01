import os

print("Enter your file hash")
a=input()
print("The file hash you entered is",a,)
print("Enter the original hash")
b=input()
print("The hash you entered is",b,)

if a == b:
  print("Hash correct, the file isnt corrupted")
else:
    print("Hash mismatch, your file can be corrupted or it was tampered")
os.system('pause')
