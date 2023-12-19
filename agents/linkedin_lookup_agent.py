from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from Tools.tools import get_profile_url


def linkedin_lookup_agent(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """"
    given the full name of {name_of_person} I want you to get me link to thier linkedin profile page.
    Your Answer should only contain a Url.
    """

    tools_for_agent = [
        Tool(
            name="Crawl google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the linkedin page url"
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"])

    linkedin_profile_url = agent.run(
        prompt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
