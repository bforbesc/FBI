# AWS Commands Reference

Common AWS CLI commands used by the assistant. Always append `--profile <YOUR_AWS_PROFILE>` to every command.

## Credentials Check

```bash
aws sts get-caller-identity --profile <YOUR_AWS_PROFILE>
```

## Service Quotas

List all quotas for a service:
```bash
aws service-quotas list-service-quotas --service-code <service-code> --profile <YOUR_AWS_PROFILE>
```

Common service codes:
- `sagemaker` — SageMaker
- `lambda` — Lambda
- `s3` — S3
- `ec2` — EC2
- `bedrock` — Bedrock

## Pricing

```bash
aws pricing get-products --service-code <service-code> --filters <filters> --region us-east-1 --profile <YOUR_AWS_PROFILE>
```

> Note: The Pricing API is only available in `us-east-1` and `ap-south-1`.

Common service codes for pricing:
- `AmazonSageMaker`
- `AmazonEC2`
- `AWSLambda`
- `AmazonS3`
- `AmazonBedrock`

## EC2 Instance Types

Describe a specific instance type:
```bash
aws ec2 describe-instance-types --instance-types <instance-type> --profile <YOUR_AWS_PROFILE>
```

Describe a whole family (e.g., all g5 types):
```bash
aws ec2 describe-instance-types --filters Name=instance-type,Values=g5.* --profile <YOUR_AWS_PROFILE>
```

The response includes `GpuInfo`, `VCpuInfo`, `MemoryInfo`, and `NetworkInfo` — use these as the authoritative source.

## Inspect Deployed Resources

```bash
# SageMaker endpoints
aws sagemaker list-endpoints --profile <YOUR_AWS_PROFILE>

# SageMaker models
aws sagemaker list-models --profile <YOUR_AWS_PROFILE>

# Running EC2 instances
aws ec2 describe-instances --filters Name=instance-state-name,Values=running --profile <YOUR_AWS_PROFILE>

# Lambda functions
aws lambda list-functions --profile <YOUR_AWS_PROFILE>

# S3 buckets
aws s3api list-buckets --profile <YOUR_AWS_PROFILE>
```

## MCP Tool Usage

Use `suggest_aws_commands` to explore services and identify the right CLI commands, then use `call_aws` to execute them. This is the preferred pattern for any question about AWS service capabilities or configurations.
