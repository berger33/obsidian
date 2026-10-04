---
id: software.testes.tranche14.000813
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
fontes: ["https://tox.wiki/en/latest/tutorial/getting-started.html", "https://tox.wiki/en/latest/reference/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# tox: separar instalação de dependências e comando de teste

## Em uma frase
Configuração tox define dependências de ambiente e comandos a executar, podendo encaminhar argumentos do usuário ao runner.

## Por que importa
A separação registra o que é instalado e o que é testado, reduzindo dependência de ferramentas globais da máquina.

## Como funciona
Declare deps e commands por ambiente, passe argumentos extras via placeholder de posargs e mantenha diretórios de teste isolados.

## Exemplo
Um ambiente instala pytest e executa a suite `tests`, anexando um filtro de caso que veio após `--`.

## Limites e trade-offs
`skip_install` e modos de pacote alteram se o projeto é instalado no ambiente; não presuma que testar o checkout seja sempre equivalente ao pacote construído.

## Como verificar
Inspecione comando expandido com `tox config` e valide a versão instalada do projeto dentro do ambiente.

## Conexões
- [[tox-factor-matrix-combinations]] — Veja também: tox: compor ambientes por fatores sem expandir manualmente.
- [[tox-env-selection-sequential-vs-parallel]] — Veja também: tox: distinguir executar ambientes em sequência de paralelo.

## Fontes
- [tox — Getting started](https://tox.wiki/en/latest/tutorial/getting-started.html) — configuração TOML, ambientes base, comandos e passagem de argumentos; consultado em 2026-10-02.
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
