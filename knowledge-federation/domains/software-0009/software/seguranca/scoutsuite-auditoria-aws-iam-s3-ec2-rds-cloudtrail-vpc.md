---
id: software.seguranca.tranche11.001012
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Scout Suite na **AWS (`scout aws`)**: Escopo de Serviços (`--services`), Regiões (`--regions`), Controle de Taxa (`--max-rate`) e Mínimo Privilégio IAM

## Em uma frase
Ao auditar uma conta **Amazon Web Services** com **`scout aws`**, o coletor interroga dezenas de serviços nativos (IAM, S3, EC2, VPC, RDS, Redshift, ElastiCache, CloudTrail, CloudWatch, Config, KMS, Lambda, EFS, ELB/ELBv2,GuardDuty, Route53, SES, SNS, SQS, Secrets Manager, SSM, etc.).

## Por que importa
Conforme mostra a implementação oficial em `ScoutSuite/__main__.py`, você controla com precisão cirúrgica o comportamento da coleta usando quatro conjuntos de parâmetros: **(1) Autenticação** (`--profile`, ou `--aws-access-key-id`, `--aws-secret-access-key` e `--aws-session-token`); **(2) Filtro de Serviços** (`--services iam s3 ec2 rds` para auditar apenas serviços selecionados, `--skipped-services` para pular serviços lentos, ou `--list-services` para listar os módulos disponíveis); **(3) Filtro de Regiões** (`--regions us-east-1 sa-east-1` ou `--excluded-regions`); e **(4) Controle de Concorrência e Rate Limit** (`--max-workers 10` e **`--max-rate <req_por_segundo>`** via `Throttler` assíncrono para evitar `ThrottlingException` nas APIs da AWS!)!

## Como funciona
Quais permissões IAM o auditor precisa na conta alvo? Basta anexar as duas políticas gerenciadas oficiais somente-leitura da AWS: **`SecurityAudit`** e **`ViewOnlyAccess`**!

## Exemplo
```bash
# Auditar especificamente IAM, S3, EC2, RDS, KMS e CloudTrail nas regioes us-east-1 e sa-east-1 limitando a 20 chamadas/segundo
scout aws \
  --profile auditoria-secops \
  --services iam s3 ec2 rds kms cloudtrail vpc \
  --regions us-east-1 sa-east-1 \
  --max-workers 10 \
  --max-rate 20 \
  --no-browser
```

## Limites e trade-offs
Por que usar **`--max-rate 20`** é uma prática recomendada ao auditar contas AWS compartilhadas com sistemas de produção críticos? Porque a API `aws iam` é global e compartilha cotas de *rate limit* (`GetPolicyVersion`, `ListAttachedRolePolicies`) com toda a conta: limitar a taxa no `Throttler` do Scout Suite garante que a auditoria nunca cause *throttling* em deploys ou microsserviços!

## Como verificar
Para listar todos os serviços suportados pelo provedor AWS antes da execução, rode `scout aws --list-services`.

## Conexões
- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — Veja também: **NCC Group Scout Suite (`nccgroup/ScoutSuite`)**: Arquitetura de Auditoria de Postura de Segurança Multi-Cloud Assíncrona e **Inspeção 100% Offline**.
- [[scoutsuite-auditoria-azure-rbac-entra-storage-network-keyvault]] — Veja também: Scout Suite no **Microsoft Azure (`scout azure`)**: Modos de Autenticação (`--cli`, `--msi`, `--service-principal`) e Varredura Multi-Subscription.
- [[scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs]] — Referência cruzada direta com scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
