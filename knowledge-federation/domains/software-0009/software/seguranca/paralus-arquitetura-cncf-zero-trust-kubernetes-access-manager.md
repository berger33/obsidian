---
id: software.seguranca.tranche05.000441
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

# CNCF Paralus: Arquitetura de Gerenciamento de Acesso Zero-Trust para Frotas de Clusters Kubernetes

## Em uma frase
**Paralus** (`paralus/paralus`, projeto CNCF Sandbox sob Apache-2.0) é uma plataforma open-source de gerenciamento de acesso Zero-Trust ao Kubernetes que centraliza a autenticação SSO/OIDC, a autorização RBAC multi-cluster e a auditoria completa de comandos `kubectl` através de GUI, CLI (`pctl`) e API REST.

## Por que importa
Elimina a distribuição perigosa de arquivos `kubeconfig` estáticos de longa validade (ou certificados `system:masters` compartilhados) e remove a necessidade de expor o `kube-apiserver` de clusters privados na internet pública.

## Como funciona
O plano central do Paralus (integrado ao Ory Kratos para identidade e PostgreSQL para persistência) comunica-se com os clusters gerenciados através de um **Relay Agent** leve implantado dentro de cada cluster. O agente estabelece um túnel mTLS *outbound* (dial-out) para o Paralus Core, permitindo que desenvolvedores usem seu `kubectl` nativo passando pelo proxy Zero-Trust do Paralus.

## Exemplo
```bash
# Instalar o plano de controle do Paralus em Kubernetes usando o chart Helm oficial
helm repo add paralus https://paralus.github.io/helm-charts
helm repo update

helm upgrade --install paralus paralus/ztka \
  --namespace paralus --create-namespace \
  --set fqdn.domain="paralus.internal.corp"
```

## Limites e trade-offs
O banco PostgreSQL do Paralus armazena políticas de RBAC de toda a frota de clusters e trilhas de auditoria; proteja-o com criptografia em repouso, conexões TLS obrigatórias e backups regulares.

## Como verificar
Execute `kubectl -n paralus get pods` e confirme que os serviços core (`paralus`, `relay-server`, `kratos`, `prompt`) estão em estado `Running`.

## Conexões
- [[paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in]] — Veja também: CNCF Paralus: Conexão Segura de Clusters Privados via Relay Agent (Túnel mTLS Outbound sem Expor o `kube-apiserver`).
- [[paralus-organizacao-projects-groups-custom-roles-namespace-rbac]] — Referência cruzada direta com paralus-organizacao-projects-groups-custom-roles-namespace-rbac.
- [[paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem]] — Referência cruzada direta com paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
