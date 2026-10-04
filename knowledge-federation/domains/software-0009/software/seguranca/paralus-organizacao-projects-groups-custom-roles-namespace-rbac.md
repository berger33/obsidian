---
id: software.seguranca.tranche05.000443
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

# CNCF Paralus: Modelo Multi-Tenant com `Projects`, `Groups`, Papéis Pré-Configurados e `Custom Roles` por Namespace

## Em uma frase
O Paralus organiza o controle de acesso em uma hierarquia lógica de **Organization -> Projects -> Clusters / Namespaces**, vinculando **Users** e **Groups** a papéis de nível de projeto (`PROJECT_ADMIN`, `PROJECT_READ_ONLY`, `INFRA_ADMIN`) ou de nível de namespace (`NAMESPACE_ADMIN`, `NAMESPACE_READ_ONLY`) e **Custom Roles**.

## Por que importa
Sem uma camada central de abstração, conceder a uma equipe de desenvolvimento permissão de leitura apenas no namespace `payments` em 15 clusters exigiria criar e manter 15 `Roles` e `RoleBindings` separadamente; no Paralus, uma única associação de grupo aplica e sincroniza o RBAC em todos os clusters do projeto.

## Como funciona
Quando um usuário recebe `NAMESPACE_READ_ONLY` para o namespace `payments` em um projeto, o Paralus provisiona dinamicamente no cluster alvo apenas as permissões equivalentes de leitura restritas àquele namespace, impedindo qualquer visibilidade sobre outros namespaces ou recursos cluster-wide.

## Exemplo
```bash
# Criar um novo projeto de isolamento e listar os papéis (roles) disponíveis via CLI pctl
pctl create project "payments-platform" --description "Clusters da vertical de pagamentos"
pctl get roles
```

## Limites e trade-offs
Evite conceder `ADMIN` (nível de organização) ou `CLUSTER_ADMIN` para equipes de desenvolvimento de aplicações; utilize sempre papéis com escopo de namespace (`NAMESPACE_ADMIN` / `NAMESPACE_READ_ONLY`) ou `Custom Roles` restritas aos grupos de API necessários.

## Como verificar
Teste com uma conta vinculada a `NAMESPACE_READ_ONLY` no namespace `payments`: confirme que `kubectl get pods -n payments` funciona e que `kubectl get secrets -n kube-system` retorna `Forbidden`.

## Conexões
- [[paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in]] — Veja também: CNCF Paralus: Conexão Segura de Clusters Privados via Relay Agent (Túnel mTLS Outbound sem Expor o `kube-apiserver`).
- [[paralus-federacao-sso-oidc-okta-entra-github-mapeamento-grupos]] — Veja também: CNCF Paralus: Federação SSO com Provedores OIDC (Okta, Microsoft Entra ID, Google, Keycloak e GitHub) e Mapeamento de Grupos.
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Referência cruzada direta com paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager.
- [[paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao]] — Referência cruzada direta com paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
