---
id: software.devops.tranche06.000509
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

# Controles de segurança, RBAC por namespace e contenção de raio de explosão (blast radius) no LitmusChaos

## Em uma frase
Conforme detalhado na arquitetura dos CRDs e nas referências oficiais da CNCF listadas no README (*Security Controls for Safe Chaos Experimentation*), o LitmusChaos foi projetado para conter estritamente o **raio de explosão (blast radius)** dos experimentos: as permissões necessárias são declaradas explicitamente em cada `ChaosExperiment`, a execução pode ser restrita ao modo de namespace isolado (onde o operador e a `ServiceAccount` do runner só têm permissão para afetar recursos daquele próprio namespace), e o `ChaosEngine` suporta interrupção imediata com reversão automática das falhas caso uma probe crítica falhe.

## Por que importa
Uma ferramenta de Engenharia de Caos tem, por definição, capacidade de matar pods, corromper pacotes de rede e estressar recursos; sem isolamento estrito por namespace e RBAC de privilégio mínimo, um experimento mal configurado por uma equipe de aplicação poderia afetar serviços vizinhos no mesmo cluster.

## Como funciona
Para equipes de desenvolvimento em clusters multi-tenant, utilize contas de serviço restritas ao próprio namespace para experimentos de nível de pod, reservando experimentos de nível de nó/infraestrutura (como `node-drain` ou `node-cpu-hog`) exclusivamente para contas administrativas da equipe de SRE.

## Exemplo
Uma squad de produto recebe permissão RBAC apenas no seu namespace `checkout-homolog` para rodar experimentos `pod-delete` e `pod-network-latency` nos seus próprios pods, ficando impedida pelo Kubernetes de afetar qualquer outro namespace ou nó do cluster.

## Limites e trade-offs
Antes de executar qualquer experimento novo em produção, valide sempre o comportamento de aborto e limpeza automática em ambiente de staging para confirmar que o encerramento antecipado do `ChaosEngine` restaura o alvo em segundos.

## Como verificar
Teste com `kubectl auth can-i` as permissões da `ServiceAccount` associada ao `ChaosEngine` confirmando que ela não possui privilégios fora do escopo pretendido.

## Conexões
- [[litmus-observability-and-metrics-correlation-in-chaos]] — Veja também: Correlação de observabilidade e métricas Prometheus durante experimentos do LitmusChaos.
- [[litmus-cncf-governance-adopters-and-community-cadence]] — Veja também: Governança CNCF, registro em ADOPTERS.md e cadência de reuniões comunitárias e de contribuidores do LitmusChaos.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
