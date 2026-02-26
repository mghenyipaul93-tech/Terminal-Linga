#  Define the command structure

import argparse
from config import APP_NAME, VERSION


def setup_parser():
    parser = argparse.ArgumentParser(
        prog="Linga",
        description="LingaTerminal - A  Multi-Dialect Documentation and translation engine"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{APP_NAME} {VERSION}"
    )

    subparsers = parser.add_subparsers(dest="command")

    # explain command

    explain_parser = subparsers.add_parser(
        "explain",
        help="Explain a programming command in a selected language"
    )
    explain_parser.add_argument(
        "--cmd", required=True, help="command to explain")
    explain_parser.add_argument(
        "--lang", required=True, help="Target language")

    # Transpile command
    transpile_parser = subparsers.add_parser(
        "transpile",
        help="Convert indigenous logic into valid programming code"
    )

    transpile_parser.add_argument(
        "--code", required=True, help="Code to transpile")
    transpile_parser.add_argument(
        "--to", required=True, help="Target language (python/javascript)")

    return parser
