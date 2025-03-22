# Password Strength and Breach Checker

This script checks whether a given password has been compromised in a data breach using the Have I Been Pwned API. It utilizes SHA-1 hashing and the k-Anonymity model to ensure that full passwords are never sent over the network.

## Features
- Converts a password into a SHA-1 hash
- Uses the first 5 characters of the hash to query the Have I Been Pwned API
- Checks if the password appears in known data breaches
- Provides feedback on whether the password is safe to use

## Requirements
- Python 3.x
- `requests` module

## Installation
Before running the script, install the required dependency:

```bash
pip install requests
```

## Usage
Run the script from the command line and provide one or more passwords as arguments:

```bash
python password_checker.py yourpassword1 yourpassword2
```

### Example Output
```
Password was found in a data breach 100 times, please change it.
```
Or, if the password is safe:
```
yourpassword1 is a good password. You can use it.
```

## How It Works
1. The password is converted into a SHA-1 hash.
2. The first 5 characters of the hash are sent to the Have I Been Pwned API.
3. The API returns all matching hash suffixes.
4. The script checks if the full hash appears in the returned results.
5. If found, the script reports the number of times the password appeared in breaches.

## Security Note
This script follows best practices by never sending the full password or full hash over the internet. However, for maximum security, avoid testing highly sensitive passwords on any third-party service.


