---
id: software.testes.tranche14.000768
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/examples/rerun-failing-tests.html", "https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Surefire: registrar reruns como evidência de flakiness

## Em uma frase
`rerunFailingTestsCount` repete falhas até aprovação ou esgotamento e o Surefire marca um caso que passa depois de falhar como flaky.

## Por que importa
O resultado intermitente é informação sobre confiabilidade do teste, não uma correção automática da causa.

## Como funciona
Configure um número pequeno de reruns somente para coletar evidência e mantenha visíveis falhas iniciais, tentativas e resultados no XML.

## Exemplo
Execute com `-Dsurefire.rerunFailingTestsCount=2` e acompanhe `Flakes` no resumo antes de investigar a dependência instável.

## Limites e trade-offs
O suporte depende do provider/framework e um limite excessivo pode mascarar falhas reais ou aumentar o tempo de feedback.

## Como verificar
Acompanhe taxa de flaky ao longo do tempo e falhe o build quando a política do projeto não tolerar casos instáveis.

## Conexões
- [[maven-skip-execution-vs-test-compilation]] — Veja também: Maven: distinguir pular testes de pular sua compilação.
- [[maven-failsafe-report-separation]] — Veja também: Maven Failsafe: separar relatórios de integração dos unitários.

## Fontes
- [Maven Surefire — Re-run failing tests](https://maven.apache.org/surefire/maven-surefire-plugin/examples/rerun-failing-tests.html) — reruns, marcação de flakiness, relatórios XML e limite de frameworks; consultado em 2026-10-02.
- [Maven Surefire — test goal](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html) — parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades; consultado em 2026-10-02.
