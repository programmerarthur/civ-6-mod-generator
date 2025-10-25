from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_models import ModRequest # <-- IMPORT OUR NEW MODEL

app = FastAPI(
    title="Civ 6 Mod Generator API",
    description="Generates the file structure for a Civ 6 Mod."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Default Vite port
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint to check API health."""
    return {"message": "Civ 6 Mod Generator API is running."}


@app.post("/api/generate-mod")
async def generate_mod(request: ModRequest):
    """
    The main endpoint.
    1. Receives the complete mod data from the frontend.
    2. Validates it using the ModRequest model.
    3. (Later) Passes this data to our generator engine.
    """
    
    # For now, we'll just return the data we received to prove it works.
    # We'll also see the server-generated 'mod_id'.
    print("Received mod request:", request.model_dump_json(indent=2))
    
    return request