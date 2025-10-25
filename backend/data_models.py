from pydantic import BaseModel, Field
import uuid

# We use default_factory to generate unique IDs on the server
# This prevents the client from having to worry about it.
def generate_uuid_str():
    return str(uuid.uuid4())

class ModInfo(BaseModel):
    """Basic information about the mod itself."""
    mod_name: str = Field(..., description="The user-facing name of the mod.")
    mod_author: str = Field(..., description="The author's name.")
    mod_id: str = Field(default_factory=generate_uuid_str, description="The unique internal ID for the mod.")

class LocalizationText(BaseModel):
    """A container for all user-facing text that needs localization."""
    name: str
    description: str
    
class CivilizationInfo(BaseModel):
    """All data needed to create a new Civilization."""
    text: LocalizationText = Field(..., description="Name, description, etc.")
    # We will add unique units/buildings here later.
    
class LeaderAbilityInfo(BaseModel):
    """
    All data for the Leader's unique ability.
    For the MVP, this is just text. Later, it will be a complex object.
    """
    text: LocalizationText = Field(..., description="Name and description of the ability.")
    
class LeaderInfo(BaseModel):
    """All data needed to create a new Leader."""
    text: LocalizationText = Field(..., description="Leader's name and title.")
    agenda_text: LocalizationText = Field(..., description="Agenda name and description.")
    ability: LeaderAbilityInfo = Field(..., description="The leader's unique ability.")

class ModRequest(BaseModel):
    """
    This is the main "payload" object that our frontend will send
    to the backend. It contains everything needed to generate the mod.
    """
    info: ModInfo
    civilization: CivilizationInfo
    leader: LeaderInfo