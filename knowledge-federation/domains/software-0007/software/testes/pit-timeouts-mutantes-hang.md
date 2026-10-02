---
id: software.testes.tranche12.000595
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://pitest.org/quickstart/basic_concepts/", "https://pitest.org/quickstart/maven/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: distinguir timeout de mutante sobrevivente

## Em uma frase
PIT usa limite temporal para evitar que um mutante que provoque loop ou execução longa bloqueie indefinidamente a análise.

## Por que importa
Separar `Timed Out` de `Survived` preserva a causa da incerteza e impede que uma alteração de orçamento seja tratada como melhora de assertions.

## Como funciona
Consulte os valores de timeout e a duração dos testes, ajuste limites com base em medição e mantenha visível quando uma mutação termina por exceder o tempo permitido.

## Exemplo
Se inverter uma condição cria um loop, o relatório pode indicar timeout; o diagnóstico deve observar tanto a mutação como o teste selecionado.

## Limites e trade-offs
Aumentar o timeout global pode multiplicar minutos por grande número de mutantes e não corrige um teste que já demora por causa de recursos externos.

## Como verificar
Reproduza um timeout com alvo pequeno e compare a duração real, a configuração e o estado final antes de modificar o orçamento da suíte.

## Conexões
- [[pit-targetclasses-targettests]] — Veja também: PIT: delimitar classes e testes de mutation testing.
- [[pit-incremental-history-assumptions]] — Veja também: PIT: tratar histórico incremental como otimização.

## Fontes
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
- [PIT — Maven Quick Start](https://pitest.org/quickstart/maven/) — goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3; consultado em 2026-10-02.
