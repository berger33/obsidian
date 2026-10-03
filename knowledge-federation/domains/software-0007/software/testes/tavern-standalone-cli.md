---
id: software.testes.tranche22.001624
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
fontes: ["https://tavern.readthedocs.io/en/latest/", "https://taverntesting.github.io/documentation"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Tavern: tavern-ci para cron e shell

## Em uma frase
Sem pytest, o CLI tavern-ci --stdout arquivo.tavern.yaml executa a mesma máquina de testes, logando cada teste e cada stage com INFO (tavern.core) e fechando com "PASSED: <stage> [200]".

## Por que importa
Testes de fumaça agendados em cronjob ou scripts bash não precisam de conftest nem de runner; o CLI mantém o formato YAML como única interface.

## Como funciona
pip install tavern (sem extra) e chame tavern-ci no arquivo — o exemplo oficial roda contra o endpoint público e imprime inclusive o corpo da resposta no log.

## Exemplo
A saída documentada lista "Running test : Get some fake data..." seguida de "Running stage : Make sure we have the right ID" — um rastro legível por humano sem nenhum parser de JUnit.

## Limites e trade-offs
O modo CLI abre mão de fixtures, hooks e plugins; quem precisa de setup complexo migra para a integração pytest, como recomenda o próprio material.

## Como verificar
Execute tavern-ci --stdout contra um endpoint que você controla e confirme o [200] na linha PASSED.

## Conexões
- [[tavern-pytest-integration]] — Veja também: Tavern: instalar como plugin e colher o ecossistema.
- [[tavern-extensibility]] — Veja também: Tavern: estenda em Python quando o YAML aperta.

## Fontes
- [Tavern — documentação inicial](https://tavern.readthedocs.io/en/latest/) — proposta, quickstart YAML, CLI e comparativos; consultado em 2026-10-03.
- [Tavern — documentação completa](https://taverntesting.github.io/documentation) — documentação oficial linkada pela página inicial; consultado em 2026-10-03.
