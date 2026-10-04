---
id: software.devops.tranche15.001425
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

# K8sGPT: modo servidor gRPC e Model Context Protocol (`k8sgpt serve --mcp`) para agentes de IA

## Em uma frase
A partir da versão `v0.4.14+`, o comando `k8sgpt serve` expõe um servidor gRPC de análise contínua e um servidor Model Context Protocol (`--mcp` / `--mcp-http`) para integração direta com clientes MCP como Claude Desktop e assistentes de IDE.

## Por que importa
Permite que engenheiros consultem a saúde do cluster, filtrem incidentes por namespace e solicitem diagnósticos guiados diretamente de interfaces conversacionais compatíveis com MCP sem executar comandos manuais repetitivos.

## Como funciona
Em modo STDIO (`k8sgpt serve --mcp`), o binário é invocado diretamente pelo cliente MCP local; já em modo HTTP (`k8sgpt serve --mcp --mcp-http --port 8080 --metrics-port 8081 --mcp-port 8089`), o K8sGPT expõe simultaneamente a API gRPC (`schema.v1.ServerAnalyzerService/Analyze` na porta `8080`), métricas na `8081` e o endpoint MCP na porta `8089`.

## Exemplo
```bash
k8sgpt serve --mcp --mcp-http --port 8080 --metrics-port 8081 --mcp-port 8089
grpcurl -plaintext -d '{"namespace": "default", "explain": "true"}' \
  localhost:8080 schema.v1.ServerAnalyzerService/Analyze
```

## Limites e trade-offs
Ao expor `k8sgpt serve --mcp --mcp-http` dentro do cluster via Helm chart, restrinja o acesso à porta `8089` com NetworkPolicies ou autenticação de gateway, pois clientes conectados poderão disparar varreduras no cluster.

## Como verificar
Teste a chamada gRPC com `grpcurl` na porta `8080` e confirme o retorno `{"status": "OK"}`.

## Conexões
- [[k8sgpt-backends-llm-openai-bedrock-ollama-localai-litellm]] — Veja também: K8sGPT: gerenciamento de provedores de IA (`k8sgpt auth`), modelos locais (Ollama/LocalAI) e proxy LiteLLM.
- [[k8sgpt-operator-crd-result-monitoramento-continuo-incluster]] — Veja também: K8sGPT Operator: monitoramento contínuo in-cluster com CRDs `K8sGPT` e `Result` e rotação automática de Secrets.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
