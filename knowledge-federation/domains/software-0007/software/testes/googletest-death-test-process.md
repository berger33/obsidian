---
id: software.testes.tranche13.000737
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
fontes: ["https://google.github.io/googletest/advanced.html", "https://google.github.io/googletest/reference/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: isolar comportamento de morte em subprocesso

## Em uma frase
Death tests verificam se uma operação encerra ou termina processo segundo condição esperada.

## Por que importa
Para comportamento que não pode ser observado após encerramento, um teste dedicado protege contrato sem matar o runner inteiro.

## Como funciona
Use macros de death test para ação e padrão de saída, reserve cenário para processo descartável e evite efeitos que assumem mudança no processo pai.

## Exemplo
Um parser de configuração pode rejeitar estado impossível chamando check fatal; teste verifica encerramento e trecho de diagnóstico.

## Limites e trade-offs
Death test pode variar com ambiente ou fork model; não o use para erro comum que pode ser representado por retorno tipado.

## Como verificar
Execute isoladamente e junto da suite, confirme que subprocesso falha como esperado e que outros testes continuam rodando.

## Conexões
- [[googletest-filter-selected-tests]] — Veja também: GoogleTest: filtrar teste sem remover registro.
- [[googletest-global-environment-boundary]] — Veja também: GoogleTest: reservar environment global para recurso de programa.

## Fontes
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
