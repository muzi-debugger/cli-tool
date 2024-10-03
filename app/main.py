import typer
from typing_extensions import Annotated


def main(
    name: Annotated[str, typer.Argument(help="Who to greet")],
    
    lastname: Annotated[
        str, typer.Argument(help="The last name", rich_help_panel="Secondary Arguments")
    ] = "",
    age: Annotated[
        str,
        typer.Argument(help="The user's age", rich_help_panel="Secondary Arguments"),
    ] = "",
):
    """
    Add a name argument and an optional lastname argument.
    """
    print(f"Hello {name} {lastname} you are {age} years old")


if __name__ == "__main__":
    typer.run(main)