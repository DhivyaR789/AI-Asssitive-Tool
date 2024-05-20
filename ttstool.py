
from typing import Dict, List, Optional, Type, Union

from googletrans import Translator
from gtts import gTTS
from langchain_core.callbacks import (AsyncCallbackManagerForToolRun,
                                      CallbackManagerForToolRun)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool


class GTTSInput(BaseModel):
    "Input for Google TTS"

    query: str = Field(description="input for text to speech")


class GoogleTrans():

    name: str = "google_translate"
    description: str = (
        "Tool that translates agent output to user's language"
        "Output is sent to user as speech"
        "Every output from agent should be sent to this tool"
    )
    max_results: int = 5
    args_schema: Type[BaseModel] = GTTSInput

    def trans_to_tamil(self, text):
        translator = Translator(service_urls=[
        'translate.google.com',
        ])
        translated = translator.translate(text, dest='ta')
        return translated.__dict__()["text"]

    def text_to_speech(self, text):
        tts = gTTS(text, lang='ta')
        tts.save('output.mp3')

    def run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> Union[List[Dict], str]:
        """Use the tool."""
        try:
            self.text_to_speech(self.trans_to_tamil(query))
            return "speech sent to user"
        except Exception as e:
            return repr(e)
