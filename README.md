# QuantumShield

**Post-Quantum Cryptography Readiness & Migration Intelligence**

QuantumShield is a developer-focused security tool that discovers
cryptographic assets in a codebase, evaluates post-quantum risk,
prioritizes migration work, and provides an interactive readiness
dashboard.

> **You cannot migrate cryptography you cannot see.**

## Live Demo

**Deployed Streamlit application:**\
https://quantum-shield.streamlit.app/

**Source repository:**\
https://github.com/Neel-stack-deb/QuantumShield

## What QuantumShield Does

``` text
Source Code / GitHub Repository
            |
            v
   Cryptographic Discovery
            |
            v
      Crypto Inventory
            |
            v
     Quantum Risk Model
            |
            v
   Migration Prioritization
            |
            v
    PQC Recommendations
            |
            v
     Dashboard + CI/CD
```

### Core capabilities

-   **Cryptographic inventory** --- detects classical and post-quantum
    algorithms with file, line, context, category, and detection method.
-   **Quantum risk assessment** --- evaluates algorithm risk,
    sensitivity, confidentiality lifetime, and exposure; produces
    transparent 0--100 risk scores and severity.
-   **Migration planning** --- prioritizes findings and provides
    migration targets, rationale, confidence, recommended actions, and a
    phased roadmap.
-   **Migration What-If Simulator** --- models expected risk impact
    before a planned cryptographic replacement.
-   **GitHub repository scanning** --- scans public HTTPS repositories
    using the same downstream pipeline as local scans.
-   **CBOM + SARIF** --- exports cryptographic inventory and SARIF
    findings for GitHub Code Scanning.
-   **GitHub Actions CI/CD** --- installs an opt-in QuantumShield
    workflow that runs the analysis automatically and uploads SARIF.
-   **Streamlit dashboard** --- visualizes inventory, risk,
    explainability, migration priorities, simulation results,
    recommendations, and roadmap.

## Supported Cryptographic Detection

### Classical asymmetric

-   RSA
-   ECDSA
-   ECDH
-   ECC / P-256 family
-   X25519

### Hashes

-   MD5
-   SHA-1
-   SHA-256
-   SHA-384
-   SHA-512

### Symmetric

-   AES
-   AES-128
-   AES-256
-   ChaCha20 / ChaCha20-Poly1305

### Post-quantum / hybrid

-   ML-KEM
-   ML-KEM-512 / 768 / 1024
-   Kyber variants
-   ML-DSA
-   Dilithium
-   SLH-DSA
-   SPHINCS+
-   X25519 + ML-KEM hybrid indicators

## Risk Model

QuantumShield does not claim that its score is a formal security
certification. The risk score is a transparent project-defined
prioritization heuristic:

``` text
Algorithm Risk
      +
Sensitivity
      +
Confidentiality Lifetime
      +
Exposure
      |
      v
Normalized Risk Score (0–100)
      |
      v
Severity
```

The dashboard exposes the contributing factors so users can understand
why an asset received its score.

## CLI Usage

### Local scan

``` powershell
python pqcscan.py ./sample-project
```

### Export inventory

``` powershell
python pqcscan.py ./sample-project --json output/inventory.json
```

### Run the complete pipeline

``` powershell
python pqcscan.py ./sample-project --export all
```

### Scan a public GitHub repository

``` powershell
python pqcscan.py --github https://github.com/OWNER/REPOSITORY
```

### Scan with exclusions

``` powershell
python pqcscan.py --github https://github.com/OWNER/REPOSITORY --exclude tests
```

### Install QuantumShield CI/CD

PowerShell:

``` powershell
$env:GITHUB_TOKEN="github_pat_..."
python pqcscan.py --github https://github.com/OWNER/REPOSITORY --install-ci
```

The token is used for repository workflow installation. Normal GitHub
scanning remains read-only.

## GitHub Actions

After installation, the target repository receives:

``` text
.github/
└── workflows/
    └── quantumshield.yml
```

The workflow:

1.  Checks out the target repository.
2.  Sets up Python.
3.  Installs dependencies.
4.  Runs QuantumShield discovery.
5.  Generates the risk assessment.
6.  Generates migration recommendations.
7.  Generates CBOM and SARIF.
8.  Uploads SARIF to GitHub Code Scanning.
9.  Exposes generated artifacts for inspection.

## Dashboard

**Live:** https://quantum-shield.streamlit.app/

The dashboard contains:

-   **Discover** --- cryptographic inventory.
-   **Assess** --- risk distribution, severity, quantum-safe status, and
    explainability.
-   **Simulate** --- current-vs-proposed migration risk comparison.
-   **Prioritize** --- Immediate / High / Planned / Low migration
    buckets.
-   **Migrate** --- targets, roles, confidence, rationale, and actions.
-   **Roadmap** --- Discover → Prepare → Transition → Retire →
    Continuous Agility.

## Output Artifacts

