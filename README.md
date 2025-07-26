# Password Strength Analyzer with Custom Wordlist Generator

## Overview

This project is a Python-based tool designed to analyze the strength of user passwords and generate targeted custom wordlists. It is ideal for cybersecurity learners, penetration testers, and ethical hackers who want to understand password vulnerabilities and create effective wordlists for password auditing.

## Features

- Analyze password strength using `zxcvbn` algorithm
- Accept personal inputs (e.g., name, birthdate, pet) to craft realistic wordlists
- Generate common patterns like leetspeak, reversed strings, appended years
- Export wordlists in `.txt` format for use in password-cracking tools
- Easy-to-use CLI and GUI interface via `argparse` and `tkinter`

## Tools and Libraries Used

- **Python 3**
- **zxcvbn** – For password strength estimation
- **argparse** – For command-line parsing
- **tkinter** – For graphical user interface
- **os, sys** – For basic I/O operations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-wordlist-tool.git
   cd password-strength-wordlist-tool
