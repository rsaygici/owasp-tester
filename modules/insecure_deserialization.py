import requests

def test_insecure_deserialization(base_url):
    """
    Test for insecure deserialization by sending malicious serialized objects.
    """
    vulnerable_url = f"{base_url}/api/deserialize"
    malicious_payload = '{"__class__":"os.system","__args__":["ls"]}'  # Örnek JSON payload
    findings = []

    response = requests.post(vulnerable_url, data=malicious_payload)
    if response.status_code == 200 and "ls" in response.text:
        findings.append("Insecure deserialization vulnerability detected.")
    return findings
