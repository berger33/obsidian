---
id: software.testes.tranche14.000817
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

# tox: usar exec para ferramenta sem executar os hooks do ambiente

## Em uma frase
`tox exec` roda um comando pontual no ambiente selecionado, sem executar `commands`, `commands_pre` ou `commands_post`, e sem instalar pacote.

## Por que importa
A diferença torna `exec` útil para inspeção, mas inadequado como prova de que os testes configurados passaram.

## Como funciona
Selecione ambiente com `-e`, separe comando por `--` e confirme previamente que dependências e pacote já estão instalados.

## Exemplo
`tox exec -e py314 -- python -c ...` permite inspecionar versão ou imports dentro do ambiente sem rodar suite inteira.

## Limites e trade-offs
O subcomando não reproduz todo lifecycle que `tox run` executaria e o binário precisa estar no PATH permitido.

## Como verificar
Use `tox run` para validação normal e reserve `exec` para debugging ou comando one-off claramente rotulado.

## Conexões
- [[tox-config-command-as-debugging-tool]] — Veja também: tox: inspecionar configuração resolvida antes de editar.
- [[tox-parallel-pytest-temp-isolation]] — Veja também: tox: dar basetemp distinto a cada pytest paralelo.

## Fontes
- [tox — How-to usage](https://tox.wiki/en/latest/how-to/usage.html) — execução sequencial/paralela, seleção por ambiente, logs e diretórios temporários; consultado em 2026-10-02.
- [tox — CLI interface](https://tox.wiki/en/latest/cli_interface.html) — subcomandos run, parallel, exec, list e opções de saída; consultado em 2026-10-02.
