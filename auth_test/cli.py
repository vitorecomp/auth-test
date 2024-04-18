"""CLI interface for auth_test project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

import google.auth
import google.auth.transport.requests



def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m auth_test` and `$ auth_test `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    print("Hello un-auth")

    credentials, project = google.auth.default()
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    print(credentials)
    print(credentials.token)
    print(project)
