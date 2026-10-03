---
id: software.seguranca.tranche11.001023
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

# Escalação de Privilégio no AWS IAM com Pacu (**`iam__privesc_scan`**): Anatomia dos **21+ Vetores Clássicos de Privesc (`PassRole`, `CreatePolicyVersion`, `AttachUserPolicy`)**

## Em uma frase
A pesquisa seminal da **Rhino Security Labs** que deu origem ao módulo **`iam__privesc_scan`** do Pacu catalogou **mais de 21 métodos distintos de Escalação de Privilégio no AWS IAM**, demonstrando como permissões aparentemente inofensivas permitem que um usuário comum se torne `AdministratorAccess` da conta AWS!

## Por que importa
Como funciona o **`run iam__privesc_scan`**? Ele lê as permissões do usuário/role atual já salvas no banco SQLite da sessão (pelo `iam__enum_permissions`) — **sem fazer nenhuma chamada extra na AWS durante a análise!** — e verifica se a identidade possui qualquer uma das combinações perigosas.

## Como funciona
Veja os 4 grupos de vetores mais críticos detectados pelo `iam__privesc_scan`: **(1) Mutação Direta de Políticas IAM**: `iam:CreatePolicyVersion` (cria uma nova versão da própria política com `"Action": "*", "Resource": "*"` e define `SetAsDefault=true`), `iam:SetDefaultPolicyVersion`, `iam:AttachUserPolicy` / `iam:AttachGroupPolicy` / `iam:AttachRolePolicy` e `iam:PutUserPolicy`; **(2) Credenciais de Outras Identidades**: `iam:CreateAccessKey`, `iam:CreateLoginProfile` / `iam:UpdateLoginProfile` e `iam:UpdateAssumeRolePolicy`; **(3) `iam:PassRole` + Serviço de Computação**: passar uma Role privilegiada para uma nova instância EC2 (`ec2:RunInstances`), função Lambda (`lambda:CreateFunction` + `lambda:InvokeFunction`), job Glue (`glue:CreateDevEndpoint`) ou CloudFormation (`cloudformation:CreateStack`); e **(4) Edição de Código de Serviços Existentes**: `lambda:UpdateFunctionCode` em uma função Lambda que já possui uma Role privilegiada!

## Exemplo
```bash
# Analisar offline as permissoes ja enumeradas na sessao para identificar caminhos de escalacao de privilegio (iam__privesc_scan)
pacu --session pentest-aws-lab \
  --module-name iam__privesc_scan \
  --module-args="--scan-only" \
  --exec
```

## Limites e trade-offs
Observe a flag **`--scan-only`** no comando acima: para auditorias defensivas e Purple Team, rodar `iam__privesc_scan --scan-only` identifica e reporta todos os caminhos de escalação de privilégio existentes nas identidades da conta **sem executar a exploração ativa**!

## Como verificar
Como defesa arquitetural na AWS, utilize **IAM Permissions Boundaries** e restrinja estritamente o recurso (`Resource`) em qualquer permissão `iam:PassRole` apenas às Roles específicas de trabalho (nunca `"Resource": "*"`).

## Conexões
- [[pacu-gestao-credenciais-set-keys-import-keys-whoami-bruteforce-permissions]] — Veja também: Reconhecimento Furtivo de Permissões no Pacu: `set_keys`, `import_keys`, `whoami` e **`iam__bruteforce_permissions` / `iam__enum_permissions`**.
- [[pacu-enumeracao-externa-sem-autenticacao-iam-roles-users-account-id]] — Veja também: Reconhecimento AWS **Sem Credenciais na Conta Alvo** no Pacu: Enumeração de Roles e Usuários via Validação de `AssumeRolePolicy` e `S3/KMS` Cross-Account.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s]] — Referência cruzada direta com cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
