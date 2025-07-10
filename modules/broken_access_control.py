import requests

def test_broken_access_control(base_url):
    """
    Test for Broken Access Control vulnerability by trying to access
    a restricted resource without proper authorization.
    """
    vulnerable_endpoints = [
        "/admin",
        "/user/settings",
        "/confidential"
    ]
    findings = []
    for endpoint in vulnerable_endpoints:
        url = f"{base_url}{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            findings.append(f"Accessible restricted endpoint without auth: {url}")
    return findings
