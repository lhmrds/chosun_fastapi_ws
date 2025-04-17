from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return "Hello, FastAPI!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", 
                reload=True, # 코드 변경 시 자동으로 서버 재시작
                host="0.0.0.0", # 모든 IP에서 접근 가능
                port=8000) # 포트번호