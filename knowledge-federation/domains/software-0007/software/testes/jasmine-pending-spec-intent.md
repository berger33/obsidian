---
id: software.testes.tranche13.000668
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://jasmine.github.io/api/7.0/global", "https://jasmine.github.io/api/7.0/Configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: registrar pending sem confundir com cobertura

## Em uma frase
Um spec `it` sem função de teste é marcado como pending, e a API também distingue specs focados.

## Por que importa
Pendências documentam trabalho incompleto, mas não demonstram que o comportamento esperado passou.

## Como funciona
Dê nome explícito ao comportamento pendente, acompanhe sua remoção e revise o resumo do reporter para que pending não seja contabilizado como sucesso afirmativo.

## Exemplo
Uma equipe pode registrar `it('preserva o rascunho offline')` sem implementação enquanto espera decisão de produto, deixando visível o requisito ainda não verificado.

## Limites e trade-offs
Um pending pode desaparecer do sinal de cobertura se a pipeline só examinar falhas. Requisitos críticos precisam de uma assertion executada.

## Como verificar
Conte separadamente specs pendentes e executados e faça o job falhar ou alertar quando a lista pendente superar o limite editorial acordado.

## Conexões
- [[jasmine-focused-spec-cleanup]] — Veja também: Jasmine: remover fit e fdescribe antes da CI.
- [[jasmine-async-matcher-await]] — Veja também: Jasmine: aguardar resultado de expectAsync.

## Fontes
- [Jasmine 7 — Global API](https://jasmine.github.io/api/7.0/global) — specs, suites, focus, hooks and async timeout; consultado em 2026-10-02.
- [Jasmine 7 — Configuration](https://jasmine.github.io/api/7.0/Configuration) — random execution, spec discovery and environment configuration; consultado em 2026-10-02.
