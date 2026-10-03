---
id: software.devops.tranche15.001428
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

# K8sGPT Operator: auto-remediação opt-in com gate de segurança determinístico e recurso `Mutation`

## Em uma frase
O `k8sgpt-operator` inclui um recurso experimental e estritamente *opt-in* de auto-remediação capaz de corrigir falhas selecionadas de imagem (`ImagePullBackOff`) sob um gate determinístico em que o LLM nunca recebe permissão direta de escrita no cluster.

## Por que importa
Conceder permissão de escrita arbitrária (`kubectl patch` irrestrito) a um modelo generativo em produção criaria grave risco de alucinação destrutiva; o design do K8sGPT Operator separa a sugestão do modelo da validação e aplicação determinística pelo controlador.

## Como funciona
Quando habilitado, o operador re-busca o objeto vivo na API, resolve Pods pertencentes a controladores para o recurso dono (como o `Deployment`), calcula ele próprio o JSON patch semântico permitindo apenas o caminho aprovado de imagem, executa `dry-run` contra o Kubernetes API Server e registra o ciclo no objeto `Mutation` até atingir o estado `Successful`.

## Exemplo
```bash
kubectl get mutations -n k8sgpt-operator-system
kubectl describe mutation -n k8sgpt-operator-system
```

## Limites e trade-offs
A auto-remediação é um recurso em estágio `alpha` voltado a classes específicas de falha (como reparo de uma única referência de imagem no workload proprietário); propostas obsoletas, amplas ou inseguras são rejeitadas pelo gate de política.

## Como verificar
Inspecione os objetos `Mutation` no namespace do operador para auditar propostas aprovadas, validações de dry-run e rollouts concluídos.

## Conexões
- [[k8sgpt-operator-multi-cluster-cluster-api-kubeconfig-remoto]] — Veja também: K8sGPT Operator: monitoramento multi-cluster sem agentes nos clusters filhos via `spec.kubeconfig` e Cluster API.
- [[k8sgpt-integrations-trivy-prometheus-sinks-slack-backstage]] — Veja também: K8sGPT: integrações com Trivy, Prometheus, sinks de notificação Slack e catálogo Backstage.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
