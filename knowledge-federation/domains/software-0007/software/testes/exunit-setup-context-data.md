---
id: software.testes.tranche12.000620
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

# ExUnit: passar contexto entre setup e teste

## Em uma frase
Callbacks `setup` podem receber contexto e retornar novos valores que são mesclados ao contexto disponível para etapas seguintes e para o teste.

## Por que importa
Uma fixture declarativa deixa visíveis os dados preparados para cada caso e reduz dependência de variáveis globais ou estado escondido no módulo.

## Como funciona
Retorne `:ok` quando não houver valores adicionais ou um map/lista de keywords com chaves próprias; consuma-as explicitamente na assinatura do teste.

## Exemplo
Um setup pode criar um identificador de tenant e adicionar `tenant_id` ao contexto que o teste usa para compor a request.

## Limites e trade-offs
Valores com a mesma chave podem sobrescrever metadados anteriores, e uma fixture que contata serviço real pode tornar muitos testes dependentes da mesma infraestrutura.

## Como verificar
Inspecione o contexto recebido e provoque erro durante setup para confirmar que os testes seguintes não usam dados parciais.

## Conexões
- [[exunit-setup-all-process-boundary]] — Veja também: ExUnit: limitar o que `setup_all` deve compartilhar.

## Fontes
- [ExUnit 1.20.4 — ExUnit.Callbacks](https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html) — setup, setup_all, contexto, processos supervisionados e on_exit; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
