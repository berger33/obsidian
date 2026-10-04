---
id: software.testes.tranche14.000814
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
fontes: ["https://tox.wiki/en/latest/how-to/usage.html", "https://tox.wiki/en/latest/cli_interface.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# tox: distinguir executar ambientes em sequência de paralelo

## Em uma frase
`tox run -e` executa ambientes escolhidos segundo a ordem especificada, enquanto o subcomando `tox parallel` executa em modo concorrente.

## Por que importa
Concorrência reduz tempo somente se cada ambiente não sobrescrever diretórios temporários, caches compartilhados ou serviços mutáveis.

## Como funciona
Use seleção sequencial para depuração previsível e habilite modo paralelo depois de tornar paths e fixtures de cada ambiente únicos.

## Exemplo
Um projeto pode executar lint e Python 3.14 em sequência localmente, mas paralelizar versões com `env_tmp_dir` exclusivo na CI.

## Limites e trade-offs
Paralelismo entre ambientes não garante isolamento interno dos testes executados por cada ambiente.

## Como verificar
Rode ambos os modos repetidamente, compare artefatos e procure colisões de temporários antes de declarar segurança concorrente.

## Conexões
- [[tox-deps-commands-and-posargs]] — Veja também: tox: separar instalação de dependências e comando de teste.
- [[tox-pass-env-explicit-contract]] — Veja também: tox: controlar variáveis herdadas com pass_env.

## Fontes
- [tox — How-to usage](https://tox.wiki/en/latest/how-to/usage.html) — execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários; consultado em 2026-10-02.
- [tox — CLI interface](https://tox.wiki/en/latest/cli_interface.html) — subcomandos run, parallel, exec, list e opções de saída; consultado em 2026-10-02.
