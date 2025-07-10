from modules import broken_access_control
from modules import injection
from modules import security_misconfiguration
from modules import authentication_failure
from modules import vulnerable_components
from modules import account_takeover
from modules import cross_site_scripting
from modules import remote_code_execution
from modules import insecure_deserialization
from modules import server_side_request_forgery
from modules import software_data_integrity_failures

def run_all_tests(base_url):
    all_findings = []

    all_findings.extend(broken_access_control.test_broken_access_control(base_url))
    all_findings.extend(injection.test_injection(base_url))
    all_findings.extend(security_misconfiguration.test_security_misconfiguration(base_url))
    all_findings.extend(authentication_failure.test_authentication_failure(base_url))
    all_findings.extend(vulnerable_components.test_vulnerable_components(base_url))
    all_findings.extend(account_takeover.test_account_takeover(base_url))
    all_findings.extend(cross_site_scripting.test_cross_site_scripting(base_url))
    all_findings.extend(remote_code_execution.test_remote_code_execution(base_url))
    all_findings.extend(insecure_deserialization.test_insecure_deserialization(base_url))
    all_findings.extend(server_side_request_forgery.test_ssrf(base_url))
    all_findings.extend(software_data_integrity_failures.test_software_data_integrity(base_url))

    return all_findings


if __name__ == "__main__":
    target_url = input("Enter the target base URL (e.g., https://example.com): ").strip()
    results = run_all_tests(target_url)

    print("\n--- OWASP Top 10 Vulnerability Test Results ---")
    if results:
        for i, finding in enumerate(results, 1):
            print(f"{i}. {finding}")
    else:
        print("No vulnerabilities detected based on the tests.")