``` text
output/
├── inventory.json
├── risk_report.json
├── migration_plan.json
├── cbom.json
└── results.sarif
```

-   `inventory.json` --- discovered cryptographic assets.
-   `risk_report.json` --- risk factors, scores, severity, explanations,
    and readiness.
-   `migration_plan.json` --- prioritized recommendations and roadmap
    information.
-   `cbom.json` --- cryptographic bill-of-materials style output.
-   `results.sarif` --- GitHub Code Scanning-compatible results.

## Architecture

``` text
Feature 01
Crypto Discovery
      |
      v
inventory.json
      |
      v
Feature 02
Quantum Risk Assessment
      |
      v
risk_report.json
      |
      v
Feature 03
Migration Recommendation
      |
      v
migration_plan.json
      |
      +------------------+
      |                  |
      v                  v
Feature 04 Dashboard   CBOM / SARIF
      |
      v
Visualization + Simulator
```

The dashboard consumes the generated JSON artifacts rather than
independently rescanning source code or recomputing risk.

## Project Structure

``` text
QuantumShield/
├── pqcscan.py
├── analysis_pipeline.py
├── scanner/
├── risk/
├── migration/
├── dashboard/
├── simulator/
├── github_source/
├── exporters/
├── sample-project/
├── tests/
├── output/
└── .github/
    └── workflows/
```

## Testing

Run:

``` powershell
python -m unittest discover -s tests -v
```

**Current verification: 95 tests passed.**

Coverage includes scanner behavior, risk analysis, migration planning,
GitHub scanning, pipeline execution, exclusions, GitHub Actions
installation, artifact generation, and integration behavior.

## Example Finding

A representative scan can identify:

``` text
CLASSICAL RSA-2048       auth.py:4
CLASSICAL X25519         key_exchange.py:2
CLASSICAL ECDSA-P256     signatures.py:5
CLASSICAL MD5            legacy.py:6
CLASSICAL SHA-1          legacy.py:7
PQC      ML-KEM-768      pqc.py:7
PQC      ML-DSA          pqc.py:4
```

QuantumShield goes beyond detection:

> Where is the cryptography used, how risky is that usage, what should
> be migrated first, and what migration path should be considered?

## Security and Privacy Notes

-   Local scans operate on the selected local project.
-   Public GitHub repositories are cloned temporarily for analysis.
-   Temporary GitHub scan directories are cleaned up after the pipeline
    completes.
-   Workflow installation requires an explicit GitHub token.
-   Normal GitHub scanning does not require write access.
-   Never commit GitHub tokens to source control.
-   Migration recommendations are planning guidance and should be
    validated against protocol, certificate, interoperability,
    performance, and key-lifecycle requirements.

## Limitations

QuantumShield is a hackathon-scale security engineering tool, not a
replacement for a full enterprise cryptographic inventory platform or
formal security assessment.

Current limitations include:

-   GitHub scanning supports public HTTPS repositories.
-   Static source analysis cannot always determine the exact runtime
    cryptographic role.
-   Sensitivity, lifetime, and exposure can use deterministic defaults
    when context is insufficient.
-   Migration recommendations do not prove application compatibility.
-   The numerical risk score is a prioritization heuristic.
-   The dashboard is primarily an assessment and planning interface
    rather than an automated remediation system.

## Demo Flow

1.  Open https://quantum-shield.streamlit.app/
2.  Select **GitHub Repository**.
3.  Scan a repository such as
    `https://github.com/Neel-stack-deb/QuantumShield-demo-app`.
4.  Show the cryptographic inventory.
5.  Show the risk landscape and explainability.
6.  Run **Migration What-If** on a classical finding.
7.  Show migration priorities and recommendations.
8.  Show the GitHub Actions workflow and Code Scanning results.

## Project Status

**Status: Demo-ready**

-   [x] Cryptographic discovery scanner
-   [x] Python AST + regex detection
-   [x] Quantum risk assessment
-   [x] Transparent risk scoring
-   [x] PQC readiness score
-   [x] Migration recommendation engine
-   [x] Migration roadmap
-   [x] Migration What-If simulator
-   [x] GitHub repository scanning
-   [x] CBOM export
-   [x] SARIF export
-   [x] GitHub Code Scanning integration
-   [x] GitHub Actions workflow installation
-   [x] Streamlit dashboard
-   [x] Automated tests
-   [x] Streamlit deployment

## Why PQC Migration Matters

Post-quantum migration is not only about waiting for a future quantum
computer. **Harvest-now-decrypt-later (HNDL)** risk means information
captured today may become decryptable by sufficiently capable quantum
systems in the future.

QuantumShield is built around a practical workflow:

``` text
Discover
   ↓
Understand exposure
   ↓
Prioritize long-lived sensitive assets
   ↓
Introduce crypto-agility
   ↓
Transition to PQC / hybrid mechanisms
   ↓
Retire legacy mechanisms
   ↓
Continuously reassess
```

## License

Add the project's chosen license here before public release.
