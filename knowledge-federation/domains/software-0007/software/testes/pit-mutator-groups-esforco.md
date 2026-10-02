---
id: software.testes.tranche12.000593
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
fontes: ["https://pitest.org/quickstart/mutators/", "https://pitest.org/quickstart/basic_concepts/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: selecionar grupos de mutadores conforme a pergunta

## Em uma frase
PIT oferece grupos de mutadores com alcances diferentes, incluindo `DEFAULTS`, `STRONGER` e `ALL`.

## Por que importa
Mais mutações podem procurar falhas mais diversas, porém elevam tempo de análise e podem gerar sobreviventes de interpretação mais difícil.

## Como funciona
Comece com o grupo padrão suportado pelo projeto, acrescente grupos adicionais para uma investigação delimitada e registre qual conjunto fundamenta qualquer score comparado.

## Exemplo
Um job de feedback rápido usa o grupo padrão; uma análise periódica pode experimentar operadores adicionais em um módulo crítico.

## Limites e trade-offs
Scores obtidos com grupos diferentes não são diretamente comparáveis, porque a população de mutantes mudou.

## Como verificar
Inspecione a configuração efetiva e o relatório para identificar os operadores que foram aplicados antes de comparar duas execuções.

## Conexões
- [[pit-status-killed-survived]] — Veja também: PIT: interpretar estados de mutantes no relatório.
- [[pit-targetclasses-targettests]] — Veja também: PIT: delimitar classes e testes de mutation testing.

## Fontes
- [PIT — Mutation Operators](https://pitest.org/quickstart/mutators/) — mutadores disponíveis e grupos DEFAULTS, STRONGER e ALL; consultado em 2026-10-02.
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
