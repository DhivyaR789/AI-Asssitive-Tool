# """Tool for the Tavily search API."""

# from typing import Dict, List, Optional, Type, Union

# import google.generativeai as genai
# from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
# from langchain_core.callbacks import (AsyncCallbackManagerForToolRun,
#                                       CallbackManagerForToolRun)
# from langchain_core.pydantic_v1 import BaseModel, Field
# from langchain_core.tools import BaseTool

# genai.configure(api_key="AIzaSyBBt3dCe19y34ccc--_Gnq64bfqgRAggV0")

# class ImageCaption(BaseModel):
#     """Input for ITT Tool."""

#     query: str = Field(description="Input query to be answered from image.")


# class ITT(BaseTool):
#     """Tool that queries the Gemini for Image captioning"""

#     name: str = "image_to_text"
#     description: str = (
#         "A tool for captioning and conversing with image"
#     )
#     max_results: int = 5
#     args_schema: Type[BaseModel] = ImageCaption

#     def __init__(self, image_bytes):
#         image_bytes = image_bytes
#     def _run(
#         self,
#         query: str,
#         run_manager: Optional[CallbackManagerForToolRun] = None,
#     ) -> Union[List[Dict], str]:
#         """Use the tool."""
#         try:
#             # Set up the model
#             generation_config = {
#             "temperature": 0.4,
#             "top_p": 1,
#             "top_k": 32,
#             "max_output_tokens": 4096,
#             }

#             safety_settings = [
#             {
#                 "category": "HARM_CATEGORY_HARASSMENT",
#                 "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#             },
#             {
#                 "category": "HARM_CATEGORY_HATE_SPEECH",
#                 "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#             },
#             {
#                 "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#                 "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#             },
#             {
#                 "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#                 "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#             },
#             ]

#             model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
#                                         generation_config=generation_config,
#                                         safety_settings=safety_settings)

#             image_parts = [
#             {
#                 "mime_type": "image/png",
#                 "data": self.image_bytes
#             },
#             ]

#             prompt_parts = [
#             image_parts[0],
#             query,
#             ]

#             response = model.generate_content(prompt_parts)
#             return response.text
        
#         except Exception as e:
#             return repr(e)

from typing import Optional, Type, Union, Dict, List
import google.generativeai as genai
from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool

genai.configure(api_key="AIzaSyBBt3dCe19y34ccc--_Gnq64bfqgRAggV0")

class ImageCaption(BaseModel):
    query: str = Field(description="Input query to be answered from image.")

class ITT(BaseTool):
    name = "image_to_text"
    description = "A tool for captioning and conversing with image"
    args_schema: Type[BaseModel] = ImageCaption

    def __init__(self, image_bytes: bytes):
        self.image_bytes = image_bytes

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> Union[List[Dict], str]:
        try:
            generation_config = {
                "temperature": 0.4,
                "top_p": 1,
                "top_k": 32,
                "max_output_tokens": 4096,
            }

            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ]

            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro-vision-latest",
                generation_config=generation_config,
                safety_settings=safety_settings
            )

            image_parts = [{"mime_type": "image/png", "data": self.image_bytes}]

            prompt_parts = [image_parts[0], query]

            response = model.generate_content(prompt_parts)
            return response.text

        except Exception as e:
            return repr(e)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> Union[List[Dict], str]:
        raise NotImplementedError("ITT does not support async")
from typing import Optional, Type, Union, Dict, List
import google.generativeai as genai
from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool

genai.configure(api_key="AIzaSyBBt3dCe19y34ccc--_Gnq64bfqgRAggV0")

class ImageCaption(BaseModel):
    query: str = Field(description="Input query to be answered from image.")

class ITT(BaseTool):
    name = "image_to_text"
    description = "A tool for captioning and conversing with image"
    args_schema: Type[BaseModel] = ImageCaption
    image_bytes: bytes = None

    # def __init__(self, byte_val: bytes):
    #     self.image_bytes = byte_val

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> Union[List[Dict], str]:
        try:
            generation_config = {
                "temperature": 0.4,
                "top_p": 1,
                "top_k": 32,
                "max_output_tokens": 4096,
            }

            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ]

            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro-vision-latest",
                generation_config=generation_config,
                safety_settings=safety_settings
            )

            image_parts = [{"mime_type": "image/png", "data": self.image_bytes}]

            prompt_parts = [image_parts[0], query]

            response = model.generate_content(prompt_parts)
            return response.text

        except Exception as e:
            return repr(e)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> Union[List[Dict], str]:
        raise NotImplementedError("ITT does not support async")
