# wom.py - An asynchronous wrapper for the Wise Old Man API.
# Copyright (c) 2023-present Jonxslays
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import functools
import typing as t
from typing import Callable
from pathlib import Path

import nox
import msgspec

SessionT = Callable[[nox.Session], None]
InjectorT = Callable[[SessionT], SessionT]


def parse_dependencies() -> t.Dict[str, str]:
    with open("pyproject.toml", "rb") as f:
        data = msgspec.toml.decode(f.read())

    poetry = data["tool"]["poetry"]
    deps: t.Dict[str, t.Union[str, t.Dict[str, str]]] = {
        **poetry["dependencies"],
        **poetry["group"]["dev"]["dependencies"],
    }

    for k, v in deps.items():
        if isinstance(v, dict):
            deps[k] = v["version"]

    return {k.lower(): f"{k}{v}" for k, v in deps.items()}


DEPS = parse_dependencies()


def install(*packages: str) -> InjectorT:
    def inner(func: SessionT) -> SessionT:
        @functools.wraps(func)
        def wrapper(session: nox.Session) -> None:
            try:
                session.install("-U", *(DEPS[p] for p in packages))
            except KeyError as e:
                session.error(f"Invalid package install - {e}")
            return func(session)

        return wrapper

    return inner


def run(session: nox.Session, *args: str) -> None:
    session.run(*args, external=True)


@nox.session(reuse_venv=True)
@install("pytest", "pytest-asyncio", "pytest-testdox", "coverage", "aiohttp", "msgspec")
def tests(session: nox.Session) -> None:
    run(
        session,
        "coverage",
        "run",
        "--omit",
        "tests/*",
        "-m",
        "pytest",
        "--testdox",
        "--log-level=INFO",
    )


@nox.session(reuse_venv=True)
@install("coverage")
def coverage(session: nox.Session) -> None:
    if not Path(".coverage").exists():
        session.skip("Skipping coverage")

    run(session, "coverage", "report", "-m")


@nox.session(reuse_venv=True)
@install("pyright", "mypy", "aiohttp", "msgspec")
def types(session: nox.Session) -> None:
    run(session, "mypy")
    run(session, "pyright")


@nox.session(reuse_venv=True)
@install("black")
def formatting(session: nox.Session) -> None:
    run(session, "black", ".", "--check")


@nox.session(reuse_venv=True)
@install("flake8", "isort")
def imports(session: nox.Session) -> None:
    run(session, "isort", "wom", "tests", "-cq")
    run(
        session,
        "flake8",
        "wom",
        "tests",
        "--select",
        "F4",
        "--extend-ignore",
        "E,F",
        "--extend-exclude",
        "__init__.py",
    )


@nox.session(reuse_venv=True)
def licensing(session: nox.Session) -> None:
    missing: t.List[Path] = []
    files = (
        *Path("./wom").rglob("*.py"),
        *Path("./tests").glob("*.py"),
        *Path(".").glob("*.py"),
    )

    for path in files:
        with open(path) as f:
            desc = f.readline()
            copy = f.readline()

            if "# wom.py -" not in desc or "# Copyright (c)" not in copy:
                missing.append(path)

    if missing:
        session.error(
            "\nThe following files are missing license attribution:\n"
            + "\n".join(f" - {m}" for m in missing)
        )


@nox.session(reuse_venv=True)
def alls(session: nox.Session) -> None:
    session.install(".")
    run(session, "python", "scripts/alls.py")
