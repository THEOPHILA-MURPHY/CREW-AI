from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
import os

def create_healthcare_crew(topic: str):
    # Initialize the LLM (make sure GROQ_API_KEY is in environment variables)
    # The ChatGroq class automatically picks up os.environ["GROQ_API_KEY"]
    llm = ChatGroq(
        temperature=0.7,
        model_name="mixtral-8x7b-32768",
        max_tokens=2048
    )

    # Agent 1: Researcher
    researcher = Agent(
        role="Senior Healthcare Researcher",
        goal=f"Collect accurate and up-to-date healthcare information about {topic}.",
        backstory="You are an expert medical researcher with a careful eye for accuracy. You only rely on reliable, scientifically-backed facts.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # Agent 2: Writer
    writer = Agent(
        role="Healthcare Content Writer",
        goal="Convert research findings into a well-structured, easy-to-understand blog post.",
        backstory="You are a skilled writer who specializes in making complex medical topics simple, clear, and engaging for the general public.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # Agent 3: Editor
    editor = Agent(
        role="Medical Content Editor",
        goal="Review the content for clarity, grammar, factual consistency, and safety.",
        backstory="You are a strict editor who ensures that healthcare content is safe, non-misleading, grammatically flawless, and carries an appropriate tone.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # Task 1
    research_task = Task(
        description=f"Conduct thorough research on '{topic}'. Focus on recent guidelines, best practices, and essential facts. Ensure medical relevance.",
        expected_output="A detailed summary of medical facts, statistics, and best practices regarding the topic.",
        agent=researcher
    )

    # Task 2
    write_task = Task(
        description="Using the findings from the researcher, write a comprehensive and engaging blog post about the topic. Include an introduction, body paragraphs with clear headings, and a conclusion.",
        expected_output="A formatted draft of a blog post containing introductions, clearly separated sections, and a helpful conclusion.",
        agent=writer
    )

    # Task 3
    edit_task = Task(
        description="Review the article draft. Ensure the language is accessible, grammatically correct, and medically safe (no dangerous advice). Return the final polished blog post in markdown format.",
        expected_output="The final, polished markdown blog post ready for publishing.",
        agent=editor
    )

    # Bring it all together
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, write_task, edit_task],
        process=Process.sequential
    )

    return crew
