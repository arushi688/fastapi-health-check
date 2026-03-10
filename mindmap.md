# CI/CD Test Automation Platform for APIs

## Project Description

This project delivers a **GitHub Actions-based test automation framework** that automatically validates APIs on every Pull Request, acting as a deployment gate before promoting Docker images to QA and Production environments. The pipeline enforces quality gates at each stage: Developer → Pull Request → Automated Tests → Docker Image Build → QA Environment → Production Deployment.

---

## Mindmap

```plantuml
@startmindmap

title CI/CD Test Automation Platform for APIs

skinparam nodesep 20
skinparam ranksep 30
skinparam defaultFontSize 14
scale 0.8

* CI/CD Test Automation\nPlatform for APIs


** Testing Types
*** Functional Testing
**** Backend API Tests
**** Frontend Flows
*** Performance Testing
**** User Flows
**** Compliance
**** Timing Metrics
*** Load Testing
**** Concurrent Users
**** Stress Testing
**** Scalability
*** Code Coverage
**** Line Coverage
**** Branch Coverage
**** Coverage Threshold Gate (≥ 80%)

** CI/CD with GitHub Actions
*** Workflow Triggers

*** Install Dependencies

*** Run Test Suites

*** Generate Reports

*** Fail / Pass Gates

*** Artifacts Upload


** Docker & Containerization (Updated Flow)
*** Build Docker Image
*** Tag Image (Semantic Version)
*** Push to Registry
*** Pull Tagged Image
*** Run Tests Against Tagged Image
*** Promote Same Image (No Rebuild)


** Environments
*** Dev

*** CI Test Environment

*** QA / Staging

*** Production



** Quality Gates
*** Functional Pass Rate ≥ 95%
*** Coverage ≥ 80%
*** P95 within baseline
*** P99 within baseline
*** Error Rate < 0.1%
*** Load Stability ≥ X concurrent users
*** Quality Gate Logic (Complete)
**** A PR can merge only if:
***** Functional tests pass
***** Coverage ≥ 80%
***** No flaky tests
***** P95/P99 within threshold
***** Error rate < 0.1%
***** Docker image tagged & stored




** Top 10 Critical APIs (Monitoring Scope)
*** Selection Criteria:
**** Highest traffic
**** Revenue/business critical
**** Used by multiple services
**** Known historical instability
*** Example Table:
**** API Name | Service | Criticality | SLA (Target) | P95 | P99
**** /auth/login | Auth Service | High | < 300ms |  |  
**** /orders | Order Service | High | < 500ms |  |  
**** /payments | Payment Service | Critical | < 400ms |  |  
*** Success Criteria (API Monitoring):
**** Continuous monitoring of Top 10 APIs
**** P95 and P99 tracked per PR and per release
**** Alert if deviation >10% from baseline
**** Error rate <0.1% under normal load
@endmindmap
```

---


# CI/CD Test Automation Platform for APIs

## Project Gantt Chart (3 Iterations)

---

### Project Summary

| Attribute | Detail |
|---|---|
| **Project Duration** | 20 weeks (2026-03-01 to 2026-07-20) |
| **Objective** | Deliver a CI/CD test automation platform for APIs with quality gates, automated PR validation, and production-ready pipeline controls. |
| **Key Deliverables** | Requirements sign-off · CI workflow with gates · Core API test suite · Performance baseline (P95/P99) · Dockerized execution and registry integration · Executive demo and handoff |

---

