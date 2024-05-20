import os

from fastapi import FastAPI, File, Form, UploadFile
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tool import ITT
from ttstool import GoogleTrans

os.environ["TAVILY_API_KEY"] = "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"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDf287UeEDU_t6vwaHN1XN3R4eDLG_4LpM"

llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)


app = FastAPI()

@app.post("/process_image/")
async def process_image(image: UploadFile = File(...), text: str = Form(...)):
    image_bytes = await image.read()
    image_to_text = ITT(image_bytes=image_bytes)

    tools = [image_to_text]


    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/openai-functions-agent")

    agent = create_openai_functions_agent(llm, tools, prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke({"input": "Send query to 'image_to_text' tool: "+text})['output']

    google_trans_instance = GoogleTrans()
    google_trans_instance.run(query=result)
    return result
