---
id: software.devops.tranche15.001422
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

# K8sGPT: analisadores embutidos padrão e opcionais (`k8sgpt filters`) para recursos nativos, Gateway API e OLM

## Em uma frase
O K8sGPT inclui 14 analisadores habilitados por padrão para recursos essenciais do Kubernetes e quase duas dezenas de analisadores opcionais cobrindo HPA, PDB, NetworkPolicy, Gateway API, segurança, logs e Operator Lifecycle Manager (OLM).

## Por que importa
Nem todo cluster utiliza Gateway API ou OLM, e escanear todos os tipos de recursos em clusters gigantescos aumentaria a latência da análise; o gerenciamento granular de filtros (`k8sgpt filters`) permite ativar apenas os verificadores relevantes.

## Como funciona
Por padrão, o K8sGPT executa `podAnalyzer`, `pvcAnalyzer`, `rsAnalyzer`, `serviceAnalyzer`, `eventAnalyzer`, `ingressAnalyzer`, `statefulSetAnalyzer`, `deploymentAnalyzer`, `jobAnalyzer`, `cronJobAnalyzer`, `nodeAnalyzer`, `mutatingWebhookAnalyzer`, `validatingWebhookAnalyzer` e `configMapAnalyzer`. Analisadores opcionais como `hpaAnalyzer`, `pdbAnalyzer`, `networkPolicyAnalyzer`, `gateway`, `httproute`, `securityAnalyzer` e `ValidatingAdmissionPolicy` são ativados via `k8sgpt filters add`.

## Exemplo
```bash
k8sgpt filters list
k8sgpt filters add HorizontalPodAutoscaler,PodDisruptionBudget
k8sgpt analyze --filter=Pod,Service --namespace=production
```

## Limites e trade-offs
Para restringir uma execução pontual sem alterar a configuração persistente de filtros padrão, utilize a flag `--filter=Service,Pod` diretamente no comando `k8sgpt analyze`.

## Como verificar
Rode `k8sgpt filters list` para auditar quais analisadores estão na lista `Active` e quais permanecem em `Unused`.

## Conexões
- [[k8sgpt-arquitetura-sre-analyzers-triagem-diagnostico-kubernetes]] — Veja também: K8sGPT: arquitetura de diagnóstico e triagem SRE de clusters Kubernetes enriquecida por IA.
- [[k8sgpt-anonimizacao-dados-sensiveis-anonymize-masking-llm]] — Veja também: K8sGPT: anonimização reversível de metadados sensíveis (`--anonymize`) antes do envio ao LLM.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
