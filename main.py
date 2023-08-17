from fastapi import FastAPI

app = FastAPI()

app.title = "Fast Api whit Data base"
app.description = "This is a very fancy project, with auto docs for the API and everything"
app.version = "0.0.1"



@app.get("/")
def read_root():
    return {"Hello": "World"}