"""Module homework #5"""

import argparse
from faker import Faker


def generate_greeting() -> None:
    """Generates a greeting"""
    name = get_name_from_argument()
    if not name:
        name = generating_name()
    print_greeting_for_user(name)


def get_name_from_argument() -> str | None:
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


def generating_name() -> str:
    """Generating name with faker

    Returns
    -------
    str
        The generated name
    """
    faker = Faker()
    return faker.name()


def print_greeting_for_user(name: str) -> None:
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
    """
    Generate greeting entry point

    Returns
    -------
    None
    """
    generate_greeting()
