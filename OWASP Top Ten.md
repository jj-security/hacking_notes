[OWASP Top 10](https://owasp.org/Top10/2025/)

- [A01:2025 - Broken Access Control](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/)
- [A02:2025 - Security Misconfiguration](https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/)
- [A03:2025 - Software Supply Chain Failures](https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/)
- [A04:2025 - Cryptographic Failures](https://owasp.org/Top10/2025/A04_2025-Cryptographic_Failures/)
- [A05:2025 - Injection](https://owasp.org/Top10/2025/A05_2025-Injection/)
- [A06:2025 - Insecure Design](https://owasp.org/Top10/2025/A06_2025-Insecure_Design/)
- [A07:2025 - Authentication Failures](https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/)
- [A08:2025 - Software or Data Integrity Failures](https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/)
- [A09:2025 - Security Logging & Alerting Failures](https://owasp.org/Top10/2025/A09_2025-Security_Logging_and_Alerting_Failures/)
- [A10:2025 - Mishandling of Exceptional Conditions](https://owasp.org/Top10/2025/A10_2025-Mishandling_of_Exceptional_Conditions/)

## [A01:2025 - Broken Access Control](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/)
- Can I access what I shouldn't be able to?
- IDOR - Insecure Direct Object Reference
- Horizontal & Vertical Privilege Escalation
- Missing auth checks on endpoints

### **Tools**:
- Burp Repeater
- ffuf (endpoint Discovery)

### **Notable CWEs**:
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
- CWE-201: Exposute of Sensitive Information Through Sent Data
- CWE-918: Server-Side Request Forgery (SSRF)
- CWE-352: Cross-Site Request Forgery (CSRF)

### **Description/Common Access Control Vulnerabilities**:
- Violation of least privilege, commonly known as deny by default, where access should only be granted for particular capabilities, roles, or users, but is available to anyone.
- Bypassing access control checks by modifying the URL (parameter tampering or force browsing), internal application state, or the HTML page, or by using an attack tool that modifies API requests.
- Permitting viewing or editing someone else's account by providing its unique identifier (insecure direct object reference)
- An accessible API with missing access controls for POST, PUT, and DELETE
- Elevation of privilege. Acting as a user without being logged in or gaining privileges.

### **Prevention**:
- Enforce server-side access control checks
- Deny by default, allow explicitly
- Use indirect object references
- Centralize auth logic

## [A02:2025 - Security Misconfiguration](https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/)
- Did they forget to secure something?
- Default configurations
- Exposed admin/debug endpoints
- Missing headers

### **Tools**:
- nmap
- nikto
- Burp Scanner

### **Notable CWEs**:
- CWE-16: Configuration
- CWE-611: XXE
- CWE-933: Improper Neutralization

### **Description/Common Access Control Vulnerabilities**:
- Default credentials or configs
- Directory listing enabled
- Debug mode enabled
- Missing security headers
- Open cloud storage (S3, blobs)

### **Prevention**:
- Harden configurations
- Disable unused features
- Apply secure headers
- Regular config audits

## [A03:2025 - Software Supply Chain Failures](https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/)
- Are dependencies compromised or vulnerable?
- Outdated libraries
- Malicious packages

### **Tools**:
- npm audit
- Snyk
- Trivy

### **Notable CWEs**:
- CWE-1104: Use of Unmaintained Components
- CWE-494: Download of Code Without Integrity Check

### **Description/Common Access Control Vulnerabilities**:
- Using vulnerable dependencies
- Dependency confusion attacks
- No integrity verification
- Compromised build pipelines

### **Prevention**:
- Dependency scanning
- Pin versions
- Verify package integrity
- Secure CI/CD pipelines

## [A04:2025 - Cryptographic Failures](https://owasp.org/Top10/2025/A04_2025-Cryptographic_Failures/)
- Is sensitive data exposed or weakly protected?
- Weak encryption
- No HTTPS

### **Tools**:
- openssl
- testssl.sh
- [Qualys SSL Labs Server Test](https://www.ssllabs.com/ssltest/index.html) - Deep analysis of the config of any SSL web server on the public internet.

### **Notable CWEs**:
- CWE-327: Broken Crypto
- CWE-319: Cleartext Transmission
- CWE-326: Weak Encryption

### **Description/Common Access Control Vulnerabilities**:
- Sensitive data in plaintext
- Weak or outdated algorithms
- Improper key management
- Missing encryption

### **Prevention**:
- Use strong crypto (AES, TLS 1.2+)
- Encrypt sensitive data
- Proper key storage/rotation

## [A05:2025 - Injection](https://owasp.org/Top10/2025/A05_2025-Injection/)
- Can I execute commands via input?
- SQL, OS, LDAP injection

### **Tools**:
- sqlmap
- Burp Intruder

### **Notable CWEs**:
- CWE-89: SQL Injection
- CWE-78: OS Command Injection

### **Description/Common Access Control Vulnerabilities**:
- Unsanitized input executed as code
- Dynamic queries without parameterization
- Command execution via user input

### **Prevention**:
- Parameterized queries
- Input validation
- Use safe APIs
- Java PreparedStatement() for SQL

## [A06:2025 - Insecure Design](https://owasp.org/Top10/2025/A06_2025-Insecure_Design/)
- Was the system designed insecurely?
- No threat modeling
- Business logic flaws

### **Tools**:
- Manual testing
- Threat modeling

### **Notable CWEs**:
- CWE-840: Business Logic Errors
- CWE-602: Client-side Enforcement

### **Description/Common Access Control Vulnerabilities**:
- Missing security requirements
- Logic flaws (race conditions, abuse flows)
- Trusting client-side validation

### **Prevention**:
- Threat modeling
- Secure design principles
- Abuse case testing

## [A07:2025 - Authentication Failures](https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/)
- Can I bypass login/session?
- Weak passwords
- Session hijacking

### **Tools**:
- Burp Suite
- Hydra (Brute Forcing)

### **Notable CWEs**:
- CWE-287: Improper Authentication
- CWE-384: Session Fixation

### **Description/Common Access Control Vulnerabilities**:
- Weak credential policies
- Missing MFA
- Session tokens predictable/reusable

### **Prevention**:
- Strong auth (MFA)
- Secure session handling
- Rate limiting

## [A08:2025 - Software or Data Integrity Failures](https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/)
- Can I tamper with data or code?
- Unsigned updates
- Deserialization

### **Tools**:
- Burp
- ysoserial

### **Notable CWEs**:
- CWE-502: Insecure Deserialization
- CWE-345: Insufficient Verification

### **Description/Common Access Control Vulnerabilities**:
- Trusting unverified data
- Unsigned updates
- Tampering with serialized objects

### **Prevention**:
- Verify integrity (signatures)
- Avoid unsafe deserialization
- Use secure update mechanisms

## [A09:2025 - Security Logging & Alerting Failures](https://owasp.org/Top10/2025/A09_2025-Security_Logging_and_Alerting_Failures/)
- Will anyone notice my attack?
- No logging
- No alerts

### **Tools**:
- SIEM (Splunk, ELK)

### **Notable CWEs**:
- CWE-778: Insufficient Logging

### **Description/Common Access Control Vulnerabilities**:
- Missing logs for critical actions
- No alerting on suspicious activity
- Logs not monitored

### **Prevention**:
- Centralized logging
- Real-time alerting
- Monitor auth/access events

## [A10:2025 - Mishandling of Exceptional Conditions](https://owasp.org/Top10/2025/A10_2025-Mishandling_of_Exceptional_Conditions/)
- What happens when things break?
- Verbose errors
- Unhandled exceptions

### **Tools**:
- Burp
- Manual fuzzing
- FFUF

### **Notable CWEs**:
- CWE-209: Information Exposure via Errors
- CWE-391: Unchecked Errors

### **Description/Common Access Control Vulnerabilities**:
- Stack traces exposed
- Crashes leak data
- Improper error handling

### **Prevention**:
- Generic error messages
- Proper exception handling
- Log internally, not to users