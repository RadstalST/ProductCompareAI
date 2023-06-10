from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

from AI.tools import Tools
from AI.prompt_template import prompt,plan_prompt,plan_features_compare,execute_features_compare


class Agent():
    def __init__(self,openai_api_key=None,gpt_model_str="gpt-3.5-turbo",max_iterations=10) -> None:

        self.tools = Tools().get_tools()
        self.llm = ChatOpenAI(temperature=0,model=gpt_model_str,openai_api_key=openai_api_key)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        # AGENTS
        self.agent = initialize_agent(
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            tools=self.tools,
            llm=self.llm,
            verbose=True, # verbose option is for printing logs (only for development)
            max_iterations=max_iterations,
            prompt=plan_prompt,
            memory=self.memory,
        )

        # for features comparison plan execution
        self.features_agent = initialize_agent(
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            tools=self.tools,
            llm=self.llm,
            verbose=True, # verbose option is for printing logs (only for development)
            max_iterations=max_iterations,
            prompt=plan_features_compare,
            memory=self.memory,
        )

        # prompt

        self.plan_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="input",
            prompt=prompt,
            output_key="output",
        )

        self.compare_plan_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="input",
            prompt=execute_features_compare,
            output_key="output",
        )

    def execute(self,prompt):
        #formulate plan
        # 1. generate plan based on input
        plan_result = self.plan_chain.run(input = prompt) #output is a string

        # 2. execute plan by agent
        search_plan = self.agent(plan_result) #output is a dict

        # 3. plan for features comparison
        features_compare_plan = self.features_agent(plan_result)

        features_table = self.compare_plan_chain.run(input = features_compare_plan["output"])


        res = {
            "search_plan":plan_result,
            "features_compare_plan":features_compare_plan,
            "features_table":features_table
        }

        return res
