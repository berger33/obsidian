---
id: software.testes.tranche15.000916
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://karatelabs.github.io/karate/#parallel-execution", "https://karatelabs.github.io/karate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: selecionar cenários por tags

## Em uma frase
Tags declaradas em features e cenários permitem selecionar subconjuntos por execução, incluindo ou excluindo grupos conforme a necessidade do pipeline.

## Por que importa
Rodar toda a suíte em cada verificação encarece o feedback, mas seleção baseada em nome de arquivo não expressa risco e envelhece rápido.

## Como funciona
Marque cenários por risco ou tipo, mantenha um conjunto pequeno de fumaça e selecione grupos no runner sem alterar as features.

## Exemplo
Uma execução de fumaça pode rodar apenas os cenários marcados com a tag correspondente enquanto a suíte completa cobre as demais marcações.

## Limites e trade-offs
Tags duplicadas ou inconsistentes tornam a seleção imprevisível; cenários novos precisam de critério para receber a marcação correta.

## Como verificar
Liste os cenários selecionados pela tag em uso e confirme que a execução rápida cobre os fluxos críticos definidos pelo time.

## Conexões
- [[karate-data-driven]] — Veja também: Karate: parametrizar cenários com tabelas e arquivos.
- [[karate-mock-server]] — Veja também: Karate: simular serviços com o servidor mock.

## Fontes
- [Karate — Parallel execution](https://karatelabs.github.io/karate/#parallel-execution) — execução paralela de features e geração de relatórios agregados; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
