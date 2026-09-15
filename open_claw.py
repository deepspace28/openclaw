#!/usr/bin/env python3
"""Serve the Open Claw demo locally."""

from __future__ import annotations

import argparse
import http.server
import os
import socketserver
from pathlib import Path


WEB_ROOT = Path(__file__).resolve().parent / "web"


class OpenClawHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_ROOT), **kwargs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Open Claw demo.")
    parser.add_argument("--port", type=int, default=8000, help="Port to serve on.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not WEB_ROOT.exists():
        raise SystemExit(f"Missing web assets at {WEB_ROOT}")

    os.chdir(WEB_ROOT)
    with socketserver.TCPServer(("", args.port), OpenClawHandler) as httpd:
        print(f"Open Claw running at http://localhost:{args.port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down Open Claw.")


if __name__ == "__main__":
    main()
