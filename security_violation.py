# security_violation.py - security violation for agentic reviewer

import subprocess

def run_command(user_input: str) -> None:
    # ⚠️ SECURITY RISK: shell=True + unsanitized input
    cmd = f"ls {user_input}"
    subprocess.run(cmd, shell=True)

def calculate(expression: str) -> float:
    # ⚠️ SECURITY RISK: eval of arbitrary input
    return eval(expression)
