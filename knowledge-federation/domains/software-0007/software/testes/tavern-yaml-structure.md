---
id: software.testes.tranche22.001621
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

# Tavern: test_name e stages como vocabulário

## Em uma frase
Todo arquivo de teste tem um ou mais testes, cada teste tem um ou mais stages, e cada stage declara a request feita e a resposta esperada — o vocabulário completo do formato cabe numa página.

## Por que importa
Reduzir o teste ao par ação/verificação torna a revisão de PR de API legível como especificação, sem precisar executar nada.

## Como funciona
A estrutura do quickstart oficial: test_name no topo, stages como lista, e dentro de cada stage name, request {url, method} e response {status_code, json}.

## Exemplo
No exemplo, o stage "Make sure we have the right ID" espera status_code: 200 e o json com id: 1 e o título fixo do endpoint público.

## Limites e trade-offs
Um json exato demais acopla o teste ao payload completo — dados voláteis de API alheia quebram o suite sem mudança de contrato; vale filtrar os campos que importam.

## Como verificar
Adicione um campo inesperado na resposta mockada localmente e confirme se o teste quebra (acoplamento total) ou não (comparação subset).

## Conexões
- [[tavern-what-it-is]] — Veja também: Tavern: testes de API escritos em YAML.
- [[tavern-file-naming]] — Veja também: Tavern: o nome do arquivo é o discovery.

## Fontes
- [Tavern — documentação inicial](https://tavern.readthedocs.io/en/latest/) — proposta, quickstart YAML, CLI e comparativos; consultado em 2026-10-03.
- [Tavern — documentação completa](https://taverntesting.github.io/documentation) — documentação oficial linkada pela página inicial; consultado em 2026-10-03.
