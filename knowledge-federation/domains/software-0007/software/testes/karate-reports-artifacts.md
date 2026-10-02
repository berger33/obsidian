---
id: software.testes.tranche15.000919
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://karatelabs.github.io/karate/#parallel-execution", "https://karatelabs.github.io/karate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: consumir o relatório da execução

## Em uma frase
O runner gera relatório HTML com o detalhamento de cada feature, cenário e passo, além de artefatos consumíveis por ferramentas de integração contínua.

## Por que importa
Um resultado resumido de sucesso ou falha não indica qual passo quebrou nem o conteúdo comparado, o que atrasa a triagem de regressões.

## Como funciona
Publique o diretório de relatórios como artefato do pipeline, referencie a execução do build e preserve a saída das execuções falhas.

## Exemplo
Os relatórios ficam no diretório de saída do projeto, normalmente em `target/karate-reports`, e o caminho deve ser configurado no runner quando o padrão não servir.

## Limites e trade-offs
O relatório descreve o que foi verificado, não a cobertura de caminhos possíveis; casos ausentes simplesmente não aparecem e não devem ser inferidos a partir do sucesso.

## Como verificar
Compare um relatório de execução aprovada com outro de execução falha e localize o passo divergente; confirme também a retenção do artefato no pipeline.

## Conexões
- [[karate-print-and-debug]] — Veja também: Karate: registrar evidências do passo.

## Fontes
- [Karate — Parallel execution](https://karatelabs.github.io/karate/#parallel-execution) — execução paralela de features e geração de relatórios agregados; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
