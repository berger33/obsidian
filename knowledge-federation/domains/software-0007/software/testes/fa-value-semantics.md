---
id: software.testes.tranche22.001598
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
fontes: ["https://www.fluentassertions.com/objectgraphs/", "https://www.fluentassertions.com/introduction"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# FluentAssertions: por valor ou por membros

## Em uma frase
Para decidir quando recursar, o FluentAssertions trata como valor qualquer tipo que sobrescreve Object.Equals — mas anonymous types, record, record struct e tuples são sempre comparados por membros, por decisão documentada da comunidade.

## Por que importa
Um DateTime é valor e um record de domínio parece valor mas esconde grafo; escolher o modo de comparação é a diferença entre um teste útil e um teste mágico.

## Como funciona
Ajuste por asserção com ComparingByValue<T>, ComparingByMembers<T>, ComparingRecordsByValue e ComparingRecordsByMembers — ou globalmente via AssertionConfiguration.Current.Equivalency.Modify(options => options.ComparingByValue<DirectoryInfo>()).

## Exemplo
Para records especificamente: options.ComparingRecordsByValue().ComparingByMembers<MyRecord>() alterna o default por tipo num único fluent chain.

## Limites e trade-offs
Primitivos nunca são comparados por membros: ComparingByMembers<int> lança InvalidOperationException — a biblioteca bloqueia explicitamente o modo sem sentido.

## Como verificar
Marque um record com Equals custom e veja o BeEquivalentTo parar de recursar sozinho, confirmando a heurística por valor.

## Conexões
- [[fa-beequivalent-to]] — Veja também: FluentAssertions: BeEquivalentTo entre DTOs.
- [[fa-equivalency-options]] — Veja também: FluentAssertions: modelando a equivalência com opções.

## Fontes
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
