import requests

def test_cross_site_scripting(base_url):
    """
    Test for reflected XSS vulnerabilities by injecting script payloads into URL parameters.
    """
    test_payload = "<script>alert('XSS')</script>"
    url = f"{base_url}/search?q={test_payload}"
    response = requests.get(url)
    
    findings = []
    if test_payload in response.text:
        findings.append("Reflected XSS vulnerability detected.")
    return findings
