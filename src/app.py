from __future__ import annotations

import argparse
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process


load_dotenv()


def build_agents(verbose: bool = False):
    """Create and return the marketing agents."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    strategy_agent = Agent(
        role="Content Strategy Expert",
        goal="Define an effective content marketing strategy for a SaaS B2B company",
        backstory="Expert in SaaS positioning and content planning.",
        llm=llm,
        allow_delegation=True,
        verbose=verbose,
    )

    seo_agent = Agent(
        role="SEO Specialist",
        goal="Optimize content ideas for search engines",
        backstory="SEO expert focused on B2B SaaS growth.",
        llm=llm,
        verbose=verbose,
    )

    content_agent = Agent(
        role="Content Creator",
        goal="Generate high-quality content ideas and formats",
        backstory="Creative marketer specialized in content creation.",
        llm=llm,
        verbose=verbose,
    )

    distribution_agent = Agent(
        role="Content Distribution Manager",
        goal="Plan content promotion and distribution channels",
        backstory="Expert in content amplification and growth strategies.",
        llm=llm,
        verbose=verbose,
    )

    return strategy_agent, seo_agent, content_agent, distribution_agent


def run_marketing_strategy(company: str, audience: str, goal: str, verbose: bool = False, save_path: str | None = None):
    print("\n🚀 Running CrewAI Multi-Agent Marketing Strategy...\n")

    strategy_agent, seo_agent, content_agent, distribution_agent = build_agents(verbose=verbose)

    strategy_task = Task(
        description=(
            f"Define the content marketing strategy for:\n"
            f"- Company: {company}\n"
            f"- Target audience: {audience}\n"
            f"- Business goal: {goal}\n\n"
            "Provide positioning, messaging pillars and a high-level plan."
        ),
        expected_output="A clear marketing strategy with positioning and key messaging pillars.",
        agent=strategy_agent,
    )

    seo_task = Task(
        description=(
            "Based on the strategy, propose an SEO plan: keyword themes, topic clusters, "
            "and SEO priorities for a SaaS B2B."
        ),
        expected_output="SEO plan with topic clusters and keyword themes.",
        agent=seo_agent,
    )

    content_task = Task(
        description=(
            "Create content ideas (titles + formats) aligned with the strategy and SEO plan. "
            "Include a simple editorial calendar outline."
        ),
        expected_output="Content ideas + formats + a basic editorial calendar.",
        agent=content_agent,
    )

    distribution_task = Task(
        description="Create a distribution plan: channels, cadence, repurposing ideas and metrics to track.",
        expected_output="Distribution plan with channels, cadence, and success metrics.",
        agent=distribution_agent,
    )

    crew = Crew(
        agents=[strategy_agent, seo_agent, content_agent, distribution_agent],
        tasks=[strategy_task, seo_task, content_task, distribution_task],
        process=Process.sequential,
        verbose=verbose,  # <- controla el “modo verde”
    )

    result = crew.kickoff()
    result_text = str(result)

    print("\n✅ Strategy generated successfully:\n")
    print(result_text)

    if save_path:
        out_path = Path(save_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(result_text, encoding="utf-8")
        print(f"\n📝 Saved output to: {out_path.as_posix()}")


def parse_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="CrewAI Multi-Agent Marketing App (SaaS B2B)")

    parser.add_argument("--company", required=True, help="Company or product name (e.g. 'SaaS CRM platform')")
    parser.add_argument("--audience", required=True, help="Target audience (e.g. 'SME founders', 'Marketing managers')")
    parser.add_argument("--goal", required=True, help="Main marketing goal (e.g. 'Lead generation', 'Brand awareness')")

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed agent reasoning/logs (noisy, but useful for debugging).",
    )

    parser.add_argument(
        "--save",
        default=None,
        help="Optional path to save the generated strategy (e.g. outputs/latest_result.md).",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    run_marketing_strategy(
        company=args.company,
        audience=args.audience,
        goal=args.goal,
        verbose=args.verbose,
        save_path=args.save,
    )


if __name__ == "__main__":
    main()
