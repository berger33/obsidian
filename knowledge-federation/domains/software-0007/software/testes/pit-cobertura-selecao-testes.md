---
id: software.testes.tranche12.000591
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
fontes: ["https://pitest.org/quickstart/basic_concepts/", "https://pitest.org/quickstart/commandline/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: usar cobertura para escolher testes por mutante

## Em uma frase
Antes de executar casos contra mutantes, PIT mede cobertura de linha e tempos para selecionar testes que alcançam a área modificada.

## Por que importa
A seleção reduz o custo em projetos grandes e evita rodar toda a suíte para cada alteração, mas depende da informação coletada na execução base.

## Como funciona
Mantenha testes descobertos e cobertura executável no classpath esperado, restrinja o alvo ao conjunto relevante e examine mutantes sem teste correspondente como lacunas de alcance.

## Exemplo
Um teste que cobre uma classe de validação pode ser selecionado para seus mutantes, enquanto um teste de módulo sem relação com aquela linha não precisa ser repetido.

## Limites e trade-offs
Cobertura de linha mostra execução, não sensibilidade da assertion à mutação. Uma linha pode ser coberta e ainda aceitar valores incorretos.

## Como verificar
Compare quais testes o relatório associou ao mutante e confirme se eles exercitam o comportamento afetado, não apenas uma linha adjacente.

## Conexões
- [[pit-mutacao-bytecode-mutantes]] — Veja também: PIT: mutação de bytecode para avaliar assertions.
- [[pit-status-killed-survived]] — Veja também: PIT: interpretar estados de mutantes no relatório.

## Fontes
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
- [PIT — Command Line Quick Start](https://pitest.org/quickstart/commandline/) — filtros de target classes/tests, execução e parâmetros de linha de comando; consultado em 2026-10-02.
