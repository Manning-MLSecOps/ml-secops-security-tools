# ML SecOps Security Tools

This repository contains reusable security utilities for Secure MLOps pipelines, with a focus on healthcare and regulated environments.

## Purpose

These tools are designed to enforce security and configuration integrity **before** ML training, model packaging, or deployment occurs.

Primary goals:
- Prevent insecure pipeline configuration
- Enforce deterministic and auditable controls
- Reduce ML supply-chain and CI/CD risks

## Current Tools

### Secure Config Checker
Validates pipeline configuration files against a strict schema to ensure:
- Required security controls are present
- Unsafe or missing settings are rejected early
- Misconfigurations fail fast in CI

## Usage (Local)

```bash
pip install -r requirements.txt
python validate_config.py pipeline_config.json
