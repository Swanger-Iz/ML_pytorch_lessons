# from pydantic import BaseModel, ConfigDict, Field

# class User(BaseModel):
#     name: str
#     email: str
#     age: int

# user = User(name="Alice", email="alice@example.com", age=30)

# class User(BaseModel):
#     tags: list[str] = []  # Safe in Pydantic - each instance gets its own list
    
    
# class StrictUser(BaseModel):
#     model_config = ConfigDict(strict=True)
#     name: str
#     age: int
    
# class UserProfile(BaseModel):
#     username: str = Field(min_length=3, max_length=20)
#     bio: str = Field(max_length=500)
#     website: str = Field(pattern=r"^https?://.*")    # pattern - Regular expression pattern to match

# # This will fail - no coercion allowed
# user = StrictUser(name="Alice", age="25")
# # ValidationError: Input should be a valid integer
    

# # Convert to dict
# user_dict = user.model_dump()
# print(user_dict)
# # {'name': 'Alice', 'email': 'alice@example.com', 'age': 30}

# # Convert to JSON string
# json_string = user.model_dump_json()
# print(json_string)
# # {"name":"Alice","email":"alice@example.com","age":30}

# # Data from an API response
# data = {"name": "Alice", "email": "alice@example.com", "age": 30}

# # Option 1: Unpack the dict (simple, common)
# user = User(**data)

# # Option 2: Use model_validate (explicit, more options)
# user = User.model_validate(data)





from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )

    # API Configuration
    api_key: SecretStr
    api_base_url: str = "https://api.example.com"
    request_timeout: int = Field(default=30, ge=1, le=300)

    # Database
    database_url: str
    max_connections: int = Field(default=10, ge=1, le=100)

    # Application
    debug: bool = False
    log_level: str = "INFO"

# Usage
settings = Settings()



print(f"API URL: {settings.api_base_url}")
print(f"Timeout: {settings.request_timeout}s")
print(f"Debug mode: {settings.debug}")