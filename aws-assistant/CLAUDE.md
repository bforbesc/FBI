# AWS ML Engineer Assistant

An AWS expert skill for ML engineers. Answers questions about AWS services, quotas, pricing, instance types, and architecture decisions — grounded in live AWS API data, not training knowledge.

## What it does

- Recommends the right AWS service for ML workloads (SageMaker, Bedrock, EC2, Lambda, ECS/EKS)
- Queries live service quotas and limits via the AWS Service Quotas API
- Looks up pricing via the AWS Pricing API
- Verifies instance specs (GPU type, memory, vCPUs) from the live EC2 API
- Inspects deployed resources in your account
- Handles expired SSO credentials via an auto-login flow using Claude in Chrome

## Usage

Invoke via `SKILL.md` in Claude Cowork, or directly in Claude Code from this directory.

| What you say | What it does |
|---|---|
| "Should I use SageMaker or Bedrock for this?" | Service recommendation with tradeoffs |
| "What are my SageMaker quotas in us-east-1?" | Live quota lookup via Service Quotas API |
| "What does a g5.xlarge cost?" | Live pricing via AWS Pricing API |
| "What instance type for training a 7B model?" | Instance recommendation with verified specs |
| "What's currently deployed in my account?" | Live inspection of endpoints, models, functions |

## Requirements

- **AWS MCP Server** with `mcp__AWS_API_MCP_Server__call_aws` and `mcp__AWS_API_MCP_Server__suggest_aws_commands`
- **Claude in Chrome MCP** (optional) — for SSO auto-login flow
- AWS credentials configured with a named profile (SSO or static)

## Setup

In `SKILL.md`, replace before use:

- `<YOUR_AWS_PROFILE>` — your AWS CLI profile name (e.g. `default`, `prod`, `dev`)
- `<YOUR_SSO_URL>` — your AWS SSO portal URL (only needed if using SSO credentials)

## File structure

```
aws-assistant/
├── CLAUDE.md                  ← this file (Claude Code + Cowork context)
├── SKILL.md                   ← skill definition and instructions
└── aws-commands-reference.md  ← quick reference for common AWS CLI commands
```
