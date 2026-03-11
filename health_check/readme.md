# FastAPI Health Check CI/CD

This project demonstrates **automated API health testing using FastAPI, Docker, and GitHub Actions**.  
It provides a simple health endpoint and a CI pipeline that validates the API status code during every push.

The goal is to simulate how **API health monitoring works in real CI/CD pipelines**.

---

# Workflow Diagram

```plantuml
@startuml
title FastAPI CI/CD Health Check Workflow

actor Developer
participant "GitHub Repository (develop)" as Repo
participant "GitHub Actions" as CI
participant "Docker Engine" as Docker
participant "FastAPI Container" as API
participant "Test Runner Container" as Test
participant "QA Branch" as QA
participant "Manual Approval (Release button)" as Approval
participant "Production" as Prod

Developer -> Repo : Push to develop
Repo -> CI : Trigger workflow

CI -> Docker : Build FastAPI image (ENVIRONMENT=dev)
CI -> Docker : Start FastAPI container (port 8000)
CI -> Docker : Build test-runner image
CI -> Test : Run test-runner (host network)
Test -> API : GET /health
API --> Test : HTTP 200
Test -> CI : Tests pass
CI -> Docker : Stop & remove FastAPI container

CI -> QA : Promote develop to qa (force sync)
QA -> CI : Trigger QA workflow

CI -> Docker : Build FastAPI image (ENVIRONMENT=qa)
CI -> Docker : Start FastAPI container (port 8000)
CI -> Docker : Build test-runner image
CI -> Test : Run test-runner (host network)
Test -> API : GET /health
API --> Test : HTTP 200
Test -> CI : Tests pass
CI -> Docker : Stop & remove FastAPI container

CI -> Approval : Await manual approval (Release)
Approval -> CI : Approved
CI -> Prod : Deploy to production
CI --> Developer : Workflow success

@enduml
```
