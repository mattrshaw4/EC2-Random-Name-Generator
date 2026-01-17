# EC2-Random-Name-Generator
AWS
# EC2 Name Generator

A Python-based tool for generating standardized EC2 instance names with department-based authorization controls.

## Overview

This project provides an automated solution for generating EC2 instance names following organizational naming conventions. By restricting name generation to authorized departments only, it ensures governance, security, and cost management across AWS resources.

## Benefits

### Standardization and Governance
- Enforces consistent naming conventions across the organization
- Prevents inconsistent or random naming schemes that complicate resource management
- Helps enforce tagging policies and cost allocation standards

### Security and Compliance
- Implements department-based access control for resource naming
- Prevents shadow IT scenarios where unauthorized teams create resources
- Creates an audit trail linking resources to requesting departments
- Supports compliance requirements for resource tracking and accountability

### Automation and Efficiency
- Automates the naming process to reduce manual errors
- Speeds up deployment workflows
- Integrates with CI/CD pipelines and Infrastructure as Code tools
- Eliminates dependency on outdated documentation

### Cost Management
- Enables department-based spending tracking through standardized naming patterns
- Simplifies identification of resource consumption by business unit
- Facilitates accurate cost allocation and chargeback processes

## Features

- **Department Authorization**: Only authorized departments can generate EC2 names
- **Batch Generation**: Create multiple instance names in a single operation
- **Naming Convention Enforcement**: Automatically applies organizational standards
