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
participant "GitHub Repository" as Repo
participant "GitHub Actions" as CI
participant "Docker Engine" as Docker
participant "FastAPI Service" as API
participant "Health Test Script" as Test

Developer -> Repo : Push Code
Repo -> CI : Trigger Workflow
CI -> Docker : Build Docker Image
Docker -> API : Start FastAPI Server
CI -> Test : Run Health Check Test
Test -> API : GET /health
API --> Test : HTTP 200 Response
Test -> CI : Test Passed
CI --> Developer : CI Pipeline Success

@enduml
```