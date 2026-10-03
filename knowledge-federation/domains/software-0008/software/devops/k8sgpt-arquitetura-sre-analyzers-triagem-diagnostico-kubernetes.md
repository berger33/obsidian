---
id: software.devops.tranche15.001421
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

# K8sGPT: arquitetura de diagnóstico e triagem SRE de clusters Kubernetes enriquecida por IA

## Em uma frase
O K8sGPT (CNCF Sandbox, licença Apache-2.0) é uma ferramenta de linha de comando e operador que escaneia clusters Kubernetes com analisadores codificados com experiência de SRE e enriquece o diagnóstico em linguagem natural usando modelos de IA.

## Por que importa
Em clusters complexos com dezenas de eventos, falhas de webhooks, erros de PVC e serviços sem endpoints, engenheiros em plantão perdem tempo correlacionando manualmente objetos dispersos; o K8sGPT executa primeiro uma triagem determinística via código Go e aciona o LLM apenas para explicar os problemas reais detectados.

## Como funciona
A execução de `k8sgpt analyze` consulta a API do Kubernetes usando o kubeconfig ativo, passa os recursos pelos analisadores habilitados e retorna a lista objetiva de falhas; quando combinado com `--explain` e `--with-doc`, envia o diagnóstico filtrado ao backend de IA configurado e anexa referências da documentação oficial do Kubernetes.

## Exemplo
```bash
k8sgpt analyze
k8sgpt analyze --explain --with-doc --output=json
```

## Limites e trade-offs
A triagem primária do K8sGPT não depende de IA: se `k8sgpt analyze` for executado sem `--explain` (ou com o backend `noopai`), nenhum dado sai do ambiente e os analisadores determinísticos continuam apontando os erros estruturais do cluster.

## Como verificar
Execute `k8sgpt analyze -s` para inspecionar o tempo exato gasto por cada analisador no cluster sem realizar chamadas externas a provedores de LLM.

## Conexões
- [[k8sgpt-analyzers-embutidos-default-opcionais-filters]] — Veja também: K8sGPT: analisadores embutidos padrão e opcionais (`k8sgpt filters`) para recursos nativos, Gateway API e OLM.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
