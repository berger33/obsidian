---
id: software.devops.tranche02.000173
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
fontes: ["https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md", "https://github.com/fluent/fluent-bit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cadência de releases maiores a cada 3–4 meses, série v5.1 e guia MAINTENANCE.md

## Em uma frase
A seção `📌 Roadmap & Maintenance` do README informa que o projeto segue um ciclo acelerado de desenvolvimento com lançamentos principais a cada **3–4 meses** (`major releases every 3–4 months`), que a branch `master` acompanha atualmente a série estável **v5.1**, e que os cronogramas e políticas de manutenção por versão estão documentados em `MAINTENANCE.md`, enquanto os próximos marcos constam do `Fluent-Bit-Roadmap` na wiki oficial.

## Por que importa
Com uma cadência rápida de lançamentos a cada 3 a 4 meses, equipes de plataforma precisam consultar `MAINTENANCE.md` para alinhar as atualizações dos DaemonSets de observabilidade às séries ativamente suportadas.

## Como funciona
Consulte o arquivo `MAINTENANCE.md` no repositório `fluent/fluent-bit` ao definir a versão do agente nos manifestos Helm ou Kustomize e acompanhe a wiki de roadmap para planejar novas capacidades.

## Exemplo
A equipe de observabilidade revisa `MAINTENANCE.md` trimestralmente para atualizar os agentes da frota para a série estável suportada.

## Limites e trade-offs
Evite fixar imagens de produção em branches de desenvolvimento sem testar a configuração dos plugins em homologação a cada mudança de série.

## Como verificar
Conferi a seção Roadmap & Maintenance no README oficial de `fluent/fluent-bit`.

## Conexões
- [[fluentbit-multi-platform-and-embedded-footprint]] — Veja também: Suporte multi-plataforma (Linux, Windows, macOS, BSD e sistemas embarcados) e escala de produção.
- [[fluentbit-pluggable-inputs-filters-outputs-architecture]] — Veja também: Arquitetura modular plugável com mais de 70 plugins de Inputs, Filters e Outputs.

## Fontes
- [Fluent Bit — GitHub README](https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md) — Visão geral do Fluent Bit (agente graduado na CNCF para Logs, Metrics e Traces), suporte multi-plataforma, ciclo de 3–4 meses (v5.1), 70+ plugins, SQL Stream Processing, extensibilidade C/Lua/Go e build CMake.; consultado em 2026-10-03.
- [Fluent Bit — Repositório Oficial no GitHub](https://github.com/fluent/fluent-bit) — Repositório oficial do Fluent Bit com código-fonte, MAINTENANCE.md, DEVELOPER_GUIDE.md e workflows de CI.; consultado em 2026-10-03.
