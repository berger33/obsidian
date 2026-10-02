---
id: software.testes.tranche12.000623
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
fontes: ["https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html", "https://ex-unit.hexdocs.pm/ExUnit.Case.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ExUnit: usar `on_exit` sem presumir o processo do teste

## Em uma frase
Callbacks `on_exit` são executados após a saída do processo de teste e rodam em processo separado.

## Por que importa
A separação é adequada para limpeza que deve ocorrer mesmo após falha, mas significa que variáveis privadas do processo não são um canal implícito para o callback.

## Como funciona
Registre a função durante setup depois de criar o recurso e capture somente identificadores ou dados serializáveis necessários para desfazer a operação.

## Exemplo
Após criar arquivo externo, o setup pode registrar remoção do caminho em `on_exit`; a limpeza continua definida mesmo se uma assertion interromper o corpo.

## Limites e trade-offs
Processos supervisionados têm garantia de término antes do callback, mas uma limpeza externa que falha ainda precisa produzir diagnóstico observável.

## Como verificar
Provoque falha no teste, verifique se o callback rodou e confira no sistema externo que o recurso foi removido.

## Conexões
- [[exunit-start-supervised-lifecycle]] — Veja também: ExUnit: encerrar processos com `start_supervised`.
- [[exunit-async-global-state]] — Veja também: ExUnit: habilitar `async: true` com estado independente.

## Fontes
- [ExUnit 1.20.4 — ExUnit.Callbacks](https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html) — setup, setup_all, contexto, processos supervisionados e on_exit; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
