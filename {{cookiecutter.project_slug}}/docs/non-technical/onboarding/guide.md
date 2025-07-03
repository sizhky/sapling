# New Developer Onboarding Guide

**Summary:** Welcome to the team! This guide provides a step-by-step process for setting up your development environment and making your first contribution.

## 1. Getting Started: Your First Week

### Day 1: Setup & Orientation
1.  **Get Access:** Ensure you have accounts for GitHub, Slack, and Jira.
2.  **Set Up Your Machine:** Follow the environment setup instructions below.
3.  **Meet the Team:** Your onboarding buddy will introduce you to the team.
4.  **Read the Docs:** Start by reading the [Business Overview](../../specifications/business/overview.md) and the [High-Level Architecture Diagram](../../architecture/high-level/diagram.md).

### Day 2-3: Dive into the Code
1.  **Clone the Repo:** `git clone <repository-url>`
2.  **Run the Project:** Follow the steps to run the application locally.
3.  **Explore the Codebase:** Use the [Code Walkthroughs](../../implementation/code-walkthroughs/README.md) to understand key areas.
4.  **Pick Your First Ticket:** Look for a "good first issue" in Jira.

### Day 4-5: Your First Contribution
1.  **Create a Branch:** `git checkout -b feature/your-feature-name`
2.  **Write Code & Tests:** Make your changes and add corresponding tests.
3.  **Submit a Pull Request:** Push your branch and open a PR for review.
4.  **Celebrate!** You've made your first contribution.

## 2. Development Environment Setup

### Prerequisites
- [Git](https://git-scm.com/)
- [Python 3.11+](https://www.python.org/)
- [Docker](https://www.docker.com/) and Docker Compose

### Installation Steps
1.  **Clone the repository:**
    ```bash
    git clone git@github.com:your-org/your-repo.git
    cd your-repo
    ```

2.  **Set up the Python environment:**
    We use `venv` for managing virtual environments.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements/dev.txt
    ```

3.  **Run the database:**
    The application requires a PostgreSQL database, which can be started easily with Docker.
    ```bash
    docker-compose up -d db
    ```

4.  **Run the application:**
    ```bash
    uvicorn src.main:app --reload
    ```
    The application should now be running at `http://127.0.0.1:8000`.

## 3. Key Resources

- **Glossary:** Unfamiliar with a term? Check the [Glossary](../glossary/terms.md).
- **Architecture:** Need a high-level view? See the [Architecture Diagrams](../../architecture/high-level/diagram.md).
- **API Docs:** Working with the API? Here is the [API Reference](../../implementation/api-reference/README.md).

---
*If you have any questions, don't hesitate to ask in the #dev-support Slack channel.*
