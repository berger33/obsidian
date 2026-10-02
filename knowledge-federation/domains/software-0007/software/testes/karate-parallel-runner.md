---
id: software.testes.tranche15.000914
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

# Karate: executar features em paralelo

## Em uma frase
O runner do Karate executa features em paralelo por padrão quando configurado com um número de threads, mantendo cada cenário em contexto isolado.

## Por que importa
A suíte cresce junto com a cobertura e a execução sequencial deixa de caber no tempo disponível, mas paralelismo sem isolamento produz falhas intermitentes.

## Como funciona
Configure o runner com o número de threads adequado ao ambiente, agrupe tags quando houver recursos compartilhados e acompanhe o relatório agregado gerado ao final.

## Exemplo
`Karate.run('features').relativeTo(getClass()).parallel(4);` distribui as features em quatro threads e consolida o resultado.

## Limites e trade-offs
O paralelismo é no nível de cenário e não resolve dependências entre eles; recursos externos com limite de conexão ou estado global continuam exigindo serialização.

## Como verificar
Compare o tempo da execução paralela com a sequencial e rode a suíte repetidas vezes para verificar estabilidade antes de aumentar o número de threads.

## Conexões
- [[karate-call-and-read]] — Veja também: Karate: reutilizar features com call e read.
- [[karate-data-driven]] — Veja também: Karate: parametrizar cenários com tabelas e arquivos.

## Fontes
- [Karate — Parallel execution](https://karatelabs.github.io/karate/#parallel-execution) — execução paralela de features e geração de relatórios agregados; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
