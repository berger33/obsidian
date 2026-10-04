---
id: software.testes.tranche24.001839
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md", "https://github.com/cucumber/cucumber-jvm"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Financiamento por OpenCollective

## Em uma frase
O README exibe dois badges do OpenCollective — backers e sponsors — apontando para a página opencollective.com/cucumber, o veículo público de financiamento coletivo do projeto, e o parágrafo de voluntariado deixa claro por que isso importa: num projeto "almost entirely developed by volunteers", tempo de mantenedor é literalmente o recurso escasso que os badges procuram cobrir.

## Por que importa
A pergunta de sustentabilidade de framework de teste — quem paga para que a v7 exista — tem resposta verificável quando o projeto publica sua arrecadação; backers e sponsors visíveis na página do repositório são a contabilidade pública da saúde do projeto, complementando a advertência do README sobre quem precisa de bug corrigido.

## Como funciona
Empresas que dependem do framework no CI devem considerar a contribuição recorrente no OpenCollective como custo de manutenção da cadeia de fornecimento, no mesmo quadro em que tratam patrocínio de ferramental crítico; o próprio README articula o trade "implementar ou pagar".

## Exemplo
A leitura de risco simples para a reunião de arquitetura: badge de funding no README + página pública + a frase sobre voluntários — os três fatores juntos dimensionam a dependência não-monetária que a organização está assumindo.

## Limites e trade-offs
A nota cobre o que o README declara (existência do financiamento coletivo) sem afirmar valores, metas ou alocações específicas, que vivem na página do OpenCollective.

## Como verificar
Os dois badges de OpenCollective e a seção de bugs/voluntariado do README oficial sustentam a nota.

## Conexões
- [[cucumber-jvm-ci-quality]] — Veja também: CI de teste e de release, com scorecard público.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Repositório oficial cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) — Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.; consultado em 2026-10-03.
