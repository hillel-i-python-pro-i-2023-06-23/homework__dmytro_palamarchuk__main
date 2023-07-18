from faker import Faker
import argparse


def generatingaGreeting() -> None:
    """Generates a greeting"""
    name = getNameFromArgument()
    if not name:
        name = generatingName()
    printGreetingForUser(name)


def getNameFromArgument() -> str | None:
    """Get the name from the argument

    Returns
    -------
    str | None
        the name of the user from argument if exists
    """
    parser = argparse.ArgumentParser(
        prog="main",
    )

    parser.add_argument(
        "-u",
        "--username",
        help="The username for greeting.",
    )

    args, _ = parser.parse_known_args()

    if args.username:
        return args.username

    return None


def generatingName() -> str:
    """Generating name with faker

    Returns
    -------
    str
        The generated name
    """
    faker = Faker()
    return faker.name()


def printGreetingForUser(name: str) -> None:
    """Print Greeting for User with name

    Parameters
    ----------
    name: str,
        The name of the user

    Returns
    -------
    None
    """
    print(f"Hello {name}!")


def main():
    generatingaGreeting()
