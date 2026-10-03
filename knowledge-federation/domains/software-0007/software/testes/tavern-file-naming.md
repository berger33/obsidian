---
id: software.testes.tranche22.001622
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

# Tavern: o nome do arquivo é o discovery

## Em uma frase
Para o plugin do pytest, a descoberta segue o nome: literalmente só arquivos test_*.tavern.yaml são coletados, e o sufixo duplo .tavern.yaml marca o formato dentro do ecossistema pytest.

## Por que importa
Convenção de nome é o registro — o mesmo padrão do pytest para .py vale aqui, e um typo no sufixo significa zero testes coletados em silêncio.

## Como funciona
Nomeie o arquivo de teste, rode py.test test_minimal.tavern.yaml -v e o item coletado aparece identificado pelo próprio test_name do YAML, não pelo caminho.

## Exemplo
A saída do quickstart mostra "test_minimal.tavern.yaml::Get some fake data from the JSON placeholder API PASSED" — o título YAML vira título do teste.

## Limites e trade-offs
Fora do pytest o nome não é obrigatório (tavern-ci aceita qualquer .yaml), mas aí você perde exatamente o que a integração oferece; a doc é explícita em preferir pytest.

## Como verificar
Renomeie um arquivo de teste válido para tavern_test.yaml e confirme que o pytest para de coletá-lo.

## Conexões
- [[tavern-yaml-structure]] — Veja também: Tavern: test_name e stages como vocabulário.
- [[tavern-pytest-integration]] — Veja também: Tavern: instalar como plugin e colher o ecossistema.

## Fontes
- [Tavern — documentação inicial](https://tavern.readthedocs.io/en/latest/) — proposta, quickstart YAML, CLI e comparativos; consultado em 2026-10-03.
- [Tavern — documentação completa](https://taverntesting.github.io/documentation) — documentação oficial linkada pela página inicial; consultado em 2026-10-03.
