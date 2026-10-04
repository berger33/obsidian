---
id: software.devops.tranche20.001957
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/Infisical/infisical/main/README.md", "https://infisical.com/docs/integrations/platforms/kubernetes/overview", "https://github.com/Infisical/infisical"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Infisical Governança de Segredos: `Secret Rotation` automática, `Point-in-Time Recovery` e detecção de intrusão com `Honey Tokens`

## Em uma frase
O pilar de gerenciamento de segredos do Infisical combina três mecanismos avançados de defesa em profundidade: **Secret Rotation** (rotação programada de credenciais em PostgreSQL, MySQL, AWS IAM, Auth0, etc.), **Point-in-Time Recovery (PITR)** (rollback do estado completo de um projeto) e **Honey Tokens** (credenciais isca para detecção de intrusão).

## Por que importa
Apenas guardar segredos em um cofre não protege contra duas ameaças reais: 1) uma alteração humana acidental que apaga ou corrompe 30 variáveis de produção antes de um deploy; e 2) um invasor que compromete um runner de CI e faz dump de todas as variáveis de ambiente do projeto.

## Como funciona
Com **Point-in-Time Recovery**, o administrador visualiza o diff exato de todos os commits de segredos do ambiente e restaura o projeto para qualquer timestamp anterior em um clique. Já ao plantar um **Honey Token** (uma credencial falsa monitorada junto aos segredos reais), no exato instante em que um atacante tenta usá-la, o Infisical dispara um alerta imediato identificando o vazamento.

## Exemplo
```bash
# Consultando o histórico de versões ou restaurando configurações via CLI/API do Infisical:
infisical secrets get DATABASE_URL --env=prod --path=/backend
```

## Limites e trade-offs
Plante Honey Tokens com nomes plausíveis (ex.: `LEGACY_BACKUP_AWS_KEY`) nos mesmos caminhos acessados por runners de CI/CD para detectar exfiltração de variáveis de ambiente com zero falsos positivos.

## Como verificar
Verifique no painel de *Commits / Point-in-Time Recovery* do projeto que cada alteração de segredo registra autor, timestamp e versão anterior.

## Conexões
- [[infisical-secret-scanning-leak-prevention-git-pre-commit-ci]] — Veja também: Infisical Secret Scanning e Leak Prevention (`infisical scan`): detecção preventiva de vazamentos em commits Git e pipelines CI.
- [[infisical-pki-private-external-ca-acme-est-code-signing]] — Veja também: Infisical Certificate Management (PKI) e Code Signing: operação de CA Interna/Externa, ACME, EST e assinatura de artefatos.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
