---
id: software.testes.tranche22.001623
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://tavern.readthedocs.io/en/latest/", "https://github.com/taverntesting/tavern/blob/master/pyproject.toml"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Tavern: instalar como plugin e colher o ecossistema

## Em uma frase
A integração recomendada é pip install tavern[pytest] — o extra ativa o plugin — e o próprio guia diz que com pytest instalado basta escrever os YAMLs e rodar: "literalmente tudo que você precisa fazer".

## Por que importa
O valor declarado de rodar dentro do pytest é herdar ecossistema: marcar, filtrar, reportar HTML e apontar contra servidores de teste periodicamente, tudo já existente.

## Como funciona
Os exemplos usam pytest.mark para organizar testes e anchors YAML para reutilizar blocos, conforme o comparativo "Easy to Write" da página oficial.

## Exemplo
O header do quickstart mostra plugins: tavern-0.7.2 na saída do pytest — é assim que a doc registra a versão do plugin no log.

## Limites e trade-offs
O extrato de versão do log do quickstart é antigo (Python 3.5, tavern 0.7.2); não espere exatamente essas linhas em install atual.

## Como verificar
Rode pytest --co test_*.tavern.yaml e confirme que os testes Tavern aparecem no collection sem nenhuma config extra.

## Conexões
- [[tavern-file-naming]] — Veja também: Tavern: o nome do arquivo é o discovery.
- [[tavern-standalone-cli]] — Veja também: Tavern: tavern-ci para cron e shell.

## Fontes
- [Tavern — documentação inicial](https://tavern.readthedocs.io/en/latest/) — proposta, quickstart YAML, CLI e comparativos; consultado em 2026-10-03.
- [Tavern — pyproject.toml](https://github.com/taverntesting/tavern/blob/master/pyproject.toml) — tagline oficial do projeto no manifesto; consultado em 2026-10-03.
