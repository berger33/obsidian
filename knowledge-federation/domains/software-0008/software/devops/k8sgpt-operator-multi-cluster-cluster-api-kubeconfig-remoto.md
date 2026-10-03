---
id: software.devops.tranche15.001427
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
fontes: ["https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md", "https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md", "https://github.com/k8sgpt-ai/k8sgpt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K8sGPT Operator: monitoramento multi-cluster sem agentes nos clusters filhos via `spec.kubeconfig` e Cluster API

## Em uma frase
O `k8sgpt-operator` pode monitorar múltiplos clusters remotos a partir de um único cluster de gerenciamento referenciando o Secret de `kubeconfig` de cada cluster alvo no campo `spec.kubeconfig`.

## Por que importa
Em arquiteturas de Platform Engineering baseadas no Cluster API, permite diagnosticar dezenas de workload clusters sem instalar CRDs do K8sGPT nem consumir recursos computacionais nos clusters filhos.

## Como funciona
Quando o Cluster API provisiona um cluster `<nome>`, ele gera o Secret `<nome>-kubeconfig` com a chave `value`. Ao criar um CR `K8sGPT` apontando `spec.kubeconfig` para esse Secret, o operador instancia um Deployment dedicado no management cluster e rotula os objetos `Result` gerados com `k8sgpts.k8sgpt.ai/name`, `k8sgpts.k8sgpt.ai/namespace` e `k8sgpts.k8sgpt.ai/backend`.

## Exemplo
```yaml
apiVersion: core.k8sgpt.ai/v1alpha1
kind: K8sGPT
metadata:
  name: capi-workload-01
  namespace: k8sgpt-operator-system
spec:
  ai:
    anonymized: true
    backend: openai
    model: gpt-4o-mini
    secret:
      name: openai-secret
      key: api_key
  kubeconfig:
    name: capi-workload-01-kubeconfig
    key: value
```

## Limites e trade-offs
O `kubeconfig` gerado por padrão pelo Cluster API possui permissões de `cluster-admin`; para ambientes que exigem privilégio mínimo (*least privilege*), gere um `kubeconfig` dedicado somente leitura para o K8sGPT.

## Como verificar
Filtre os diagnósticos por cluster monitorado executando `kubectl get results -n k8sgpt-operator-system -l k8sgpts.k8sgpt.ai/name=capi-workload-01`.

## Conexões
- [[k8sgpt-operator-crd-result-monitoramento-continuo-incluster]] — Veja também: K8sGPT Operator: monitoramento contínuo in-cluster com CRDs `K8sGPT` e `Result` e rotação automática de Secrets.
- [[k8sgpt-operator-auto-remediation-safety-gate-mutation]] — Veja também: K8sGPT Operator: auto-remediação opt-in com gate de segurança determinístico e recurso `Mutation`.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
