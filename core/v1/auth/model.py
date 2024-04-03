from core.v1.model import APIModel


class Token(APIModel):
    access_token: str
    token_type: str


class TokenData(APIModel):
    user_id: int
