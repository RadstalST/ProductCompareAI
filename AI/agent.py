from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

from AI.tools import Tools
from AI.prompt_template import prompt,plan_prompt,plan_features_compare,execute_features_compare,pros_cons_compare,consider_budget_prompt
from AI.prompt_template import title_prompt,introduction_prompt,vs_paragraph_prompt,plan_review_product


class Agent():
    def __init__(self,openai_api_key=None,gpt_model_str="gpt-3.5-turbo",max_iterations=10) -> None:

        self.tools = Tools().get_tools()
        self.llm = ChatOpenAI(temperature=0,model=gpt_model_str,openai_api_key=openai_api_key)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.llm_v2 = ChatOpenAI(temperature=0,model=gpt_model_str,openai_api_key=openai_api_key)
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

        self.review_agent = initialize_agent(
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            tools=self.tools,
            llm=self.llm_v2,
            verbose=True, # verbose option is for printing logs (only for development)
            max_iterations=max_iterations,
            prompt=plan_review_product,
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

        self.title_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="topic",
            prompt=title_prompt,
            output_key="title",
        )

        self.introduction_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="title",
            prompt=introduction_prompt,
            output_key="introduction",
        )

        self.vs_paragraph_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="topic",
            prompt=vs_paragraph_prompt,
            output_key="vs_paragraph",
        )

        self.procons_plan_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="input",
            prompt=pros_cons_compare,
            output_key="output",
        )

        self.consider_budget_chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            input_key="budget",
            prompt=consider_budget_prompt,
            output_key="output",
        )

    def execute(self,prompt,budget=0):
        #formulate plan
        # 1. generate plan based on input
        plan_result = self.plan_chain.run(input = prompt) #output is a string

        # 2. execute plan by agent
        search_plan = self.agent(plan_result) #output is a dict

        # 3. plan for features comparison
        features_compare_plan = self.features_agent(plan_result)

        features_table = self.compare_plan_chain.run(input = features_compare_plan["output"])
    
        # 4. Generate pro and cons
        procons_result = self.procons_plan_chain.run(input= features_compare_plan["output"])
        # 4. create catchy title
        title = self.title_chain.run(topic = prompt)

        # 5. create introduction paragraph
        introduction = self.introduction_chain.run(title = title)

        # 6. create comparison paragraph
        vs_paragraph = self.vs_paragraph_chain.run(topic = title)

        # 7. consider budget
        budget_result = self.consider_budget_chain.run(budget = budget)

        res = {
            "search_plan":search_plan,
            "plan_result":plan_result,
            "features_compare_plan":features_compare_plan,
            "features_table":features_table,
            "pro_cons":procons_result,
            "title":title,
            "introduction":introduction,
            "vs_paragraph":vs_paragraph,
            "budget_consider":budget_result
        }

        return res
    def review(self,prompt):
        review = self.review_agent(prompt)
        return review        


