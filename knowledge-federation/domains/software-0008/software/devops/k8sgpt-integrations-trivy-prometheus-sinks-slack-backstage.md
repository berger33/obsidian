---
id: software.devops.tranche15.001429
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

# K8sGPT: integrações com Trivy, Prometheus, sinks de notificação Slack e catálogo Backstage

## Em uma frase
O K8sGPT estende seus analisadores nativos por meio do subsistema `k8sgpt integrations` (como Trivy e Prometheus) e encaminha resultados do operador para sinks como webhooks do Slack e plugins do Backstage.

## Por que importa
Permite unificar na mesma interface de triagem tanto problemas operacionais de Kubernetes (Pods em crash, PVCs pendentes) quanto vulnerabilidades de segurança detectadas pelo Trivy e alertas de configuração do Prometheus.

## Como funciona
Na CLI, o operador gerencia extensões com `k8sgpt integrations list`, `k8sgpt integrations activate trivy` e `k8sgpt analyze --filter=VulnerabilityReport`. No CR `K8sGPT` do operador, é possível habilitar `spec.integrations.trivy`, configurar `spec.sink` (com URL de webhook protegida em Secret) e ativar `spec.extraOptions.backstage.enabled: true`.

## Exemplo
```bash
k8sgpt integrations list
k8sgpt integrations activate trivy
k8sgpt analyze --filter=VulnerabilityReport
```

## Limites e trade-offs
Ativar a integração do Trivy via CLI ou Operator instala ou consulta CRDs de relatórios de vulnerabilidades no cluster; verifique o namespace configurado (`spec.integrations.trivy.namespace`) para evitar duplicação com uma instalação preexistente do `trivy-operator`.

## Como verificar
Liste as integrações ativas com `k8sgpt integrations list` e verifique a geração de objetos `Result` correspondentes.

## Conexões
- [[k8sgpt-operator-auto-remediation-safety-gate-mutation]] — Veja também: K8sGPT Operator: auto-remediação opt-in com gate de segurança determinístico e recurso `Mutation`.
- [[k8sgpt-diagnostico-performance-stats-dump-custom-headers-proxy]] — Veja também: K8sGPT: estatísticas de latência por analisador (`-s`), captura de diagnóstico (`dump`) e proxies corporativos.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
