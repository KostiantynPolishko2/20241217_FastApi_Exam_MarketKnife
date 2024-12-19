from fastapi import Form

# Custom OAuth2PasswordRequestForm
class CustomOAuth2PasswordRequestFormSchema:
    def __init__(
        self,
        username: str = Form(..., description="The user's username", min_length=5, max_length=10),
        password: str = Form(..., description="The user's password")
    ):
        self.username = username
        self.password = password