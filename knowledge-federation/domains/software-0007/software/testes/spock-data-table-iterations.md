---
id: software.testes.tranche13.000723
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://spockframework.org/spock/docs/2.4/data_driven_testing.html", "https://spockframework.org/spock/docs/2.4/all_in_one.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: parametrizar feature com where table

## Em uma frase
Bloco `where:` fornece data variables que executam a mesma feature para cada linha da tabela.

## Por que importa
Tabela separa dados de lógica e faz valores problemáticos aparecerem no relatório de cada iteração.

## Como funciona
Declare cabeçalho e linhas com tipos coerentes, mantenha `where:` no fim do método e use uma separação visual entre colunas de entrada e saída quando isso melhora leitura.

## Exemplo
Uma tabela de parcelas e taxa pode aplicar mesmo cálculo a combinações pequenas, com resultado esperado numa coluna separada.

## Limites e trade-offs
Iteration é isolada como feature distinta, mas referências mutáveis compartilhadas exigem `@Shared`; tabela fixa não substitui propriedade sobre todo domínio.

## Como verificar
Introduza valor incorreto numa linha e confirme que relatório identifica a iteração e seus dados sem impedir execução das demais.

## Conexões
- [[spock-shared-field-scope]] — Veja também: Spock: limitar uso de Shared para recurso realmente comum.
- [[spock-where-iteration-isolation]] — Veja também: Spock: preservar isolamento entre linhas de dados.

## Fontes
- [Spock 2.4 — Data-Driven Testing](https://spockframework.org/spock/docs/2.4/data_driven_testing.html) — where blocks, data tables, iteration isolation and failures; consultado em 2026-10-02.
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
