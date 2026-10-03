---
id: software.devops.tranche05.000488
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/dapr/dapr/master/README.md", "https://docs.dapr.io/getting-started/", "https://github.com/dapr/dapr"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SDKs nativos em 8 linguagens (.NET, Java, Python, Go, JS/TS, Rust, C++ e PHP) sobre HTTP e gRPC

## Em uma frase
O README oficial lista os repositórios dedicados de SDKs oficiais mantidos pelo projeto Dapr: **`go-sdk`** (Go), **`java-sdk`** (Java), **`js-sdk`** (JavaScript/TypeScript), **`python-sdk`** (Python), **`dotnet-sdk`** (.NET), **`rust-sdk`** (Rust), **`cpp-sdk`** (C++) e **`php-sdk`** (PHP). Ao mesmo tempo, o documento enfatiza que todas as capacidades do Dapr são expostas diretamente pelo sidecar sobre **HTTP e gRPC padrão**, o que significa que **qualquer linguagem de programação** pode usar o Dapr mesmo sem importar nenhum SDK específico.

## Por que importa
Em empresas com arquitetura políglota (por exemplo, serviços core em Go e Rust, sistemas corporativos em Java e .NET, agentes de IA em Python e BFFs em TypeScript), padronizar SDKs nativos ergonômicos que falam com a mesma versão do sidecar `daprd` unifica a governança da plataforma.

## Como funciona
Adote os SDKs oficiais (`dapr/go-sdk`, `dapr/python-sdk`, `dapr/java-sdk`, `dapr/dotnet-sdk`, `dapr/js-sdk`, `dapr/rust-sdk`, `dapr/cpp-sdk`, `dapr/php-sdk`) para ganhar tipagem forte e integração nativa com workflows e atores, ou invoque diretamente os endpoints HTTP/gRPC do `localhost` em scripts e linguagens adicionais.

## Exemplo
Uma equipe de engenharia desenvolve o orquestrador de agentes de IA usando `dapr/python-sdk` e o serviço de liquidação financeira de baixa latência usando `dapr/rust-sdk`; ambos invocam um ao outro com mTLS automático via `Service Invocation` do Dapr.

## Limites e trade-offs
Prefira o protocolo **gRPC** entre a aplicação e o sidecar `daprd` local (padrão nos SDKs oficiais) quando buscar menor latência de serialização e maior throughput em comparação a payloads JSON sobre HTTP/1.1.

## Como verificar
Execute um exemplo do repositório `github.com/dapr/quickstarts` usando um dos SDKs oficiais e confirme a comunicação com o sidecar local.

## Conexões
- [[dapr-actors-distributed-lock-cryptography-and-jobs-apis]] — Veja também: APIs avançadas de coordenação e segurança no Dapr: Actors, Distributed Lock, Cryptography e Jobs.
- [[dapr-dapr-cli-local-and-kubernetes-lifecycle-management]] — Veja também: Gerenciamento de desenvolvimento local e clusters Kubernetes com Dapr CLI (dapr/cli).

## Fontes
- [Dapr GitHub — README.md (Durable Execution, AI Agents, Zero-Trust mTLS, 12 Building Block APIs & Sidecar Architecture)](https://raw.githubusercontent.com/dapr/dapr/master/README.md) — README oficial do Dapr (projeto graduado na CNCF sob Apache-2.0) detalhando execução durável com Dapr Workflows, primitivas para agentes de IA e Conversation API, segurança por padrão com mTLS e Configuration accessControl, execução verificável, tabela das 12 APIs de blocos de construção sobre HTTP/gRPC (binário de ~58MB usando ~4MB de RAM) e repositórios de SDKs e components-contrib.; consultado em 2026-10-03.
- [Dapr Official Documentation — Getting Started & Concepts](https://docs.dapr.io/getting-started/) — Documentação oficial do Dapr cobrindo inicialização com Dapr CLI local e em Kubernetes, sidecar daprd, componentes plugáveis e observabilidade.; consultado em 2026-10-03.
- [Dapr — Official GitHub Repository](https://github.com/dapr/dapr) — Repositório principal Apache-2.0 do Dapr na CNCF.; consultado em 2026-10-03.
