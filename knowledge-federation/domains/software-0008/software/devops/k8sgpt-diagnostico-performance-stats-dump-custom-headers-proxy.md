---
id: software.devops.tranche15.001430
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md", "https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md", "https://github.com/k8sgpt-ai/k8sgpt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K8sGPT: estatísticas de latência por analisador (`-s`), captura de diagnóstico (`dump`) e proxies corporativos

## Em uma frase
O K8sGPT oferece ferramentas nativas de observabilidade e rede corporativa, incluindo medição de tempo de execução por analisador (`k8sgpt analyze -s`), geração de pacotes de suporte (`k8sgpt dump`) e suporte a cabeçalhos HTTP customizados e proxies.

## Por que importa
Em ambientes empresariais onde chamadas a LLMs passam por gateways de IA internos ou proxies HTTPS autenticados, e onde clusters com milhares de Pods exigem profiling de performance dos analisadores, esses controles viabilizam a operação segura.

## Como funciona
A flag `-s` (`--stats`) imprime a duração exata em milissegundos ou segundos de cada analisador; `k8sgpt dump` grava um arquivo local `dump_<timestamp>_json` com informações de diagnóstico; `--custom-headers Chave:Valor` injeta cabeçalhos nas requisições ao LLM; e `spec.ai.proxyEndpoint` no Operator roteia o tráfego por proxies corporativos.

## Exemplo
```bash
k8sgpt analyze -s --namespace=kube-system
k8sgpt analyze --explain --custom-headers X-Org-Gateway:devops-prod
k8sgpt dump
```

## Limites e trade-offs
O comando `k8sgpt dump` gera um arquivo JSON local contendo estado da configuração e resultados de análise; revise e sanitize esse arquivo antes de anexá-lo em issues públicas no GitHub.

## Como verificar
Execute `k8sgpt analyze -s` e identifique quais analisadores (como `Pod` ou `Service`) consomem a maior fração do tempo de varredura no cluster.

## Conexões
- [[k8sgpt-integrations-trivy-prometheus-sinks-slack-backstage]] — Veja também: K8sGPT: integrações com Trivy, Prometheus, sinks de notificação Slack e catálogo Backstage.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
