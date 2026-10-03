---
id: software.devops.tranche05.000484
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

# Segurança por padrão no Dapr: identidade criptográfica, mTLS automático e políticas de accessControl

## Em uma frase
A seção *Secure by Default* do README oficial detalha a arquitetura de segurança zero-trust nativa do Dapr: toda aplicação Dapr recebe uma **identidade criptograficamente verificável** (com emissão e rotação automática de certificados pelo serviço Sentry do Dapr), aplicando **Mutual TLS (mTLS) para todo o tráfego serviço-para-serviço**, gerenciamento de segredos integrado ao cofre preferido e **políticas de autorização de privilégio mínimo** declaradas no recurso `kind: Configuration` (`apiVersion: dapr.io/v1alpha1`). Por exemplo, um manifesto `access-policy` define `spec.accessControl.defaultAction: deny` e libera especificamente `appId: orders` com `defaultAction: allow`.

## Por que importa
Em arquiteturas de microsserviços e agentes de IA, permitir que qualquer serviço chame qualquer outro endpoint interno sem mTLS e sem controle de acesso por identidade de aplicação (`appId`) permite movimentação lateral irrestrita em caso de comprometimento de um pod.

## Como funciona
Mantenha o mTLS habilitado no plano de controle do Dapr e aplique recursos `kind: Configuration` com `spec.accessControl.defaultAction: deny`, declarando explicitamente na lista `policies` quais `appId`, métodos HTTP/gRPC e verbos têm permissão de invocação.

## Exemplo
Para proteger o serviço de pagamentos, a equipe aplica uma `Configuration` do Dapr com `defaultAction: deny` que permite invocação apenas a partir do `appId: orders`; qualquer tentativa de chamada vinda de outro `appId` é bloqueada imediatamente pelo sidecar `daprd`.

## Limites e trade-offs
Ao ativar `defaultAction: deny` em uma `Configuration` compartilhada, revise todos os fluxos de `Service Invocation` existentes em homologação para garantir que nenhum `appId` legítimo foi omitido na lista de políticas permitidas.

## Como verificar
Aplique a `Configuration` de `accessControl` do exemplo oficial e verifique que chamadas de um `appId` não listado são rejeitadas com erro de acesso negado pelo sidecar receptor.

## Conexões
- [[dapr-reliable-ai-agents-and-conversation-api-llm]] — Veja também: Operação confiável de agentes de IA, orquestração multi-agentes e Conversation API para LLMs no Dapr.
- [[dapr-verifiable-execution-provenance-and-auditability]] — Veja também: Execução verificável (Verifiable Execution) para auditoria de linhagem e integridade no Dapr.

## Fontes
- [Dapr GitHub — README.md (Durable Execution, AI Agents, Zero-Trust mTLS, 12 Building Block APIs & Sidecar Architecture)](https://raw.githubusercontent.com/dapr/dapr/master/README.md) — README oficial do Dapr (projeto graduado na CNCF sob Apache-2.0) detalhando execução durável com Dapr Workflows, primitivas para agentes de IA e Conversation API, segurança por padrão com mTLS e Configuration accessControl, execução verificável, tabela das 12 APIs de blocos de construção sobre HTTP/gRPC (binário de ~58MB usando ~4MB de RAM) e repositórios de SDKs e components-contrib.; consultado em 2026-10-03.
- [Dapr Official Documentation — Getting Started & Concepts](https://docs.dapr.io/getting-started/) — Documentação oficial do Dapr cobrindo inicialização com Dapr CLI local e em Kubernetes, sidecar daprd, componentes plugáveis e observabilidade.; consultado em 2026-10-03.
- [Dapr — Official GitHub Repository](https://github.com/dapr/dapr) — Repositório principal Apache-2.0 do Dapr na CNCF.; consultado em 2026-10-03.
