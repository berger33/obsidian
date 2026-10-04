---
id: software.testes.tranche14.000762
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
fontes: ["https://maven.apache.org/surefire/maven-failsafe-plugin/examples/single-test.html", "https://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Surefire: selecionar classe sem confundir o escopo

## Em uma frase
A propriedade `-Dtest` seleciona classes ou métodos para Surefire, e deve ser tratada como filtro de diagnóstico, não como execução integral.

## Por que importa
Executar um caso específico acelera a investigação, mas um build verde nesse recorte não demonstra que as outras classes passaram.

## Como funciona
Passe o nome da classe ou um padrão conforme documentado, mantendo os nomes convencionados ou a configuração de includes do projeto.

## Exemplo
`mvn -Dtest=OrderServiceTest test` executa uma classe de unidade; para Failsafe, use a propriedade de seleção de teste de integração documentada pelo plugin.

## Limites e trade-offs
Seleção por método depende do provider e framework; os formatos aceitos variam, portanto confirme a compatibilidade na versão usada.

## Como verificar
Compare a lista de classes selecionadas com o filtro esperado e rode o conjunto completo antes de concluir uma mudança.

## Conexões
- [[maven-failsafe-verify-lifecycle]] — Veja também: Maven Failsafe: encerrar integração pela fase verify.
- [[maven-junit-platform-provider-boundary]] — Veja também: Maven Surefire: conferir engines da JUnit Platform.

## Fontes
- [Maven Failsafe — Running a Single Test](https://maven.apache.org/surefire/maven-failsafe-plugin/examples/single-test.html) — seleção de classes, métodos e padrões de testes de integração por -Dit.test; consultado em 2026-10-02.
- [Maven Surefire — Running a Single Test](https://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html) — seleção de testes individuais em Surefire e Failsafe; consultado em 2026-10-02.
