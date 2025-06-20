설치방법

>pip install git+https://github.com/choimagon/ColorLog.git

사용방법
```
from colorlog import CP

CP().printc(a=1, b=2)
CP().printcb(color='r', msg="볼드 컬러 출력")
CP().printB(color='b', alert="중요", line=2)
```
