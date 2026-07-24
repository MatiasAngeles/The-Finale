import fastapi
import pydantic
import uvicorn

app = fastapi.FastAPI(title="Discord Bot Tracker API")

db_users = {}


class ActivityPayload(pydantic.BaseModel):
    username: str
    action_type: str


@app.get("/")
def read_root():
    """API Runner"""
    return {"status": "online", "message": "Its Running"}


@app.post("/users/{user_id}/activity")
def activity_user(user_id: str, payload: ActivityPayload):
    """Registers the user things."""
    if user_id not in db_users:
        db_users[user_id] = {
            "username": payload.username,
            "messages": 0,
            "commands": 0,
        }

    db_users[user_id]["username"] = payload.username

    if payload.action_type == "message":
        db_users[user_id]["messages"] += 1
    elif payload.action_type == "command":
        db_users[user_id]["commands"] += 1
    else:
        raise fastapi.HTTPException(
            status_code=400, detail="Invalid action_type provided"
        )

    return {
        "status": "success",
        "user_id": user_id,
        "data": db_users[user_id],
    }


@app.get("/users/{user_id}")
def user_data(user_id: str):
    """History of the user."""
    user = db_users.get(user_id)
    if not user:
        return {"name": "unknown", "messages": 0, "commands": 0}

    return user


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
