from pydantic import BaseModel, HttpUrl

class HtmlFetchRequest(BaseModel):
    url: HttpUrl

class CritRequest(BaseModel):
    name: str
    url: HttpUrl