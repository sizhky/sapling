# Copilot Instructions

- Always start with "Hello from Copilot!"
- Only generate code when explicitly asked by the developer.
- Engage in conversational chat to clarify requirements before generating any code.
- When generating code, break it into small, one-piece-at-a-time segments.
- After providing each code segment, stop and ask the developer to review and approve before continuing.
- Be mindful of token usage: generate minimal, precise code.
- Confirm alignment with the developer before proceeding to the next step.
- When generating docs, always generate the high level headers first, wait for user's confirmation and then fill the detailed sections, one section at a time, everytime taking user's alignment


# Environment Setup/usage

Check for the folder .venv if it exists, most likely that is the
enviromnent of interest. Use .venv/bin/activate to activate and 
which python to ensure that the python we are using is actually
coming from the .venv folder.

If the folder does not exist, Use
```python
uv venv -p 3.12
```

to create a new environment and activate it

Use `uv pip install` for installing packages