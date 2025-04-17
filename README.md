# chosun_fastapi_ws
FastAPI Web Server for CloudComputing &amp; Visualization  
Date : 2025.04.10
## 1. Python 개발환경 구축
- python3 -m venv venv
- ./venv/bin/activate (venv 가상환경 접속)
- pip install -r requirement.txt (venv 가상환경에 라이브러리 설치, 한 줄씩 읽어와서 설치해줌))
- pip list (가상환경 라이브러리 목록)
- ^+shift+p : Select Interpreter -> /venv/python 선택

## 2. 형상관리도구(Github)
  1) 로컬(노트북)
     - `git init` :: Create a git project
     - Create the repository on github
     - `git remote -v` :: Check the connection status of github remote
     - `git status` :: Managing the version state of the git
     - `git add [filename]` :: Tracking file
     - `git add .` :: Tracking all file
     - `git commit -m "version 1.0"` :: Create local version
      - `git push origin main` :: Upload the versions I made to the global main branch
  2) 글로벌(Github)

## 숙제
- 소스코드 확대 모드
- 주석 색깔 바꿔오기
- git 연결 해오기
- 테마 바꿔오기 -> 아이콘, 개발툴
- 거꾸로 해보기(이미 내용이 존재하는 디렉토리를 깃으로 관리하는 방법)
  - 집에서 VSC 폴더 생성
  - 개발 코드
  - git으로 관리 git init
  - github에서 텅 빈 repository 생성
  - vscode 폴더와 repository를 remote로 연결
  - push 해보기

## main.py 작성

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return "Hello, FastAPI!"
```

## FastAPI 서버 띄우기
1. `uvicorn main:app -reload`
2. 소스코드 추가
```py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
```

Master가 차별적인 발언이라고 해서 바뀐것임
Master -> main 으로 바꾸는 중임
우리가 로컬에서 이미 만들고 git을 연동하면 Master 브랜치가 되고 깃허브에서 시작함녀 main 브랜치가 된다
