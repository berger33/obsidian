---
id: software.seguranca.tranche05.000447
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/paralus/paralus/main/README.md", "https://www.paralus.io/docs/", "https://www.paralus.io/docs/usage/audit-logs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF Paralus: Automação Declarativa (*RBAC-as-Code*) com a CLI `pctl` e API REST em Pipelines GitOps

## Em uma frase
A ferramenta de linha de comando **`pctl`** (`paralus/cli`) e a API REST do Paralus permitem gerenciar projetos, clusters, grupos, usuários e políticas de acesso de forma totalmente declarativa a partir de pipelines de CI/CD e fluxos GitOps.

## Por que importa
Impede alterações manuais não rastreadas (*ClickOps*) nas permissões de acesso aos clusters: toda concessão de papel `NAMESPACE_ADMIN` ou criação de `Custom Role` passa por revisão de Pull Request no Git antes de ser aplicada pelo `pctl`.

## Como funciona
O `pctl` autentica-se no Paralus Core usando um perfil de configuração JSON (contendo a `API Key` e `API Secret` de uma conta de automação de CI) e suporta operações idempotentes sobre projetos, grupos e associações de permissões.

## Exemplo
```bash
# Verificar a configuração do perfil da CLI pctl e listar todos os clusters do projeto em JSON
pctl version
pctl get clusters --project "payments-platform" -o json | jq '.items[].metadata.name'
```

## Limites e trade-offs
Chaves de API (`API Key` / `API Secret`) usadas pelo `pctl` em pipelines de GitOps possuem privilégios elevados de administração de acesso; armazene-as em cofres de segredos (Vault/OpenBao) e rotacione-as periodicamente.

## Como verificar
Execute `pctl get projects` usando o perfil de CI e confirme que o estado dos projetos e grupos no Paralus coincide com as definições versionadas no repositório.

## Conexões
- [[paralus-terminal-web-prompt-sessoes-efemeras-browser-kubectl]] — Veja também: CNCF Paralus: Acesso `kubectl` Browser-Based via Componente `Prompt` (Sessões Efêmeras sem Credenciais no Desktop).
- [[paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem]] — Veja também: CNCF Paralus: Trilhas de Auditoria Imutáveis (`System Audit Logs` e `Kubectl / Relay Audit Logs`) para Conformidade e SIEM.
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Referência cruzada direta com paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager.
- [[paralus-organizacao-projects-groups-custom-roles-namespace-rbac]] — Referência cruzada direta com paralus-organizacao-projects-groups-custom-roles-namespace-rbac.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
