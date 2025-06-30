# security_violation.py - security violation for agentic reviewer

import subprocess

def run_command(user_input: str) -> None:
    # ⚠️ SECURITY RISK: shell=True + unsanitized input
    cmd = f"ls {user_input}"
    subprocess.run(cmd, shell=True)

def calculate(expression: str) -> float:
    # ⚠️ SECURITY RISK: eval of arbitrary input
    return eval(expression)

import pickle

def unsafe_load(data: bytes):
    # ⚠️ SECURITY RISK: untrusted pickle load
    return pickle.loads(data)

import sqlite3

def get_user(email: str):
    # ⚠️ SECURITY RISK: SQL Injection possible
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    return cursor.fetchone()
