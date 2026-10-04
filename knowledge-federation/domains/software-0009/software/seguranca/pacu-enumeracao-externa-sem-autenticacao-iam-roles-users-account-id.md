---
id: software.seguranca.tranche11.001024
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
fontes: ["https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md", "https://github.com/RhinoSecurityLabs/pacu/wiki/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Reconhecimento AWS **Sem Credenciais na Conta Alvo** no Pacu: Enumeração de Roles e Usuários via Validação de `AssumeRolePolicy` e `S3/KMS` Cross-Account

## Em uma frase
Como um atacante externo ou Red Teamer descobre quais nomes de `IAM Roles` e `IAM Users` existem dentro de uma conta AWS alvo conhecendo apenas o **Account ID de 12 dígitos** daquela conta — e **sem ter nenhuma credencial da conta alvo**?

## Por que importa
O Pacu automatiza essa técnica nos módulos **`iam__detect_honeytokens`**, **`iam__enum_users`** e **`iam__enum_roles`**: o segredo técnico está no comportamento de validação de ARNs da própria API da AWS! Quando você usa uma conta AWS controlada pelo próprio pentester para atualizar a política de confiança (`AssumeRolePolicyDocument`) de uma Role sua ou uma política de Bucket S3 / KMS especificando no campo `"Principal": {"AWS": "arn:aws:iam::<CONTA_ALVO>:role/<nome_teste>"}`, a API da AWS valida em tempo real no backend se aquele ARN existe na conta alvo!

## Como funciona
Se a Role ou Usuário **não existir** na conta alvo, a API da AWS rejeita a gravação da política com `MalformedPolicyDocument: Invalid principal in policy`; se a Role **existir**, a chamada tem sucesso (`200 OK`) — e o melhor para o atacante: **como a chamada foi feita na conta do próprio atacante, ela NÃO gera nenhum log no CloudTrail da conta alvo**!

## Exemplo
```bash
# Em laboratorio autorizado: demonstrar a enumeracao de nomes de IAM Roles de uma conta de teste usando uma conta auxiliar
pacu --session pentest-aws-lab \
  --module-name iam__enum_roles \
  --module-args="--account-id 111122223333 --word-list /usr/share/wordlists/aws-common-roles.txt" \
  --exec
```

## Limites e trade-offs
Além de descobrir se uma Role existe, o módulo `iam__enum_roles` tenta assumi-la (`sts:AssumeRole`) caso a política de confiança daquela Role tenha sido mal configurada permitindo `"Principal": {"AWS": "*"}` (qualquer conta da AWS!) sem exigir um `sts:ExternalId` secreto!

## Como verificar
Audite todas as suas IAM Roles com o **Prowler** ou **Steampipe (`aws_iam_role`)** para garantir que nenhuma Role confie em contas externas desconhecidas e exija sempre `sts:ExternalId` em integrações de terceiros.

## Conexões
- [[pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque]] — Veja também: Escalação de Privilégio no AWS IAM com Pacu (**`iam__privesc_scan`**): Anatomia dos **21+ Vetores Clássicos de Privesc (`PassRole`, `CreatePolicyVersion`, `AttachUserPolicy`)**.
- [[pacu-auditoria-monitoramento-cloudtrail-guardduty-config-deteccao]] — Veja também: Pacu vs Monitoramento AWS (**CloudTrail, GuardDuty, Config & CloudWatch**): Módulos de Enumeração (`detection__enum_services`) e Controles de Blindagem (SCPs).
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
