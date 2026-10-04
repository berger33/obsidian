---
id: software.testes.tranche14.000815
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

# tox: controlar variáveis herdadas com pass_env

## Em uma frase
`pass_env` seleciona variáveis do ambiente do processo que podem atravessar para a execução do ambiente tox.

## Por que importa
Declarar quais valores externos entram torna a reprodução mais clara e reduz vazamento acidental de configuração ou credenciais.

## Como funciona
Liste apenas variáveis exigidas pelo teste e use `set_env` para valores determinísticos pertencentes ao ambiente tox.

## Exemplo
Um teste que precisa de locale ou token de sandbox recebe somente essas variáveis nomeadas em vez de herdar todo o shell.

## Limites e trade-offs
Passar segredo à suite não elimina risco de exposição por logs, subprocessos ou assertions; trate dados sensíveis em CI.

## Como verificar
Inspecione configuração resolvida com `tox config -e ... -k pass_env set_env` e confira ambiente real dentro do processo.

## Conexões
- [[tox-env-selection-sequential-vs-parallel]] — Veja também: tox: distinguir executar ambientes em sequência de paralelo.
- [[tox-config-command-as-debugging-tool]] — Veja também: tox: inspecionar configuração resolvida antes de editar.

## Fontes
- [tox — Configuration reference](https://tox.wiki/en/latest/reference/config.html) — lista de ambientes, fatores, TOML, templates e configurações por ambiente; consultado em 2026-10-02.
- [tox — How-to usage](https://tox.wiki/en/latest/how-to/usage.html) — execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários; consultado em 2026-10-02.
