from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

from AI.tools import Tools
from AI.prompt_template import prompt,plan_prompt


class Agent():
    def __init__(self,openai_api_key=None,gpt_model_str="gpt-3.5-turbo") -> None:

        self.tools = Tools().get_tools()
        self.llm = llm = ChatOpenAI(temperature=0,model=gpt_model_str,openai_api_key=openai_api_key)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        self.agent = initialize_agent(
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            tools=self.tools,
            llm=llm,
            verbose=True, # verbose option is for printing logs (only for development)
            max_iterations=10,
            prompt=prompt,
            memory=self.memory,
        )
        self.plan_chain = ConversationChain(
            llm=llm,
            memory=self.memory,
            input_key="input",
            prompt=plan_prompt,
            output_key="output",
        )

    def execute(self,prompt):
        #formulate plan
        plan_result = self.plan_chain.run(prompt)
        # Agent execution
        res = self.agent(plan_result)
        return res
