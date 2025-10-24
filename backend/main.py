from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Civ 6 Mod Generator API",
    description="Generates the file structure for a Civ 6 Mod."
)

# This is CRITICAL. It allows our React frontend (on a different port)
# to make requests to this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # The default Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint to check API health."""
    return {"message": "Civ 6 Mod Generator API is running."}