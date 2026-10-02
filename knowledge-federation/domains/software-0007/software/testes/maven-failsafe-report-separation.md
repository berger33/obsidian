---
id: software.testes.tranche14.000769
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
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/", "https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Failsafe: separar relatórios de integração dos unitários

## Em uma frase
Failsafe registra resultados de integração em formato compatível com Surefire, mas seus relatórios ficam em diretório próprio.

## Por que importa
Separar artefatos permite atribuir falhas à camada correta e preservar resultados após cleanup dos serviços usados em integração.

## Como funciona
Publique `target/failsafe-reports` além do diretório de Surefire e configure relatórios ou coleta da CI para ambos.

## Exemplo
O resumo do pipeline pode agregar testes unitários e de integração, mantendo os XML individuais ligados ao módulo que os produziu.

## Limites e trade-offs
Consumo de formato semelhante não significa que os dois goals tenham o mesmo lifecycle ou diretório.

## Como verificar
Confirme que uma falha injetada em cada fase aparece no artefato de relatório esperado após `mvn verify`.

## Conexões
- [[maven-rerun-flaky-evidence]] — Veja também: Maven Surefire: registrar reruns como evidência de flakiness.

## Fontes
- [Maven Surefire — Introduction](https://maven.apache.org/surefire/maven-surefire-plugin/) — fase test, execução de testes unitários e diretório padrão de relatórios; consultado em 2026-10-02.
- [Maven Failsafe — Usage](https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html) — goals integration-test e verify, teardown do ciclo e relatórios de integração; consultado em 2026-10-02.
