---
id: software.testes.tranche22.001620
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

# Tavern: testes de API escritos em YAML

## Em uma frase
O Tavern é um plugin do pytest, uma ferramenta de linha de comando e uma biblioteca Python para testes automatizados de APIs com sintaxe YAML simples e flexível, cobrindo REST, APIs MQTT e serviços gRPC.

## Por que importa
Testes de contrato de API em Python puro viram repetição de asserts; em YAML o contrato vira documento revisável por QA e backend no mesmo arquivo.

## Como funciona
Você declara request (url, method) e response esperado (status_code, json) por etapa, e o Tavern faz a chamada real, compara e reporta via pytest.

## Exemplo
O quickstart da doc oficial consulta https://jsonplaceholder.typicode.com/posts/1 e exige id: 1, userId: 1 e título exato no corpo.

## Limites e trade-offs
YAML não é linguagem de teste: lógica condicional e laços continuam pedindo Python (via fixtures/hooks), e o próprio projeto se descreve como "pequeno codebase que usa pytest por baixo".

## Como verificar
Rode o exemplo mínimo contra o jsonplaceholder e veja o caso passar com a linha "1 passed" do pytest.

## Conexões
- [[tavern-yaml-structure]] — Veja também: Tavern: test_name e stages como vocabulário.

## Fontes
- [Tavern — documentação inicial](https://tavern.readthedocs.io/en/latest/) — proposta, quickstart YAML, CLI e comparativos; consultado em 2026-10-03.
- [Tavern — pyproject.toml](https://github.com/taverntesting/tavern/blob/master/pyproject.toml) — tagline oficial do projeto no manifesto; consultado em 2026-10-03.
