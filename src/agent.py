import os
from langchain.agents import AgentExecutor,Tool,create_react_agent
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
class WaferAgent:
    def __init__(self,toolkit):
        key=os.getenv("OPENAI_API_KEY")
        if not key: raise ValueError("OPENAI_API_KEY is not set")
        llm=ChatOpenAI(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),api_key=key,base_url=os.getenv("OPENAI_BASE_URL","https://api.openai.com/v1"),temperature=0)
        tools=[Tool(name="inspect_data",func=toolkit.inspect_data,description="Inspect loaded synthetic data."),Tool(name="optimal_clusters",func=toolkit.optimal_clusters,description="Find the best tested K-means cluster count."),Tool(name="apply_kmeans",func=toolkit.apply_kmeans,description="Apply K-means; input is cluster count."),Tool(name="analyze_clusters",func=toolkit.analyze_clusters,description="Summarize clusters after clustering.")]
        prompt=PromptTemplate.from_template("""You are a teaching assistant for synthetic wafer analytics. Use tools for computation and state that all data is synthetic.
Tools:
{tools}
Tool names: {tool_names}
Question: {input}
Thought: choose the next step
Action: one of [{tool_names}]
Action Input: input
Observation: result
Thought: evidence is sufficient
Final Answer: concise answer with assumptions
{agent_scratchpad}""")
        self.executor=AgentExecutor(agent=create_react_agent(llm,tools,prompt),tools=tools,verbose=False,handle_parsing_errors=True,max_iterations=8)
    def ask(self,q): return self.executor.invoke({"input":q})["output"]
