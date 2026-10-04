---
id: software.testes.tranche14.000810
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://tox.wiki/en/latest/reference/config.html", "https://tox.wiki/en/latest/tutorial/getting-started.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# tox: preferir configuração TOML em projetos novos

## Em uma frase
tox 4 aceita TOML nativo e mantém INI por compatibilidade, mas a documentação marca INI como obsoleto e congelado.

## Por que importa
Iniciar arquivos novos no formato atual evita dependência de sintaxe antiga que não receberá novos recursos e pode ser removida em versão principal futura.

## Como funciona
Use `pyproject.toml` sob `[tool.tox]` ou `tox.toml`, valide a configuração resolvida e migre INI com testes da matriz.

## Exemplo
Um projeto novo declara `env_list` e ambientes nomeados em TOML e mantém a seleção padrão explícita.

## Limites e trade-offs
Migração automática pode alterar precedência, expansão ou parsing de valores; confira resultados dos ambientes após converter.

## Como verificar
Rode `tox list`, `tox config` e os ambientes selecionados antes e depois da migração para comparar o plano efetivo.

## Conexões
- [[tox-env-list-is-default-matrix]] — Veja também: tox: tratar env_list como matriz padrão executável.

## Fontes
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
- [tox — Getting started](https://tox.wiki/en/latest/tutorial/getting-started.html) — configuração TOML, ambientes base, comandos e passagem de argumentos; consultado em 2026-10-02.
