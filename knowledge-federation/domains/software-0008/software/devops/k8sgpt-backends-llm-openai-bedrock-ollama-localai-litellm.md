---
id: software.devops.tranche15.001424
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

# K8sGPT: gerenciamento de provedores de IA (`k8sgpt auth`), modelos locais (Ollama/LocalAI) e proxy LiteLLM

## Em uma frase
O subcomando `k8sgpt auth` configura e alterna entre mais de uma dezena de provedores de IA — incluindo OpenAI, Azure OpenAI, Amazon Bedrock, Google Gemini/Vertex AI, Cohere, IBM watsonx.ai, modelos locais via Ollama/LocalAI e mais de 100 provedores via LiteLLM.

## Por que importa
Permite que equipes operem o K8sGPT tanto com modelos de nuvem corporativos governados por IAM (como AWS Bedrock Inference Profiles) quanto em ambientes 100% *air-gapped* usando modelos abertos rodando localmente em Ollama ou vLLM.

## Como funciona
O operador adiciona credenciais e endpoints com `k8sgpt auth add --backend <nome> --model <modelo>`, lista os provedores configurados com `k8sgpt auth list` e define o provedor padrão com `k8sgpt auth default -p <nome>`. O backend `litellm` conecta-se por padrão a `http://localhost:4000/v1` para rotear chamadas a qualquer modelo compatível.

## Exemplo
```bash
k8sgpt auth add --backend ollama --baseurl http://localhost:11434 --model llama3.2
k8sgpt auth default -p ollama
k8sgpt auth list
```

## Limites e trade-offs
Ao usar Amazon Bedrock com perfis de inferência (`amazonbedrock` ou `amazonbedrockconverse`), é obrigatório informar `--providerRegion` e o ARN completo do `inference-profile` ou `application-inference-profile` na flag `--model`.

## Como verificar
Execute `k8sgpt auth list` e verifique que o provedor desejado aparece sob a seção `Active` e `Default`.

## Conexões
- [[k8sgpt-anonimizacao-dados-sensiveis-anonymize-masking-llm]] — Veja também: K8sGPT: anonimização reversível de metadados sensíveis (`--anonymize`) antes do envio ao LLM.
- [[k8sgpt-serve-mode-grpc-mcp-server-claude-desktop]] — Veja também: K8sGPT: modo servidor gRPC e Model Context Protocol (`k8sgpt serve --mcp`) para agentes de IA.

## Fontes
- [K8sGPT GitHub — README.md (Built-in & Optional SRE Analyzers, Anonymization, LLM AI Backends, LiteLLM & Model Context Protocol Server)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/main/README.md) — README oficial do k8sgpt-ai/k8sgpt documentando analisadores padrão e opcionais, mascaramento reversível (--anonymize), provedores de IA e servidor gRPC/MCP; consultado em 2026-10-03.
- [K8sGPT Operator GitHub — README.md (In-Cluster K8sGPT CRD, Result Objects, Multi-Cluster Cluster API Monitoring & Opt-In Auto-Remediation)](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt-operator/main/README.md) — README oficial do k8sgpt-ai/k8sgpt-operator detalhando monitoramento contínuo in-cluster, rotação automática de Secrets, integração multi-cluster com CAPI e gate determinístico de auto-remediação; consultado em 2026-10-03.
- [K8sGPT — Official GitHub Repository](https://github.com/k8sgpt-ai/k8sgpt) — Repositório oficial Apache-2.0 do K8sGPT; consultado em 2026-10-03.
