from core.v1.model import APIModel


class Token(APIModel):
    access_token: str
    token_type: str


class TokenData(APIModel):
    username: str | None = None
    scopes: list[str] = []
