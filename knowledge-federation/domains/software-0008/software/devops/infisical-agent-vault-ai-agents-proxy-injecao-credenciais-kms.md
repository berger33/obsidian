---
id: software.devops.tranche20.001959
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

# Infisical `Infisical Agent`, `Agent Vault` (para IA) e `KMS`: injeção de segredos sem SDK e proteção contra exfiltração por LLMs

## Em uma frase
O ecossistema Infisical oferece três mecanismos para aplicações e agentes que não devem carregar o SDK nem reter credenciais brutas: o **`Infisical Agent`** (daemon sidecar que autentica e renderiza templates de arquivos em disco), o **`Infisical KMS`** (criptografia simétrica/assimétrica via API) e o **`Agent Vault`** (proxy de saída para agentes de IA).

## Por que importa
Em arquiteturas modernas com agentes de IA autônomos (LLMs com execução de ferramentas), entregar uma chave real de API (`OPENAI_API_KEY`, `GITHUB_TOKEN`, `STRIPE_KEY`) no ambiente do agente permite que um ataque de *prompt injection* instrua o agente a imprimir ou exfiltrar a credencial.

## Como funciona
Com o **Agent Vault** (`Infisical/agent-vault`), os agentes de IA nunca recebem as credenciais reais: todas as requisições HTTP de saída do agente passam por um proxy controlado que valida a política e injeta o segredo real no cabeçalho apenas no momento de encaminhar ao destino externo.

## Exemplo
```yaml
# Exemplo de configuração do Infisical Agent renderizando um arquivo de configuração:
infisical:
  address: "https://app.infisical.com"
auth:
  type: "universal-auth"
  config:
    client-id: "/etc/infisical/client-id"
    client-secret: "/etc/infisical/client-secret"
templates:
  - source-path: "/etc/infisical/app.conf.tpl"
    destination-path: "/etc/app/app.conf"
```

## Limites e trade-offs
Ao usar o `Infisical Agent` em VMs ou containers legados, configure `remove-client-secret-on-read: true` quando aplicável para que o segredo de bootstrap não permaneça em disco após a autenticação inicial.

## Como verificar
Verifique o arquivo renderizado em `destination-path` pelo `Infisical Agent` e monitore as métricas do agente.

## Conexões
- [[infisical-pki-private-external-ca-acme-est-code-signing]] — Veja também: Infisical Certificate Management (PKI) e Code Signing: operação de CA Interna/Externa, ACME, EST e assinatura de artefatos.
- [[infisical-operator-metricas-prometheus-serviceaccount-customizada-producao]] — Veja também: Infisical Operator em Produção: métricas Prometheus (`/metrics`), `ServiceAccount` customizada e migração `v1alpha1` -> `v1beta1`.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
