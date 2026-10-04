---
id: software.testes.tranche12.000598
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
fontes: ["https://pitest.org/quickstart/maven/", "https://pitest.org/quickstart/basic_concepts/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: executar `mutationCoverage` e guardar o relatório

## Em uma frase
O plugin Maven expõe o goal `mutationCoverage`, que compila e executa a análise conforme os filtros definidos no projeto.

## Por que importa
Uma chamada reproduzível e o HTML gerado permitem inspecionar mutantes individualmente em vez de registrar somente uma porcentagem em CI.

## Como funciona
Execute o goal após compilar testes, mantenha a versão do plugin fixada e publique o diretório de relatório como artefato com retenção compatível com a política da equipe.

## Exemplo
Um job pode chamar `mvn test-compile org.pitest:pitest-maven:mutationCoverage` e anexar o relatório HTML ao build que produziu os resultados.

## Limites e trade-offs
Relatório da análise depende da configuração de classes, operadores e testes; comparar páginas de commits diferentes sem essas informações omite contexto essencial.

## Como verificar
Abra o HTML publicado, navegue de um resumo a um mutante específico e confirme que o arquivo corresponde ao SHA e à versão de PIT executados.

## Conexões
- [[pit-maven-dry-run-setup]] — Veja também: PIT: usar dry run ao configurar a análise.
- [[pit-mutation-score-interpretacao]] — Veja também: PIT: não reduzir adequação de testes ao mutation score.

## Fontes
- [PIT — Maven Quick Start](https://pitest.org/quickstart/maven/) — goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3; consultado em 2026-10-02.
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
