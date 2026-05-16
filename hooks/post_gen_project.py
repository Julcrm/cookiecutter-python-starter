"""Post-generation hook for Cookiecutter.

Runs after project generation to remove optional files, initialise Git,
and install dependencies.
"""
import shutil
import subprocess
from pathlib import Path


def run_command(command: str) -> None:
    """Run a shell command, printing an error message on failure."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError:
        print(f"[!] Command failed: {command}")


# Remove .github/ if GitHub Actions were not requested
if "{{ cookiecutter.include_github_actions }}" == "no":
    shutil.rmtree(Path(".github"), ignore_errors=True)
    print("[~] Skipped GitHub Actions (.github/ removed)")

# Remove Dockerfile if Docker was not requested
if "{{ cookiecutter.include_docker }}" == "no":
    Path("Dockerfile").unlink(missing_ok=True)
    print("[~] Skipped Docker (Dockerfile removed)")

print("\n[+] Initialising Git repository...")
run_command("git init")
run_command("git add .")
run_command("git commit -m 'feat: initial commit from template'")

print("\n[+] Installing dependencies with uv...")
run_command("uv sync")

print("\n[✓] Project ready. Run: cd {{ cookiecutter.project_slug }}")
