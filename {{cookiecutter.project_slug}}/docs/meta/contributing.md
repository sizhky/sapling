# Contributing Guide

**Summary:** Thank you for your interest in contributing to our project! This guide outlines our contribution process, coding standards, and how to get your changes merged.

## How to Contribute

We welcome contributions of all kinds, from bug fixes to new features. To get started, please follow these steps:

1.  **Fork the Repository:** Create your own copy of the repository on GitHub.
2.  **Create a Branch:** Create a new branch for your changes.
    ```bash
    git checkout -b feature/my-awesome-feature
    ```
3.  **Make Your Changes:** Write your code and add tests to cover your changes.
4.  **Ensure Tests Pass:** Run the full test suite to ensure your changes don't break anything.
    ```bash
    pytest
    ```
5.  **Commit Your Work:** Follow our commit message conventions.
    ```bash
    git commit -m "feat: Add my awesome feature"
    ```
6.  **Submit a Pull Request (PR):** Push your branch to your fork and open a PR against our `main` branch. Provide a clear description of your changes.

## Coding Standards

- **Style Guide:** We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code. We use `black` for formatting and `ruff` for linting.
- **Testing:** All new features must be accompanied by tests. We use `pytest` for our testing framework.
- **Documentation:** If you add a new feature, please update the relevant documentation in the `/docs` directory.

## Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. This helps us automate changelog generation and makes the commit history more readable.

**Format:** `<type>(<scope>): <subject>`

- **`type`:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **`scope`:** (optional) The part of the codebase you are changing (e.g., `api`, `db`).
- **`subject`:** A short, imperative-tense description of the change.

**Example:**
`feat(api): add endpoint for user profiles`

## Pull Request Process

1.  Once a PR is submitted, a core team member will review it.
2.  You may be asked to make changes based on the feedback.
3.  Once the PR is approved and all checks pass, it will be merged into the `main` branch.

---
*For a more detailed setup guide, see the [Onboarding Guide](../non-technical/onboarding/guide.md).*
