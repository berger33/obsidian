---
id: software.testes.tranche14.000811
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
fontes: ["https://tox.wiki/en/latest/reference/config.html", "https://tox.wiki/en/latest/how-to/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# tox: tratar env_list como matriz padrão executável

## Em uma frase
`env_list` define ambientes que tox seleciona por padrão quando a execução não recebe um escopo mais restrito.

## Por que importa
Uma matriz explícita comunica versões e verificações obrigatórias melhor que pressupor que todos os nomes configurados sempre serão executados.

## Como funciona
Liste ambientes de forma legível, agrupe fatores coerentes e use a CLI para selecionar um subconjunto durante investigação.

## Exemplo
Um `env_list` com Python 3.13, 3.14 e lint permite que `tox` rode a matriz completa sem parâmetros.

## Limites e trade-offs
Muitos eixos geram combinações caras; ambientes não listados como padrão podem exigir seleção explícita.

## Como verificar
Execute `tox list` e compare a lista observada com os jobs que a CI espera cobrir.

## Conexões
- [[tox-toml-over-deprecated-ini]] — Veja também: tox: preferir configuração TOML em projetos novos.
- [[tox-factor-matrix-combinations]] — Veja também: tox: compor ambientes por fatores sem expandir manualmente.

## Fontes
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
- [tox — How-to usage](https://tox.wiki/en/latest/how-to/usage.html) — execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários; consultado em 2026-10-02.
