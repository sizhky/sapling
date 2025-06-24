"""Main module."""

from .__pre_init__ import cli


@cli.command()
def main() -> None:
    print("Hello World! This is the main function of {{cookiecutter.project_slug}}.")