#!/usr/local/bin/python3

"""Main module."""

import os

from app.app import app, csrf


def main():
    """Run the app."""
    app.secret_key = os.urandom(12).hex()
    csrf.init_app(app)
    app.run()


if __name__ == "__main__":
    main()
