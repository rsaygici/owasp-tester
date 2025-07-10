import requests

def test_vulnerable_components(base_url):
    """
    Checks if the application exposes vulnerable or outdated components, like specific JS/CSS versions.
    """
    findings = []
    response = requests.get(base_url)
    
    # Örnek olarak jQuery'nin eski versiyonu aranıyor
    if "jquery-1." in response.text or "jquery-2." in response.text:
        findings.append("Old and vulnerable jQuery version detected.")
    
    # Başka popüler kütüphaneler kontrol edilebilir
    if "angular.js" in response.text and "1.4." in response.text:
        findings.append("Old AngularJS version detected.")
        
    return findings
