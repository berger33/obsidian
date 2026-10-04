---
id: software.devops.tranche15.001426
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

# K8sGPT Operator: monitoramento contínuo in-cluster com CRDs `K8sGPT` e `Result` e rotação automática de Secrets

## Em uma frase
O `k8sgpt-operator` gerencia implantações in-cluster do K8sGPT por meio do Custom Resource `K8sGPT` (`core.k8sgpt.ai/v1alpha1`) e publica cada problema diagnosticado como um objeto Kubernetes nativo do tipo `Result`.

## Por que importa
Transforma diagnósticos pontuais de CLI em observabilidade contínua orientada a GitOps: os objetos `Result` podem ser inspecionados via `kubectl get results`, integrados ao Prometheus/Alertmanager, encaminhados a sinks (como Slack) ou exibidos no Backstage.

## Como funciona
O administrador instala o operador via Helm (`k8sgpt/k8sgpt-operator`), cria o Secret com a chave de API do provedor e aplica o recurso `K8sGPT`. Sempre que qualquer chave de dados do Secret referenciado em `spec.ai.secret` muda, o operador dispara automaticamente o rollout do Deployment do K8sGPT para recarregar a nova credencial.

## Exemplo
```bash
helm repo add k8sgpt https://charts.k8sgpt.ai/
helm install release k8sgpt/k8sgpt-operator -n k8sgpt-operator-system --create-namespace
kubectl get k8sgpts,results -n k8sgpt-operator-system
```

## Limites e trade-offs
Alterações apenas em labels ou annotations do Secret de IA não disparam rollout, mas modificações em qualquer chave dentro de `data` do Secret referenciado reiniciam o Deployment automaticamente.

## Como verificar
Execute `kubectl get results -n k8sgpt-operator-system -o json` após alguns minutos e verifique o preenchimento de `spec.details` nos resultados encontrados.

## Conexões
- [[k8sgpt-serve-mode-grpc-mcp-server-claude-desktop]] — Veja também: K8sGPT: modo servidor gRPC e Model Context Protocol (`k8sgpt serve --mcp`) para agentes de IA.
- [[k8sgpt-operator-multi-cluster-cluster-api-kubeconfig-remoto]] — Veja também: K8sGPT Operator: monitoramento multi-cluster sem agentes nos clusters filhos via `spec.kubeconfig` e Cluster API.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
