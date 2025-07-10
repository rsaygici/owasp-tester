import requests

def test_account_takeover(base_url):
    """
    Test account takeover risks, e.g., password reset or session fixation vulnerabilities.
    """
    reset_url = f"{base_url}/password-reset"
    payload = {"email": "victim@example.com"}
    findings = []
    
    response = requests.post(reset_url, data=payload)
    if "reset link sent" in response.text.lower():
        findings.append("Password reset function accessible - verify email verification robustness.")
    
    # Session fixation vb. testler eklenebilir
    
    return findings
