import requests

def test_software_data_integrity(base_url):
    """
    Test for failures in software or data integrity like missing hash validation.
    """
    findings = []
    response = requests.get(f"{base_url}/download/software.exe")
    
    # Örnek kontrol: headers içerisinde hash olup olmadığını kontrol et
    if "X-Checksum" not in response.headers:
        findings.append("No checksum header found for software download.")
    
    return findings
