import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY no encontrada. "
            "Crea un archivo .env a partir de .env.example"
        )

    # Agente principal
    content_marketing_agent = Agent(
        role="Content Marketing Strategist",
        goal="Diseñar una estrategia de marketing de contenidos eficaz",
        backstory=(
            "Especialista en marketing digital y creación de contenidos, "
            "con experiencia en estrategia, SEO y storytelling."
        ),
    )

    # Tarea principal
    marketing_task = Task(
        description=(
            "Define una estrategia de marketing de contenidos en 5 puntos "
            "para una empresa SaaS B2B."
        ),
        expected_output=(
            "Lista clara de 5 puntos accionables, redactados en español."
        ),
        agent=content_marketing_agent,
    )

    # Crew
    crew = Crew(
        agents=[content_marketing_agent],
        tasks=[marketing_task],
    )

    result = crew.kickoff()
    print("\nResultado:\n")
    print(result)

if __name__ == "__main__":
    main()
