import typer

from pchex.deps import generate_urls
from pchex.models.compounds import RequestParams


def main(inp_string: str) -> None:
    params = RequestParams.from_string(inp_string, sep=",")
    g = generate_urls(params)
    while True:
        try:
            print(next(g))
        except StopIteration:
            print("Done!")
            break


if __name__ == "__main__":
    typer.run(main)
