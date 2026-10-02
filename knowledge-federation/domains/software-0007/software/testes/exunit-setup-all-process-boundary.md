---
id: software.testes.tranche12.000621
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

# ExUnit: limitar o que `setup_all` deve compartilhar

## Em uma frase
`setup_all` roda uma vez por módulo antes dos testes, em processo separado do processo de cada teste.

## Por que importa
A fronteira de processo impede tratar variáveis de processo como se fossem memória compartilhada e exige decidir conscientemente como fixtures chegam aos casos.

## Como funciona
Use esse callback para inicialização comum que possa ser lida de modo seguro; retorne metadados do contexto quando apropriado e prefira setup por teste para estado mutável.

## Exemplo
Um módulo pode validar a disponibilidade de configuração no início, enquanto cada teste cria seu próprio registro e processo supervisionado.

## Limites e trade-offs
Inicializar um recurso global no callback não torna seu estado serializado entre testes nem garante segurança de escrita para casos assíncronos.

## Como verificar
Compare o identificador do processo no `setup_all` e nos testes, e execute o módulo em modo async para detectar pressupostos sobre compartilhamento.

## Conexões
- [[exunit-setup-context-data]] — Veja também: ExUnit: passar contexto entre setup e teste.
- [[exunit-start-supervised-lifecycle]] — Veja também: ExUnit: encerrar processos com `start_supervised`.

## Fontes
- [ExUnit 1.20.4 — ExUnit.Callbacks](https://ex-unit.hexdocs.pm/ExUnit.Callbacks.html) — setup, setup_all, contexto, processos supervisionados e on_exit; consultado em 2026-10-02.
- [ExUnit 1.20.4 — ExUnit.Case](https://ex-unit.hexdocs.pm/ExUnit.Case.html) — testes, describe, tags, async e filtros de execução; consultado em 2026-10-02.
