---
id: software.testes.tranche14.000812
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

# tox: compor ambientes por fatores sem expandir manualmente

## Em uma frase
Fatores são segmentos do nome do ambiente e permitem condicionar dependências ou comandos por combinação, incluindo plataforma.

## Por que importa
Uma matriz nomeada reduz duplicação e torna visível quais versões de Python e dependências foram exercitadas.

## Como funciona
Defina fatores ou `env_base` com combinações deliberadas, exclua pares sem suporte e mantenha nomes legíveis para relatórios.

## Exemplo
Uma matriz pode combinar `py313` e `py314` com fatores de versões Django, instalando a dependência compatível para cada sessão.

## Limites e trade-offs
Produto cartesiano cresce rapidamente e algumas combinações são redundantes ou inválidas; não acrescente eixos só porque são fáceis de gerar.

## Como verificar
Inspecione `tox list`, dependências resolvidas e quantidade de ambientes produzidos quando um fator novo for incluído.

## Conexões
- [[tox-env-list-is-default-matrix]] — Veja também: tox: tratar env_list como matriz padrão executável.
- [[tox-deps-commands-and-posargs]] — Veja também: tox: separar instalação de dependências e comando de teste.

## Fontes
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
- [tox — Getting started](https://tox.wiki/en/latest/tutorial/getting-started.html) — configuração TOML, ambientes base, comandos e passagem de argumentos; consultado em 2026-10-02.
