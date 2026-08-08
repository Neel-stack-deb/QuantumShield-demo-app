QuantumShield

Post-Quantum Cryptography Readiness & Migration Intelligence

QuantumShield is a developer-focused security tool that discoverscryptographic assets in a codebase, evaluates post-quantum risk,prioritizes migration work, and provides an interactive readinessdashboard.

You cannot migrate cryptography you cannot see.

Live Demo

Deployed Streamlit application:https://quantum-shield.streamlit.app/

Source repository:https://github.com/Neel-stack-deb/QuantumShield

What QuantumShield Does

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

Core capabilities

Cryptographic inventory --- detects classical and post-quantumalgorithms with file, line, context, category, and detection method.

Quantum risk assessment --- evaluates algorithm risk,sensitivity, confidentiality lifetime, and exposure; producestransparent 0--100 risk scores and severity.

Migration planning --- prioritizes findings and providesmigration targets, rationale, confidence, recommended actions, and aphased roadmap.

Migration What-If Simulator --- models expected risk impactbefore a planned cryptographic replacement.

GitHub repository scanning --- scans public HTTPS repositoriesusing the same downstream pipeline as local scans.

CBOM + SARIF --- exports cryptographic inventory and SARIFfindings for GitHub Code Scanning.

GitHub Actions CI/CD --- installs an opt-in QuantumShieldworkflow that runs the analysis automatically and uploads SARIF.

Streamlit dashboard --- visualizes inventory, risk,explainability, migration priorities, simulation results,recommendations, and roadmap.

Supported Cryptographic Detection

Classical asymmetric

RSA

ECDSA

ECDH

ECC / P-256 family

X25519

Hashes

MD5

SHA-1

SHA-256

SHA-384

SHA-512

Symmetric

AES

AES-128

AES-256

ChaCha20 / ChaCha20-Poly1305

Post-quantum / hybrid

ML-KEM

ML-KEM-512 / 768 / 1024

Kyber variants

ML-DSA

Dilithium

SLH-DSA

SPHINCS+

X25519 + ML-KEM hybrid indicators

Risk Model

QuantumShield does not claim that its score is a formal securitycertification. The risk score is a transparent project-definedprioritization heuristic:

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

The dashboard exposes the contributing factors so users can understandwhy an asset received its score.

CLI Usage

Local scan

python pqcscan.py ./sample-project

Export inventory

python pqcscan.py ./sample-project --json output/inventory.json

Run the complete pipeline

python pqcscan.py ./sample-project --export all

Scan a public GitHub repository

python pqcscan.py --github https://github.com/OWNER/REPOSITORY

Scan with exclusions

python pqcscan.py --github https://github.com/OWNER/REPOSITORY --exclude tests

Install QuantumShield CI/CD

PowerShell:

$env:GITHUB_TOKEN="github_pat_..."
python pqcscan.py --github https://github.com/OWNER/REPOSITORY --install-ci

The token is used for repository workflow installation. Normal GitHubscanning remains read-only.

GitHub Actions

After installation, the target repository receives:

.github/
└── workflows/
    └── quantumshield.yml

The workflow:

Checks out the target repository.

Sets up Python.

Installs dependencies.

Runs QuantumShield discovery.

Generates the risk assessment.

Generates migration recommendations.

Generates CBOM and SARIF.

Uploads SARIF to GitHub Code Scanning.

Exposes generated artifacts for inspection.

Dashboard

Live: https://quantum-shield.streamlit.app/

The dashboard contains:

Discover --- cryptographic inventory.

Assess --- risk distribution, severity, quantum-safe status, andexplainability.

Simulate --- current-vs-proposed migration risk comparison.

Prioritize --- Immediate / High / Planned / Low migrationbuckets.

Migrate --- targets, roles, confidence, rationale, and actions.

Roadmap --- Discover → Prepare → Transition → Retire →Continuous Agility.

Output Artifacts

output/
├── inventory.json
├── risk_report.json
├── migration_plan.json
├── cbom.json
└── results.sarif

inventory.json --- discovered cryptographic assets.

risk_report.json --- risk factors, scores, severity, explanations,and readiness.

migration_plan.json --- prioritized recommendations and roadmapinformation.

cbom.json --- cryptographic bill-of-materials style output.

results.sarif --- GitHub Code Scanning-compatible results.

Architecture

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

The dashboard consumes the generated JSON artifacts rather thanindependently rescanning source code or recomputing risk.

Project Structure

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

Testing

Run:

python -m unittest discover -s tests -v

Current verification: 95 tests passed.

Coverage includes scanner behavior, risk analysis, migration planning,GitHub scanning, pipeline execution, exclusions, GitHub Actionsinstallation, artifact generation, and integration behavior.

Example Finding

A representative scan can identify:

CLASSICAL RSA-2048       auth.py:4
CLASSICAL X25519         key_exchange.py:2
CLASSICAL ECDSA-P256     signatures.py:5
CLASSICAL MD5            legacy.py:6
CLASSICAL SHA-1          legacy.py:7
PQC      ML-KEM-768      pqc.py:7
PQC      ML-DSA          pqc.py:4

QuantumShield goes beyond detection:

Where is the cryptography used, how risky is that usage, what shouldbe migrated first, and what migration path should be considered?

Security and Privacy Notes

Local scans operate on the selected local project.

Public GitHub repositories are cloned temporarily for analysis.

Temporary GitHub scan directories are cleaned up after the pipelinecompletes.

Workflow installation requires an explicit GitHub token.

Normal GitHub scanning does not require write access.

Never commit GitHub tokens to source control.

Migration recommendations are planning guidance and should bevalidated against protocol, certificate, interoperability,performance, and key-lifecycle requirements.

Limitations

QuantumShield is a hackathon-scale security engineering tool, not areplacement for a full enterprise cryptographic inventory platform orformal security assessment.

Current limitations include:

GitHub scanning supports public HTTPS repositories.

Static source analysis cannot always determine the exact runtimecryptographic role.

Sensitivity, lifetime, and exposure can use deterministic defaultswhen context is insufficient.

Migration recommendations do not prove application compatibility.

The numerical risk score is a prioritization heuristic.

The dashboard is primarily an assessment and planning interfacerather than an automated remediation system.

Demo Flow

Open https://quantum-shield.streamlit.app/

Select GitHub Repository.

Scan a repository such ashttps://github.com/Neel-stack-deb/QuantumShield-demo-app.

Show the cryptographic inventory.

Show the risk landscape and explainability.

Run Migration What-If on a classical finding.

Show migration priorities and recommendations.

Show the GitHub Actions workflow and Code Scanning results.

Project Status

Status: Demo-ready

Cryptographic discovery scanner

Python AST + regex detection

Quantum risk assessment

Transparent risk scoring

PQC readiness score

Migration recommendation engine

Migration roadmap

Migration What-If simulator

GitHub repository scanning

CBOM export

SARIF export

GitHub Code Scanning integration

GitHub Actions workflow installation

Streamlit dashboard

Automated tests

Streamlit deployment

Why PQC Migration Matters

Post-quantum migration is not only about waiting for a future quantumcomputer. Harvest-now-decrypt-later (HNDL) risk means informationcaptured today may become decryptable by sufficiently capable quantumsystems in the future.

QuantumShield is built around a practical workflow:

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

License

Add the project's chosen license here before public release.
