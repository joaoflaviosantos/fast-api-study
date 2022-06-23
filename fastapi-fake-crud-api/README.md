<h1 align="center">FAST API - FAKE TRACKS CRUD</h1>

### BugBytes
- [Blog Post](https://www.bugbytes.io/posts/creating-a-music-track-api-with-fastapi-in-python/)
- [Tutorial Video](https://www.youtube.com/watch?v=gV-EpY2TeQ0)

### 1 - Running the service:

#### Windows:

```python
pip install virtualenv

virtualenv venv

.\venv\Scripts\activate

pip install -r requeriments.txt

uvicorn main:app --reload
```

#### Linux:

```python
pip install virtualenv

virtualenv venv

. .\venv\bin\activate

pip install -r requeriments.txt

uvicorn main:app --reload
```

### 2 - Testing EndPoints:

#### Access on any browser:

> http://127.0.0.1:8000/docs
