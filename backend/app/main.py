from fastapi import FastAPI

app = FastAPI(title='Resumora')


@app.get('/health')
def health():
    return {'status': 'ok'}
