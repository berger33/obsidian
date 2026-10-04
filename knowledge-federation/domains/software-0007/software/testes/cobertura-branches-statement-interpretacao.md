---
id: software.testes.code-coverage.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://coverage.readthedocs.io/en/latest/branch.html", "https://clang.llvm.org/docs/SourceBasedCodeCoverage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Code coverage, Statement coverage, Branch coverage, Cobertura de código]
lote: software-testes-2000-0001
---

# Cobertura de statements e branches: o que medem

## Em uma frase
Cobertura de código mede itens executados segundo uma ferramenta e critério; statement coverage e branch coverage observam itens diferentes.

## Por que importa
Uma função pode ter cada linha executada sem que ambas as saídas de um `if` sejam exercitadas. Separar cobertura de instruções e de desvios ajuda a revelar lacunas na execução, especialmente em lógica condicional. As métricas são sinais de quais caminhos foram percorridos, não atestados de que os asserts verificaram a especificação.

## Como funciona
Coverage.py define branch coverage acompanhando possíveis destinos de execução entre linhas e marcando desvios não visitados; um `if` executado apenas como verdadeiro pode deixar a saída falsa sem cobertura, mesmo com as linhas visíveis executadas. Clang source-based coverage coleta dados instrumentados e gera relatórios de linhas, branches e, quando configurado, MC/DC. Compilar com instrumentação, executar testes e gerar o relatório são etapas separadas.

## Exemplo
Para `if x: return 1; else: return 0`, chamar a função só com `x=True` pode executar o ramo verdadeiro e a linha de retorno correspondente, mas não o destino do `else`. Um relatório de branch coverage revela o ramo ausente; o teste complementar deve verificar tanto o resultado falso quanto o comportamento exigido, não apenas executar a linha.

## Limites e trade-offs
100% de cobertura de branches não garante asserts corretos, todos os estados, todas as entradas nem ausência de defeitos. Macros, exclusões, código gerado e branches estruturais parciais podem afetar relatórios. Comparações entre linguagens e ferramentas precisam especificar o que cada uma conta. Cobertura deve orientar investigação, não virar objetivo isolado.

## Como verificar
Registre ferramenta, versão, flags e filtros usados. Inspecione branches parciais e exclusões com justificativa; examine código sem cobertura e asserções dos testes associados. Para decisões booleanas compostas, considere critérios mais fortes quando o risco exigir, como MC/DC, e mantenha cobertura ligada a requisitos e defeitos reais.

## Conexões
- [[mutation-testing-eficacia-testes]] — avalia se alterações de comportamento são detectadas, algo que cobertura de execução sozinha não mostra.
- [[mcdc-coverage-condicoes-independentes]] — aumenta a granularidade para efeitos independentes de condições.
- [[piramide-testes-estrategia-contexto]] — cobertura é uma métrica transversal a níveis de teste, não substituto de uma estratégia.

## Fontes
- [Coverage.py — Branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html) — diferença entre cobertura de statements e destinos de branches; acesso em 2026-10-01.
- [Clang — Source-based Code Coverage](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html) — instrumentação, relatórios e suporte a MC/DC; acesso em 2026-10-01.
