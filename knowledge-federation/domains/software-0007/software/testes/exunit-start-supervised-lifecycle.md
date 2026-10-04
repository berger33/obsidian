---
id: software.testes.tranche12.000622
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

# ExUnit: encerrar processos com `start_supervised`

## Em uma frase
`start_supervised` inicia um processo sob supervisor vinculado ao ciclo de vida do teste e assegura seu encerramento antes de `on_exit`.

## Por que importa
Gerenciar processos explicitamente evita que um GenServer iniciado por um caso continue alterando estado depois de o caso seguinte começar.

## Como funciona
Inicie o child pela API de ExUnit, capture seu PID ou nome de registro e use configuração exclusiva quando o processo mantém dados mutáveis.

## Exemplo
Um teste de fila pode subir um worker com tabela isolada e consultá-lo enquanto o caso está ativo, sem implementar manualmente cada caminho de cleanup.

## Limites e trade-offs
Nomes registrados em atom podem colidir em execução paralela, e processos não supervisionados continuam exigindo encerramento explícito.

## Como verificar
Force uma assertion a falhar depois do start e confirme que o processo termina antes de o próximo teste consultar o mesmo recurso.

## Conexões
- [[exunit-setup-all-process-boundary]] — Veja também: ExUnit: limitar o que `setup_all` deve compartilhar.
- [[exunit-on-exit-separar-cleanup]] — Veja também: ExUnit: usar `on_exit` sem presumir o processo do teste.

## Fontes
- [ExUnit 1.20.4 — ExUnit.Callbacks](https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html) — setup, setup_all, contexto, processos supervisionados e on_exit; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
