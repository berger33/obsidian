---
id: software.testes.tranche14.000764
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
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/examples/inclusion-exclusion.html", "https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Surefire: tornar convenções de nome parte da descoberta

## Em uma frase
Os padrões de inclusão do Surefire determinam quais classes compiladas entram na execução padrão.

## Por que importa
Classe fora da convenção pode compilar sem ser coletada, criando um falso sinal de cobertura do build.

## Como funciona
Use os nomes padrão aceitos pelo plugin ou configure includes e excludes explícitos, evitando regras que contradigam o layout real do módulo.

## Exemplo
Uma equipe pode manter `*Test.java` para testes de unidade e configurar um padrão distinto no Failsafe para `*IT.java`.

## Limites e trade-offs
Alterar um padrão global pode excluir acidentalmente classes válidas ou incluir testes lentos na fase unitária.

## Como verificar
Inspecione os relatórios e a contagem por classe após renomear um teste ou editar includes.

## Conexões
- [[maven-junit-platform-provider-boundary]] — Veja também: Maven Surefire: conferir engines da JUnit Platform.
- [[maven-fork-count-process-isolation]] — Veja também: Maven Surefire: escolher forkCount pelo isolamento exigido.

## Fontes
- [Maven Surefire — Inclusion and Exclusion](https://maven.apache.org/surefire/maven-surefire-plugin/examples/inclusion-exclusion.html) — padrões de nomes para incluir ou excluir classes de teste; consultado em 2026-10-02.
- [Maven Failsafe — Usage](https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html) — goals integration-test e verify, teardown do ciclo e relatórios de integração; consultado em 2026-10-02.
