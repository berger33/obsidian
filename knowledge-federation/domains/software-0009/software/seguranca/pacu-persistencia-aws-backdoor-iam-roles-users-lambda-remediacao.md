---
id: software.seguranca.tranche11.001029
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

# Análise de Técnicas de **Persistência em AWS IAM** Mapeadas pelo Pacu (`iam__backdoor_*`) e Playbook de **Erradicação e Resposta a Incidentes (DFIR)**

## Em uma frase
Durante uma investigação forense de comprometimento de conta AWS, um erro grave de resposta a incidentes é apenas revogar a chave `AKIA...` inicial que vazou e dar o incidente por encerrado — sem verificar se o invasor já implantou mecanismos de **Persistência no IAM**!

## Por que importa
Os módulos da família **`iam__backdoor_*`** do Pacu demonstram exatamente onde um atacante esconde acesso persistente em uma conta AWS: **(1) `iam__backdoor_assume_role`** — adiciona um segundo `Statement` discreto na `AssumeRolePolicyDocument` (*Trust Policy*) de uma IAM Role legítima existente, permitindo que uma conta AWS externa do atacante assuma aquela Role a qualquer momento via `sts:AssumeRole`!; **(2) `iam__backdoor_users_keys`** — cria uma **segunda `AccessKey`** (`iam:CreateAccessKey`) em usuários IAM existentes que tinham apenas 1 chave ativa!; e **(3) `iam__backdoor_users_password`** — adiciona um `LoginProfile` (senha de console) a usuários IAM de serviço que antes só usavam API!

## Como funciona
Para erradicar completamente um adversário de uma conta AWS durante um incidente de DFIR, o analista deve auditar sistematicamente todas as políticas de confiança (`AssumeRolePolicyDocument`), chaves de acesso secundárias, perfis de login recém-criados e versões não-padrão de políticas gerenciadas!

## Exemplo
```bash
# Comandos de Resposta a Incidentes (DFIR / Blue Team) com AWS CLI e jq para cacar backdoors em Trust Policies de IAM Roles
aws iam list-roles --output json | \
  jq -r '.Roles[] | select(.AssumeRolePolicyDocument.Statement[].Principal.AWS != null) | "\(.RoleName): \(.AssumeRolePolicyDocument.Statement[].Principal.AWS)"'
```

## Limites e trade-offs
Guarde a consulta `aws iam list-roles | jq ...` acima no seu **Playbook de Resposta a Incidentes Cloud**: ao responder a um comprometimento de credencial AWS, audite obrigatoriamente **(1)** todas as `AssumeRolePolicyDocument` de todas as Roles da conta em busca de Account IDs externos desconhecidos, **(2)** todos os usuários IAM com 2 `AccessKeys` ativas, **(3)** novas versões de políticas IAM (`CreatePolicyVersion`), e **(4)** funções Lambda modificadas recentemente (`LastModified`)!

## Como verificar
Use também o **CloudQuery** (em modo `write_mode: append`) ou o **AWS Config** para comparar o diff exato de todas as políticas IAM antes e depois do incidente.

## Conexões
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Veja também: Detecção de **Honeytokens / Canarytokens AWS** (`iam__detect_honeytokens`) e Como Projetar **Decoys de Credenciais AWS Indetectáveis** para o Blue Team.
- [[pacu-automacao-purple-team-aws-cloudtrail-sigma-guardduty-validacao]] — Veja também: Engenharia de Detecção (**Purple Team AWS**) com Pacu: Como Validar Regras **Sigma (`aws_cloudtrail`)** e Alertas do **Amazon GuardDuty**.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque]] — Referência cruzada direta com pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque.
- [[cloudquery-deteccao-drift-historico-temporal-snapshots-sql]] — Referência cruzada direta com cloudquery-deteccao-drift-historico-temporal-snapshots-sql.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
