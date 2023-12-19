import streamlit as st
from agents.linkedin_lookup_agent import linkedin_lookup_agent
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv
load_dotenv()


st.title("Linkedin Ice Breaker")

information = """"
AI || ML || Sass Tooling || Chrome extension || Nodejs || React || Full Stack Senior Engineer


I am a software engineer and Backend developer with experience in various technologies such as JavaScript, Solidity, Smart Contracts, Blockchain, Web3, TypeScript, Node, Express, Mongo, React, Redux, Git, OOP, jQuery, NoSQL, Java, C, Chai Unit Testing, Frontend, Backend, and Full-Stack development.

I have worked in several positions where I have gained valuable experience. As the Chief Technical Officer and Co-Founder of SignAssist, I designed and implemented a Chrome extension to solve the problem of transaction security and readability in the web3 space. I also developed and provided API as a Service to non-custodial wallets in a B2B capacity and secured frontier.xyz as our client. I assisted in creating a business model for the startup and redirected the direction of the business.

As an Independent Contractor, Full Stack Blockchain Engineer, I managed and directed the development of various projects for over 15 international clients, primarily serving as a Frontend , Solidity and backend engineer. I designed and constructed Backend Architectures of various projects, including an NFT marketplace, initial NFT offerings, token whitelisting with Merkle proofs, NFT minting, NFT subscriptions, ve(3,3), vaults, lending, and borrowing. I also developed scalable APIs and distributed systems and created bots to index on-chain events on the blockchain. Some of the projects I worked on include emillionsart.com, Metria, Diva Protocol, Milkshake Finance, Metalaunch, and Shiboshis.

Lastly, as a Full Stack Blockchain Engineer at Cryption Network in Pune, I built and led the development of Cryption Network Core Smart Contracts. I wrote test cases, collaborated with other team members, and audited smart contracts. I contributed to the growth of the TVL from zero to 10 million USD by optimizing the frontend application built in React and enhancing Web3 integrations. As the second employee, I provided innovative ideas and actively supported the company in securing a 1.5 million dollar funding round.
"""

if __name__ == '__main__':
    # print("hello langchain")

    linkedin_profile_url = 'https://in.linkedin.com/in/samarth30'

    # print(linkedin_profile_url)

    summary_template = """" 
    given the linkedin information {information} about a person from i want to create : 
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # elonMuskInterestingFacts = chain.run(information)
    # print(elonMuskInterestingFacts)

    linkedindata = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url)
    # print(linkedindata)

    user_input = st.text_input("Enter your text here")

    # Create a button
    if st.button("Process Text"):
        # Call your function and store the result
        result = chain.run(information=information)

        st.image("https://media.licdn.com/dms/image/D4D03AQHRomotqsqiyg/profile-displayphoto-shrink_400_400/0/1694683690619?e=1708560000&v=beta&t=Nr_UWc5gr1vU5dE_QM4GhHQ7qpDnyxOHJ7qYF0ezuws")
        # Display the result
        st.write(result)
