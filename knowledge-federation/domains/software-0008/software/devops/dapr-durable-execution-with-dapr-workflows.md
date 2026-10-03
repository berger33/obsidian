---
id: software.devops.tranche05.000482
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

# Execução durável e retomada automática de etapas com Dapr Workflows

## Em uma frase
A seção *Durable Execution* do README oficial destaca o bloco **Dapr Workflows**: uma engine de execução durável embutida no runtime que **persiste automaticamente o progresso de workflows de longa duração e retoma a execução exatamente a partir da última etapa concluída** após quedas de processo (`process crashes`), reinicializações de pod (`pod restarts`), falhas de nó (`node failures`), implantações rolantes (`rolling deployments`) ou interrupções de infraestrutura. O desenvolvedor escreve o workflow como código comum em sua linguagem de preferência, sem precisar projetar tabelas de máquina de estados ou lógica manual de checkpoint no banco de dados.

## Por que importa
Processos críticos de negócio — como processamento de pedidos, onboarding de clientes, aprovações humanas (*human-in-the-loop*), processamento de documentos e fluxos de múltiplos passos — não podem reiniciar do zero (cobrando o cartão do cliente duas vezes) nem perder o estado no meio quando um pod sofre rolling update no Kubernetes.

## Como funciona
Utilize a API de **Dapr Workflows** para orquestrar processos de negócio multi-etapas com atividades idempotentes, compensações (padrão Saga) e espera por eventos externos, deixando o Dapr persistir o histórico de execução no state store configurado.

## Exemplo
Durante um fluxo de processamento de pedido de 5 etapas, o nó Kubernetes onde o pod rodava falha exatamente após a etapa 3; quando o pod sobe em outro nó, o Dapr Workflows recupera o estado persistido e executa imediatamente a etapa 4 sem reexecutar as etapas 1, 2 e 3.

## Limites e trade-offs
Para que a reconstrução determinística do estado do workflow funcione corretamente após uma retomada, mantenha todas as chamadas com efeitos colaterais externos (I/O de rede, geração de números aleatórios ou relógio atual) encapsuladas dentro das atividades (*Activities*) do workflow.

## Como verificar
Inicie uma instância de Dapr Workflow, force o reinício do contêiner da aplicação no meio de uma etapa de espera e confirme pela API de status do workflow que ele retoma da etapa seguinte até atingir `COMPLETED`.

## Conexões
- [[dapr-sidecar-runtime-and-twelve-building-block-apis]] — Veja também: Arquitetura sidecar leve do Dapr (~58MB binário, ~4MB RAM) e as 12 APIs de blocos de construção.
- [[dapr-reliable-ai-agents-and-conversation-api-llm]] — Veja também: Operação confiável de agentes de IA, orquestração multi-agentes e Conversation API para LLMs no Dapr.

## Fontes
- [Dapr GitHub — README.md (Durable Execution, AI Agents, Zero-Trust mTLS, 12 Building Block APIs & Sidecar Architecture)](https://raw.githubusercontent.com/dapr/dapr/master/README.md) — README oficial do Dapr (projeto graduado na CNCF sob Apache-2.0) detalhando execução durável com Dapr Workflows, primitivas para agentes de IA e Conversation API, segurança por padrão com mTLS e Configuration accessControl, execução verificável, tabela das 12 APIs de blocos de construção sobre HTTP/gRPC (binário de ~58MB usando ~4MB de RAM) e repositórios de SDKs e components-contrib.; consultado em 2026-10-03.
- [Dapr Official Documentation — Getting Started & Concepts](https://docs.dapr.io/getting-started/) — Documentação oficial do Dapr cobrindo inicialização com Dapr CLI local e em Kubernetes, sidecar daprd, componentes plugáveis e observabilidade.; consultado em 2026-10-03.
- [Dapr — Official GitHub Repository](https://github.com/dapr/dapr) — Repositório principal Apache-2.0 do Dapr na CNCF.; consultado em 2026-10-03.
