---
id: software.devops.tranche06.000510
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

# Governança CNCF, registro em ADOPTERS.md e cadência de reuniões comunitárias e de contribuidores do LitmusChaos

## Em uma frase
A seção *Community* e *License* do README oficial documenta a governança aberta do LitmusChaos como projeto da CNCF sob **Apache License 2.0** (auditado pelo OpenSSF Best Practices e FOSSA): as empresas usuárias são registradas em `ADOPTERS.md`, o acompanhamento de versões ocorre no Release Tracker (`github.com/litmuschaos/litmus/milestones`), o suporte comunitário acontece no canal `#litmus` do Slack do Kubernetes (`slack.k8s.io` / `slack.litmuschaos.io`), e o projeto mantém duas reuniões regulares abertas: **Community Meetings** (toda 3ª quarta-feira do mês às 17:30 GMT) e **Contributor Meetings** (toda 2ª e última quinta-feira do mês às 14:30 GMT).

## Por que importa
Conhecer os canais formais de governança, o rastreador de milestones e os encontros técnicos quinzenais permite às equipes de plataforma acompanhar novas versões do LitmusChaos, reportar problemas e contribuir novos experimentos ao ecossistema CNCF.

## Como funciona
Acompanhe os milestones de release em `github.com/litmuschaos/litmus/milestones` ao planejar atualizações do `chaos-center` e dos operadores de execução, e consulte `docs.litmuschaos.io/docs/getting-started/installation` para os pré-requisitos de cada versão.

## Exemplo
Uma equipe de SRE que adota o LitmusChaos em produção registra seu caso de uso via PR em `ADOPTERS.md` e participa das Contributor Meetings para alinhar o suporte a uma nova versão do Kubernetes e do containerd.

## Limites e trade-offs
Conforme nota explícita na seção *License* do README, embora o Litmus seja licenciado sob Apache-2.0, alguns subprojetos ou ferramentas de terceiros acionadas opcionalmente podem ser regidos por licenças próprias; verifique sempre a licença específica ao integrar ferramentas externas via BYOC.

## Como verificar
Verifique a versão instalada dos componentes do LitmusChaos (`chaos-center`, `chaos-operator`, `chaos-exporter`) contra a release estável atual no repositório oficial.

## Conexões
- [[litmus-security-controls-rbac-and-blast-radius-containment]] — Veja também: Controles de segurança, RBAC por namespace e contenção de raio de explosão (blast radius) no LitmusChaos.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
