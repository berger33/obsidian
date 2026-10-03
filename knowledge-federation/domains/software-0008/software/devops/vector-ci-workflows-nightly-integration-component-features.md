---
id: software.devops.tranche02.000188
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
fontes: ["https://raw.githubusercontent.com/vectordotdev/vector/master/README.md", "https://github.com/vectordotdev/vector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Verificação contínua no repositório: Nightly, Integration/E2E Test Suite e Component Features

## Em uma frase
Os três badges no topo do README oficial mostram as suítes de automação que validam o repositório `vectordotdev/vector`: **Nightly** (`workflows/nightly.yml`), **Integration/E2E Test Suite** (`workflows/integration.yml`) e **Component Features** (`workflows/component_features.yml`).

## Por que importa
Como o Vector integra dezenas de protocolos, bancos de dados e serviços de nuvem distintos via feature flags do Cargo/Rust, testar isoladamente cada combinação de `component_features` além da suíte de integração ponta a ponta evita que uma alteração em um sink quebre a compilação modular de outro componente.

## Como funciona
Ao compilar builds customizadas do Vector em Rust ou contribuir com código para um source/sink específico, valide tanto o workflow `component_features.yml` quanto a suíte `integration.yml`.

## Exemplo
Um contribuidor que adiciona suporte a um novo cabeçalho em um sink HTTP verifica os testes de integração ponta a ponta antes de solicitar revisão do pull request.

## Limites e trade-offs
Builds `nightly` servem para validação antecipada; para clusters de produção, utilize sempre as versões estáveis em `vector.dev/releases/latest/download/` ou as imagens oficiais em `vectordotdev/vector/pkgs/container/vector`.

## Como verificar
Conferi os badges e links de topo no README oficial de `vectordotdev/vector`.

## Conexões
- [[vector-sources-transforms-sinks-pipeline-model]] — Veja também: Modelo declarativo do pipeline: coleta em sources, processamento em transforms e entrega em sinks.
- [[vector-policies-releases-versioning-security-privacy]] — Veja também: Políticas formais do projeto: Releases, Versioning, Security, Privacy e Code of Conduct.

## Fontes
- [Vector — GitHub README](https://raw.githubusercontent.com/vectordotdev/vector/master/README.md) — Visão geral do Vector (pipeline de observabilidade em Rust para agent e aggregator), princípios, 5 casos de uso, escala na comunidade (500 TB/dia) e tabelas de performance e corretude.; consultado em 2026-10-03.
- [Vector — Repositório Oficial no GitHub](https://github.com/vectordotdev/vector) — Repositório oficial do Vector em Rust com código-fonte, workflows de integração e links de políticas.; consultado em 2026-10-03.
