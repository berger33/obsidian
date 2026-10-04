---
id: software.testes.tranche12.000629
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://ex-unit.hexdocs.pm/ExUnit.html", "https://ex-unit.hexdocs.pm/ExUnit.Case.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ExUnit: reproduzir ordem com seed e controlar `max_cases`

## Em uma frase
ExUnit permite configurar seed para randomizar testes e `max_cases` para limitar quantos casos de módulos distintos rodam simultaneamente.

## Por que importa
A seed ajuda a repetir ordem de uma falha, enquanto o limite de casos coordena concorrência com os recursos disponíveis no runner.

## Como funciona
Guarde a seed exibida pelo Mix, repita-a durante diagnóstico e configure `max_cases` conforme CPU, banco e serviços utilizados pelos módulos.

## Exemplo
Uma falha causada por configuração deixada por outro módulo pode reaparecer ao repetir a seed original com a mesma lista de testes.

## Limites e trade-offs
Semente reproduzível não fixa relógio ou estado remoto; aumentar paralelismo além da capacidade do serviço pode gerar erros de ambiente em vez de defeitos.

## Como verificar
Reexecute com a seed registrada e compare logs dos módulos concorrentes antes de atribuir a causa à implementação testada.

## Conexões
- [[exunit-tags-select-filters]] — Veja também: ExUnit: selecionar execução com tags e filtros.

## Fontes
- [ExUnit 1.20.4 — ExUnit](https://ex-unit.hexdocs.pm/ExUnit.html) — configuração de max_cases, seed e execução paralela por módulo; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
