# from flask import Flask
 
# app = Flask(__name__)
 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
 
# if __name__ == '__main__':
#     app.run(debug=True,
#             host="0.0.0.0")

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Christmas Greeting</title>
    <style>
        body {
            background-color: #e74c3c;  /* Christmas red color */
            color: #ffffff;  /* White text color */
            font-family: 'Arial', sans-serif;
            text-align: center;
            padding: 50px;
            margin: 0;
        }
    </style>
</head>
<body>
    <h1>Hello, World! Merry Christmas 🎄</h1>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=html_code)


# run code locally
import uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,
                host="0.0.0.0",
                # port=8000
                )