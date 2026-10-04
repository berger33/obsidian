---
id: software.testes.tranche16.000987
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/openjdk/jmh/tree/master/jmh-samples", "https://github.com/openjdk/jmh"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMH: escolher o escopo do estado

## Em uma frase
O escopo do objeto de estado define se os dados são compartilhados entre threads, exclusivos de cada thread ou limitados a um grupo.

## Por que importa
Compartilhar estado mutável sem sincronização produz medição de contenção acidental, enquanto estado por thread pode impedir o compartilhamento pretendido.

## Como funciona
Use escopo por thread para eliminar disputa, escopo compartilhado para medir concorrência real e escopo de grupo para testes que exigem coordenação.

## Exemplo
Um benchmark de estrutura de dados sem sincronização deve criar uma instância por thread, medindo a operação e não o bloqueio acidental.

## Limites e trade-offs
Estado compartilhado com escrita concorrente mede o mecanismo de sincronização da estrutura, e essa intenção precisa ser declarada no desenho do experimento.

## Como verificar
Execute o mesmo caso com escopo por thread e compartilhado e explique a diferença observada antes de reportar qualquer número.

## Conexões
- [[jmh-forking]] — Veja também: JMH: isolar execuções com fork.
- [[jmh-setup-and-teardown]] — Veja também: JMH: preparar em níveis adequados.

## Fontes
- [JMH — exemplos oficiais](https://github.com/openjdk/jmh/tree/master/jmh-samples) — amostras de parâmetros, estados, preparação e consumo de resultados; consultado em 2026-10-03.
- [JMH — repositório oficial](https://github.com/openjdk/jmh) — anotações, modos de medição, forking, estados, parâmetros e execução; consultado em 2026-10-03.
