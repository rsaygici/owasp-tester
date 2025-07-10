import requests

def test_authentication_failure(base_url):
    """
    Test for authentication failure by attempting login with invalid or blank credentials,
    and check if the system leaks sensitive information or allows access.
    """
    login_url = f"{base_url}/login"
    test_payloads = [
        {"username": "admin", "password": "wrongpass"},
        {"username": "", "password": ""},
        {"username": "user", "password": "12345"},
    ]
    findings = []
    for payload in test_payloads:
        response = requests.post(login_url, data=payload)
        if "invalid password" not in response.text.lower() and response.status_code == 200:
            findings.append(f"Possible authentication failure vulnerability with payload: {payload}")
    return findings
