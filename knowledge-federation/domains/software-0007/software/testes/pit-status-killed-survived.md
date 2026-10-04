---
id: software.testes.tranche12.000592
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

# PIT: interpretar estados de mutantes no relatório

## Em uma frase
PIT classifica resultados como `Killed`, `Survived`, `No coverage`, `Non viable` e `Timed Out`, entre outros estados documentados.

## Por que importa
Rótulos diferentes apontam ações distintas: reforçar uma assertion, ampliar cobertura, revisar compilação da mutação ou entender um limite de tempo.

## Como funciona
Abra o detalhe do mutante, identifique a linha modificada e leia o estado junto dos testes selecionados antes de resumir a execução em um único score.

## Exemplo
Um `Survived` indica que os testes executados não detectaram aquela alteração; `No coverage` diferencia a ausência de teste que exercite a linha.

## Limites e trade-offs
Nem todo mutante sobrevivente é um defeito real, e um timeout pode vir da interação entre código alterado e teste lento em vez de uma falha funcional observável.

## Como verificar
Escolha um caso de cada estado reportado e relacione o rótulo com os testes executados e a mutação concreta para checar se o time o interpreta corretamente.

## Conexões
- [[pit-cobertura-selecao-testes]] — Veja também: PIT: usar cobertura para escolher testes por mutante.
- [[pit-mutator-groups-esforco]] — Veja também: PIT: selecionar grupos de mutadores conforme a pergunta.

## Fontes
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
- [PIT — Maven Quick Start](https://pitest.org/quickstart/maven/) — goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3; consultado em 2026-10-02.
