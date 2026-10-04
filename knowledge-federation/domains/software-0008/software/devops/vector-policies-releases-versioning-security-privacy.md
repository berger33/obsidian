---
id: software.devops.tranche02.000189
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/vectordotdev/vector/master/README.md", "https://vector.dev/docs/setup/quickstart/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Políticas formais do projeto: Releases, Versioning, Security, Privacy e Code of Conduct

## Em uma frase
A seção `Documentation` do README lista, sob `Other Resources`, o calendário do projeto (`Vector Calendar`) e as seis políticas oficiais que regem o ciclo de vida do Vector: **Code of Conduct**, **Contributing**, **Privacy**, **Releases**, **Versioning** e **Security**.

## Por que importa
Para operar um pipeline de dados corporativo com previsibilidade, a equipe de plataforma precisa conhecer exatamente a política de versionamento (`Versioning`), a cadência e suporte de lançamentos (`Releases`), as garantias de privacidade do binário (`Privacy`) e o processo de divulgação de falhas (`Security`).

## Como funciona
Consulte as políticas de `Releases` e `Versioning` do Vector ao definir a estratégia de atualização dos agentes e agregadores na sua frota e revise a política de `Security` para o tratamento de CVEs.

## Exemplo
Antes de atualizar os agregadores centrais para uma nova versão do Vector, o engenheiro de confiabilidade confere a política de versionamento e as notas de release para identificar eventuais mudanças de configuração.

## Limites e trade-offs
Teste sempre novas versões do Vector validando os arquivos de configuração existentes em ambiente de homologação antes do rollout nos nós de produção.

## Como verificar
Conferi a seção Documentation no README oficial de `vectordotdev/vector`.

## Conexões
- [[vector-ci-workflows-nightly-integration-component-features]] — Veja também: Verificação contínua no repositório: Nightly, Integration/E2E Test Suite e Component Features.
- [[vector-choosing-between-vector-fluentbit-and-otelcol]] — Veja também: Posicionamento arquitetural: como combinar ou escolher entre Vector, Fluent Bit e OpenTelemetry Collector.

## Fontes
- [Vector — GitHub README](https://raw.githubusercontent.com/vectordotdev/vector/master/README.md) — Visão geral do Vector (pipeline de observabilidade em Rust para agent e aggregator), princípios, 5 casos de uso, escala na comunidade (500 TB/dia) e tabelas de performance e corretude.; consultado em 2026-10-03.
- [Vector Documentation — Quickstart & Components](https://vector.dev/docs/setup/quickstart/) — Documentação oficial do Vector para configuração de sources, transforms e sinks referenciada no README.; consultado em 2026-10-03.
