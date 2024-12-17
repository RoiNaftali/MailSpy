import os
import subprocess
from pathlib import Path

def banner():
    """Prints the banner."""
    print("=" * 60)
    print("              EMAIL OSINT AUTOMATION TOOL")
    print("        Powered by Mosint, Sherlock, GHunt, and TheHarvester")
    print("=" * 60)

def check_tool_availability(tool_name, tool_path):
    """Checks if a tool is available in the given path."""
    if not Path(tool_path).exists():
        print(f"[-] {tool_name} is not installed or the path is incorrect.")
        return False
    return True

def run_mosint(email):
    """Run Mosint for email OSINT."""
    print("[+] Running Mosint...")
    mosint_path = "./mosint"  # Replace with your Mosint installation path
    if check_tool_availability("Mosint", mosint_path):
        os.chdir(mosint_path)
        subprocess.run(["python3", "mosint.py", "-e", email])
        os.chdir("..")

def run_sherlock(email):
    """Run Sherlock to find social media accounts."""
    print("[+] Running Sherlock...")
    sherlock_path = "./sherlock/sherlock"  # Replace with your Sherlock installation path
    if check_tool_availability("Sherlock", sherlock_path):
        subprocess.run(["python3", sherlock_path, email])

def run_ghunt(email):
    """Run GHunt for Google account information."""
    print("[+] Running GHunt...")
    ghunt_path = "./GHunt/ghunt.py"  # Replace with your GHunt installation path
    if check_tool_availability("GHunt", ghunt_path):
        subprocess.run(["python3", ghunt_path, "email", email])

def run_theharvester(domain):
    """Run TheHarvester to gather information about the email's domain."""
    print("[+] Running TheHarvester...")
    try:
        subprocess.run(["theharvester", "-d", domain, "-l", "100", "-b", "google"])
    except FileNotFoundError:
        print("[-] TheHarvester is not installed. Install it using: apt install theharvester")

def extract_domain(email):
    """Extract the domain from an email address."""
    if "@" in email:
        return email.split("@")[1]
    return None

def main():
    banner()
    email = input("[*] Enter the target email address: ").strip()
    
    if "@" not in email:
        print("[-] Invalid email address.")
        return

    # Extract domain from the email address
    domain = extract_domain(email)
    if domain:
        print(f"[+] Domain extracted: {domain}")

    # Run tools
    run_mosint(email)
    run_sherlock(email)
    run_ghunt(email)
    run_theharvester(domain)

if __name__ == "__main__":
    main()
