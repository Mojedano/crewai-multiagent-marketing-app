import os
import argparse
from dotenv import load_dotenv
from crewai import Agent, Task, Crew


def build_crew(language: str = "es") -> Crew:
    agent = Agent(
        role="Content Marketing Strategist",
        goal="Diseñar una estrategia de marketing de contenidos eficaz para SaaS B2B",
        backstory=(
            "Especialista en marketing digital y creación de contenidos, "
            "con experiencia en estrategia, SEO y storytelling."
        ),
    )

    expected_lang = "español" if language == "es" else "English"
    task = Task(
        description=(
            "Define una estrategia de marketing de contenidos en 5 puntos "
            "para una empresa SaaS B2B. Incluye acciones concretas."
        ),
        expected_output=f"Lista de 5 puntos accionables, redactados en {expected_lang}.",
        agent=agent,
    )

    return Crew(agents=[agent], tasks=[task])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CrewAI Multi-Agent LLM App - Content Marketing Strategy Generator"
    )
    parser.add_argument(
        "--lang",
        choices=["es", "en"],
        default="es",
        help="Idioma de salida (es/en). Default: es",
    )
    args = parser.parse_args()

    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY no encontrada. Crea un archivo .env a partir de .env.example "
            "y añade tu clave."
        )

    print("▶️ Ejecutando CrewAI...")
    crew = build_crew(language=args.lang)
    result = crew.kickoff()

    print("\n✅ Resultado:\n")
    print(result)


if __name__ == "__main__":
    main()
