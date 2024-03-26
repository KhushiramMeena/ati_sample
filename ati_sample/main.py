from fastapi import FastAPI
from codeguru_profiler_agent import Profiler

# Initialize FastAPI app
app = FastAPI()

# Start CodeGuru Profiler agent
if __name__ == "__main__":
    Profiler(profiling_group_name="ati_sample").start()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Define endpoints
@app.get("/")
async def read_root()
    return {"message": "Hello, World!"}

@app.get("/about")
async def read_about():
    return {"message": "This is the about page"}

@app.get("/ati_operation")
async def perform_ati_operation():
    # Perform some ATI operation
    return {"message": "ATI operation performed successfully"}

@app.get("/contact_ati")
async def contact_ati():
    # Provide contact information for ATI
    return {"email": "ati@example.com", "phone": "123-456-7890"}
