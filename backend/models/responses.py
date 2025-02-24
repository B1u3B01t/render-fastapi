from pydantic import BaseModel

class HtmlResponse(BaseModel):
    html_content: str