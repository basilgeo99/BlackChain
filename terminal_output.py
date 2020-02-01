import os

pipe = os.popen("sh test.sh")
output = pipe.read()
print(output)

pipe = os.popen("echo $?")
output = pipe.read()
print(output)
