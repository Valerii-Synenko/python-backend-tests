from typing import Annotated

from pydantic import BaseModel, Field


class RegisterUserResponseModel(BaseModel):
    """
    The model for register user response.
    The response has only one field - id.
    """

    id: Annotated[str, Field(min_length=24, max_length=24)]
