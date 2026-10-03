---
id: software.testes.tranche20.001364
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://docs.gauge.org/writing-specifications", "https://docs.gauge.org/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: conduzir cenários por dados

## Em uma frase
Uma tabela antes de um cenário transforma o bloco em várias execuções, uma por linha, com os valores disponíveis nos passos.

## Por que importa
A tabela concentra os casos de entrada e saída, deixando visível a cobertura de combinações sem repetir cenários no texto.

## Como funciona
Declare a tabela com cabeçalho nomeado, mantenha uma linha por caso e use os nomes das colunas exatamente como aparecem.

## Exemplo
Uma tabela pode listar três perfis de usuário com o resultado esperado para cada um, executando o mesmo cenário três vezes.

## Limites e trade-offs
Linhas redundantes inflam o tempo de execução, e colunas sem uso tornam a tabela difícil de manter.

## Como verificar
Acrescente uma linha inválida e confirme que o relatório identifica o caso pelo valor da coluna correspondente.

## Conexões
- [[gauge-context-and-hooks]] — Veja também: Gauge: preparar estado com ganchos e contexto.
- [[gauge-parallel-execution]] — Veja também: Gauge: executar em fluxos paralelos.

## Fontes
- [Gauge — Escrever especificações](https://docs.gauge.org/writing-specifications) — sintaxe das especificações, tabelas de dados e conceitos; consultado em 2026-10-03.
- [Gauge — Visão geral](https://docs.gauge.org/overview) — conceitos de especificação, cenário, passo e conceito; consultado em 2026-10-03.
