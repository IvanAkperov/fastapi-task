from fastapi import FastAPI
import httpx


app = FastAPI()


async def fetch_user_data(user_id: int):
    async with httpx.AsyncClient() as client:
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    user_data = await fetch_user_data(user_id)
    return user_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
