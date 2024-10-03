import typer

def main(
    name: str = typer.Option(..., prompt="What is your first name?"),
    lastname: str = typer.Option(..., prompt="What is your last name?")
):
    print(f"Hello {name} {lastname}")

if __name__ == "__main__":
    typer.run(main)
