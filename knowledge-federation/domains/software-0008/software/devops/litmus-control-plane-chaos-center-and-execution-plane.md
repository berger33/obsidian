---
id: software.devops.tranche06.000501
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md", "https://docs.litmuschaos.io/docs/introduction/what-is-litmus", "https://github.com/litmuschaos/litmus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura do LitmusChaos: Chaos Control Plane (chaos-center) e Chaos Execution Plane

## Em uma frase
O LitmusChaos (`litmuschaos.io`), projeto 100% open-source da CNCF licenciado sob Apache-2.0, é uma plataforma cloud-native de **Engenharia de Caos (Chaos Engineering)** que permite às equipes identificar fraquezas e potenciais indisponibilidades em infraestruturas e aplicações induzindo testes de falha de forma controlada. Conforme detalha o README oficial, em alto nível a arquitetura do Litmus divide-se em duas camadas: o **Chaos Control Plane**, centrado na ferramenta gerenciadora **`chaos-center`** que auxilia a construir, agendar e visualizar workflows de caos; e os **Chaos Execution Plane Services**, compostos por um agente de caos e múltiplos operadores que executam e monitoram o experimento dentro do ambiente Kubernetes alvo definido.

## Por que importa
Separar o plano de controle (`chaos-center`) do plano de execução (agentes e operadores instalados nos clusters alvo) permite que uma equipe central de SRE e confiabilidade orquestre e visualize experimentos de caos através de múltiplos clusters Kubernetes de homologação e produção a partir de um único painel.

## Como funciona
Implante o `chaos-center` como plano de controle centralizado da organização e conecte os clusters Kubernetes alvo instalando os serviços do Chaos Execution Plane com permissões RBAC escopadas.

## Exemplo
Uma plataforma corporativa gerencia experimentos de resiliência em três clusters regionais a partir de uma única instância do `chaos-center`, disparando workflows agendados e comparando os índices de resiliência resultantes.

## Limites e trade-offs
Controle rigorosamente o acesso autenticado ao `chaos-center` e restrinja os agentes de execução nos clusters produtivos aos namespaces autorizados para evitar injeção de falhas não planejada fora da janela de GameDay.

## Como verificar
Acesse o `chaos-center` e verifique na aba de ambientes/agentes conectados que o Chaos Execution Plane do cluster alvo reporta status ativo e saudável.

## Conexões
- [[litmus-chaosexperiment-custom-resource-and-byoc]] — Veja também: O recurso customizado ChaosExperiment e o modelo Bring-Your-Own-Chaos (BYOC) no LitmusChaos.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
