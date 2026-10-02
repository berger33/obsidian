---
id: software.testes.tranche12.000626
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
fontes: ["https://ex-unit.hexdocs.pm/ExUnit.CaptureIO.html", "https://ex-unit.hexdocs.pm/ExUnit.Case.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ExUnit: capturar IO com segurança em testes async

## Em uma frase
`capture_io` substitui o group leader do processo atual durante a função e devolve o texto capturado.

## Por que importa
Capturar saída permite validar CLI e mensagens ao usuário sem poluir o log, mas dispositivos nomeados como stderr podem ser compartilhados por testes concorrentes.

## Como funciona
Prefira capturar IO do próprio processo; use `with_io` quando também precisar do retorno da função e trate capturas de dispositivos comuns conforme as regras de concorrência.

## Exemplo
Um teste de comando pode comparar a mensagem escrita em stdout e verificar separadamente o código calculado pelo bloco.

## Limites e trade-offs
Capturar o group leader de outro PID não é seguro para rodar concorrente, e stdout de um dispositivo compartilhado pode conter texto de mais de um teste.

## Como verificar
Execute duas capturas paralelas com marcadores distintos e confirme se a assertion observa apenas a saída do processo que deveria controlar.

## Conexões
- [[exunit-case-template-reuso]] — Veja também: ExUnit: compartilhar convenções com `CaseTemplate`.
- [[exunit-doctest-documentacao]] — Veja também: ExUnit: transformar exemplos de documentação em testes.

## Fontes
- [ExUnit 1.20.4 — ExUnit.CaptureIO](https://ex-unit.hexdocs.pm/ExUnit.CaptureIO.html) — captura de stdout/stderr, group leader e limites de concorrência; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
