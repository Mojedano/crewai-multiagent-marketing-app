# CrewAI Multi-Agent LLM App – Content Marketing Team Replacement

Aplicación **multiagente** construida con **CrewAI** que simula el trabajo de un equipo de marketing de contenidos para una empresa SaaS B2B.  
La aplicación define agentes con roles claros y tareas coordinadas para generar una **estrategia de marketing de contenidos estructurada y accionable** utilizando un LLM.

> EN: Multi-agent application built with CrewAI to simulate a content marketing team and generate a structured content strategy using LLMs.

---

## 🎯 Objetivo del proyecto

Demostrar el diseño y la implementación de una **aplicación multiagente basada en LLMs**, aplicando:
- definición de roles (agents)
- asignación de tareas (tasks)
- coordinación mediante CrewAI

El caso de uso se centra en **reemplazar o apoyar un equipo de marketing de contenidos**, un escenario realista y frecuente en entornos SaaS.

---

## 🧠 Enfoque y arquitectura

El proyecto sigue un enfoque dual:

- 📓 **Notebook (`notebooks/`)**  
  Versión explicada del proyecto, con razonamiento, comentarios y contexto.  
  Ideal para entender el proceso y las decisiones de diseño.

- 🐍 **Script ejecutable (`src/app.py`)**  
  Versión limpia y profesional del núcleo de la aplicación, pensada para ejecución directa sin Jupyter.

Este enfoque refleja un flujo de trabajo real: **exploración + implementación**.

---

## 🧩 Agentes y tareas

### Agente principal
- **Role**: Content Marketing Strategist  
- **Goal**: Diseñar una estrategia de marketing de contenidos eficaz para SaaS B2B  
- **Backstory**: Especialista en marketing digital, SEO y storytelling

### Tarea
- Definir una estrategia de marketing de contenidos en 5 puntos
- Salida esperada clara, accionable y en español

---

## 🧰 Tech Stack

- Python 3.11+
- CrewAI
- LLM (OpenAI)
- python-dotenv
- Jupyter Notebook

---

## 📁 Estructura del proyecto

```text
crewai-multiagent-marketing-app/
├─ notebooks/
│  └─ 01_crewai_multiagent_marketing.ipynb
├─ src/
│  └─ app.py
├─ assets/
├─ .env.example
├─ .gitignore
├─ requirements.txt
└─ README.md
