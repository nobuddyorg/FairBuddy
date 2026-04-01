#!/usr/bin/env python3
# ruff: noqa: T201
"""Cross-platform bootstrap script for the FairBuddy development environment.

Usage:
    macOS / Linux:  python3 boot.py
    Windows:        python boot.py
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def ask(prompt: str) -> bool:
    """Ask a yes/no question in a loop until valid input is provided."""
    while True:
        answer = input(f"{prompt} [y/n]: ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def run(cmd: list[str]) -> None:
    """Run a subprocess command, raising on failure."""
    subprocess.run(cmd, check=True)  # noqa: S603


def install_uv() -> None:
    """Install uv using the official platform-appropriate installer."""
    print("uv not found. Installing uv...")
    os_name = sys.platform
    if os_name in ("linux", "darwin"):
        run(["sh", "-c", "curl -LsSf https://astral.sh/uv/install.sh | sh"])
        # Ensure ~/.local/bin is on PATH so uv is usable in this session
        uv_bin = str(Path.home() / ".local" / "bin")
        if uv_bin not in os.environ.get("PATH", ""):
            os.environ["PATH"] = uv_bin + ":" + os.environ.get("PATH", "")
    elif os_name == "win32":
        run(
            [
                "powershell",
                "-ExecutionPolicy",
                "ByPass",
                "-Command",
                "irm https://astral.sh/uv/install.ps1 | iex",
            ],
        )
    else:
        print(
            f"Unsupported platform: {os_name}\n"
            "Please install uv manually: https://docs.astral.sh/uv/getting-started/installation/",
        )
        sys.exit(1)
    print("uv installed successfully.\n")


def optional_tool(
    name: str,
    brew_name: str | None = None,
    winget_name: str | None = None,
    linux_cmd: str | None = None,
) -> None:
    """Prompt to install an optional tool using the right method per platform."""
    if not ask(f"Install {name}?"):
        return

    os_name = sys.platform
    if os_name == "darwin":
        if brew_name:
            try:
                run(["brew", "install", brew_name])
            except subprocess.CalledProcessError:
                print(
                    f"Warning: Attempted to install {name}, but it returned an error. "
                    "You may need to install it manually.",
                )
        else:
            print(f"No Homebrew formula known for {name}. Please install manually.")
    elif os_name == "win32":
        if winget_name:
            print(f"\n  Run this in an admin terminal to install {name}:")
            print(f"    winget install {winget_name}\n")
        else:
            print(f"Please install {name} manually for Windows.")
    elif linux_cmd:
        print(f"\n  Run this to install {name}:")
        print(f"    {linux_cmd}\n")
    else:
        print(f"Please install {name} manually for your Linux distro.")
    print()


def main() -> None:
    """Run the full bootstrap sequence."""
    print("=" * 50)
    print("  FairBuddy — Bootstrap")
    print("=" * 50)
    print()

    # Step 1: Ensure uv is available
    if not shutil.which("uv"):
        install_uv()
    else:
        print("✓ uv is already installed.\n")

    # Step 2: Install pinned Python version
    if ask("\nInstall pinned Python version with uv?"):
        print("Installing Python…")
        run(["uv", "python", "install"])
        print("✓ Python installed.\n")

    # Step 3: Sync all project dependencies (downloads targeted Python + .venv)
    print("Syncing project dependencies with uv…")
    run(["uv", "sync"])
    print("✓ Dependencies synced.\n")

    # Step 4: Install git hooks via prek
    print("Installing git hooks via prek…")
    run(["uv", "run", "prek", "install"])
    run(["uv", "run", "prek", "install", "--hook-type", "commit-msg"])
    print("✓ Git hooks installed.\n")

    # Step 5: Optional tools (interactive)
    print("Optional tools (skip any you don't need):\n")

    optional_tool(
        "AWS CLI",
        brew_name="awscli",
        winget_name="Amazon.AWSCLI",
        linux_cmd="pip install awscli  # or use your distro's package manager",
    )
    optional_tool(
        "Pulumi",
        brew_name="pulumi/tap/pulumi",
        winget_name="Pulumi.Pulumi",
        linux_cmd="curl -fsSL https://get.pulumi.com | sh",
    )
    optional_tool(
        "act (run GitHub Actions locally)",
        brew_name="act",
        winget_name="nektos.act",
        linux_cmd="curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash",
    )

    # opengrep: Linux/macOS use curl installer; Windows requires manual download
    if ask("Install opengrep (static code analysis)?"):
        if sys.platform == "win32":
            print(
                "\n  opengrep Windows binaries are available at:\n  https://github.com/opengrep/opengrep/releases\n",
            )
        else:
            try:
                run(
                    [
                        "sh",
                        "-c",
                        "curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh | bash",
                    ],
                )
            except subprocess.CalledProcessError:
                print("Warning: opengrep installation failed. You may need to install it manually.")
        print()

    # Step 6: Optional AWS configuration
    if ask("Run 'aws configure' now?"):
        run(["aws", "configure"])

    print()
    print("=" * 50)
    print("  Bootstrap finished! Happy coding 🎉")
    print("=" * 50)


if __name__ == "__main__":
    main()
