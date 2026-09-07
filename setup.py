# -*- coding: utf-8 -*-

"""Metadados do projeto de instruções de instalação do screenkey."""

from pathlib import Path

from setuptools import setup


ROOT_DIR = Path(__file__).resolve().parent


def readme():
    """Retorna o conteúdo do README em Markdown."""
    return (ROOT_DIR / "README.md").read_text(encoding="utf-8")


setup(
    name="screenkey-installation-docs",
    version="0.0.1",
    description="Instruções de instalação do screenkey no Linux Ubuntu via apt.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/wavexx/screenkey",
    author="Eden Denis F. da S. L. Santos",
    license="MIT",
    py_modules=[],
    python_requires=">=3.8",
)
