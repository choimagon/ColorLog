# ColorLog 🖍️

간단하고 직관적인 **컬러 키-값 출력 유틸리티**입니다.  
`printc`, `printcb`, `printB` 메서드를 사용해 컬러 및 볼드 스타일로 로그를 출력할 수 있습니다.

---

## 📦 설치 방법

```bash
pip install git+https://github.com/choimagon/ColorLog.git

## 🚀 사용 방법

```python
from colorlog import CP

CP().printc(a=1, b=2)                          # 기본 컬러 출력
CP().printcb(color='r', msg="볼드 컬러 출력")   # 컬러 + 볼드 출력
CP().printB(color='b', alert="중요", line=2)    # 상자 형태의 강조 출력
```

---

## 🎨 지원 색상

컬러는 이름 또는 축약형으로 지정할 수 있습니다:

| 컬러 이름 | 축약형 |
|-----------|--------|
| `'red'`   | `'r'`  |
| `'green'` | `'g'`  |
| `'yellow'`| `'y'`  |
| `'blue'`  | `'b'`  |

> 컬러를 생략하면 기본값으로 **흰색(`white`)**이 사용됩니다.
