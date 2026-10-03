---
id: software.testes.tranche17.001154
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://rspec.info/features/3-12/rspec-core/", "https://github.com/rspec/rspec-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec: selecionar exemplos por metadados

## Em uma frase
Os grupos e exemplos aceitam metadados, e a configuração pode aplicar ganchos ou filtros conforme esses metadados.

## Por que importa
A seleção permite rodar apenas subconjuntos relevantes e aplicar preparação específica sem duplicar código.

## Como funciona
Use metadados com significado estável, defina filtros na configuração e evite depender de títulos para selecionar exemplos.

## Exemplo
Exemplos marcados como lentos podem ser excluídos da execução rápida e incluídos na esteira completa.

## Limites e trade-offs
Metadados inconsistentes deixam exemplos fora da seleção sem aviso, e filtros por título quebram ao reescrever uma descrição.

## Como verificar
Liste os exemplos selecionados com os filtros usados e compare com a intenção antes de fixar a configuração.

## Conexões
- [[rspec-shared-examples]] — Veja também: RSpec: reutilizar comportamento com exemplos compartilhados.
- [[rspec-configuration-and-profiling]] — Veja também: RSpec: configurar e diagnosticar a suíte.

## Fontes
- [RSpec — Core](https://rspec.info/features/3-12/rspec-core/) — grupos de exemplos, contextos, ganchos, metadados e configuração; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
