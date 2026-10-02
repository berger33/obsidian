---
id: software.testes.tranche12.000599
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
fontes: ["https://pitest.org/quickstart/basic_concepts/", "https://pitest.org/quickstart/mutators/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: não reduzir adequação de testes ao mutation score

## Em uma frase
Mutation score resume proporções de estados dos mutantes, mas não descreve quais requisitos foram testados nem o custo de interpretar sobreviventes.

## Por que importa
O indicador serve para localizar áreas pouco sensíveis a mudanças simuladas, não para provar que a suíte cobre todos os defeitos ou contratos do sistema.

## Como funciona
Leia resultados por pacote e operador, investigue sobreviventes representativos e anote alterações no conjunto de mutantes ao comparar limiares ao longo do tempo.

## Exemplo
Uma classe pode ter score alto porque mutações simples foram mortas, embora uma regra de autorização crítica não tenha caso específico de fronteira.

## Limites e trade-offs
Mutantes equivalentes podem não alterar o comportamento observável; elevar o limiar sem triagem incentiva ignorar alertas ou escrever assertions frágeis.

## Como verificar
Escolha uma amostra de mutantes mortos e sobreviventes, avalie seu significado para o domínio e combine a métrica com revisão de requisitos e testes de fronteira.

## Conexões
- [[pit-maven-goal-relatorio]] — Veja também: PIT: executar `mutationCoverage` e guardar o relatório.

## Fontes
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
- [PIT — Mutation Operators](https://pitest.org/quickstart/mutators/) — mutadores disponíveis e grupos DEFAULTS, STRONGER e ALL; consultado em 2026-10-02.