```mermaid
gantt
  title CI/CD Test Automation Platform (3 Iterative Lifecycle Phases)
  dateFormat  YYYY-MM-DD
  axisFormat  %b %d
  excludes    weekends
  tickInterval 1week

  section Iteration 1 – Foundation (Mar 1 – Apr 10)
  Requirements Gathering & Scope        :i1a, 2026-03-01, 5d
  Analysis (Top APIs + Risk Study)      :i1b, after i1a, 5d
  Architecture & Framework Design       :i1c, after i1b, 5d
  CI Skeleton + Initial Tests           :i1d, after i1c, 5d
  Docker + Versioning Implementation    :i1e, after i1d, 5d
  Iteration 1 Review                    :i1f, after i1e, 3d
  Iteration 1 Complete (Milestone)      :milestone, m1, after i1f, 0d

  section Iteration 2 – Quality & Performance (Apr 13 – Jun 05)
  Enhanced Test Design                  :i2a, 2026-04-13, 5d
  Functional + Edge Case Testing        :i2b, after i2a, 8d
  Performance & Load Implementation     :i2c, after i2b, 8d
  Coverage Gates + Metrics Integration  :i2d, after i2c, 5d
  Iteration 2 Review                    :i2e, after i2d, 3d
  Iteration 2 Complete (Milestone)      :milestone, m2, after i2e, 0d

  section Iteration 3 – Integration & Release (Jun 08 – Jul 20)
  Promotion Workflow Design             :i3a, 2026-06-08, 5d
  QA/Registry Integration Implementation :i3b, after i3a, 7d
  Reporting + Executive Dashboard       :i3c, after i3b, 5d
  Full Pipeline Testing & Stabilization :i3d, after i3c, 5d
  Deployment Automation Setup           :i3e, after i3d, 5d
  Production Readiness Review           :i3f, after i3e, 3d
  Maintenance & Handoff                 :i3g, after i3f, 3d
  Production-Ready Gate (Milestone)     :milestone, m3, 2026-07-20, 0d
```

### Key Milestones by Iteration
- **Iteration 1 – Foundation:** CI skeleton operational, initial API tests running in GitHub Actions, Docker build/versioning in place, Iteration 1 review complete.
- **Iteration 2 – Quality & Performance:** Functional + edge-case suite expanded, performance/load tests integrated, coverage gates and metrics enforced, Iteration 2 review complete.
- **Iteration 3 – Integration & Release:** Promotion workflow and registry integration complete, reporting/dashboard delivered, full pipeline stabilized, production-ready gate achieved.

# Phase 1 – Scope & Success Criteria

## 1. Problem Statement
- Current API testing is fragmented, largely manual, and inconsistent across teams and services.
- CI/CD validation gaps allow regressions to pass through PRs without reliable automated gates.
- Manual or inconsistent regression testing introduces release risk, longer feedback cycles, and quality drift.
- Performance baselining and automated quality gates are needed to enforce objective release thresholds.

## 2. Project Scope

### In Scope
- Automated functional API tests (core business flows)
- Edge case and data contract validation
- CI workflow skeleton and execution pipeline
- Performance benchmarks (P95/P99)
- Load and stress test scenarios
- Dockerized test execution
- CI quality gates integration
- Reporting and dashboards

### Out of Scope
- UI automation
- Full end-to-end system testing across external dependencies
- Production performance testing
- Security penetration testing (unless explicitly added later)


## 3. Success Criteria (Measurable Outcomes)
- ≥80% functional API coverage for core services
- Test suite execution time under 10 minutes in CI
- <5% flaky test rate
- Automated performance baseline established (P95/P99)
- CI pipeline blocks merges on failed tests
- Fully dockerized and reproducible execution
- Reporting dashboard available to engineering stakeholders
- All Docker images use semantic versioning
- Build metadata traceable to commit SHA
- Release tags created on production promotion
- Continuous monitoring of Top 10 APIs
- P95 and P99 tracked per PR and per release
- Alert if deviation >10% from baseline
- Error rate <0.1% under normal load

# Semantic Versioning
- Version Format: MAJOR.MINOR.PATCH-BUILD (e.g., 1.4.2-156)
- MAJOR: Breaking API change
- MINOR: New backward-compatible feature
- PATCH: Bug fix
- BUILD: CI run number
- Extract version from package.json or file, append ${{ github.run_number }}
- Example final tag: 1.3.0-245

# Final Architecture Flow
Developer
  ↓
PR Created
  ↓
Build + Tag Image (Semantic Version)
  ↓
Push to Registry
  ↓
Pull Same Image
  ↓
Run Tests (Functional + Coverage + Performance)
  ↓
Quality Gates
  ↓
Promote to QA
  ↓
Production Approval

## 4. Risks & Dependencies
- API instability during development
- Environment reliability issues
- CI runner capacity constraints
- Incomplete API documentation
- Test data management challenges
