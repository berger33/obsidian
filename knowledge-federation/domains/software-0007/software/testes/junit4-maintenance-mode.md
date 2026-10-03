---
id: software.testes.tranche23.001670
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://junit.org/junit4/", "https://github.com/junit-team/junit4/wiki/Getting-started"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit 4 é um xUnit clássico em modo manutenção

## Em uma frase
A página oficial define o JUnit como "a simple framework to write repeatable tests", instância da arquitetura xUnit, e logo abaixo crava: "JUnit 4 is in maintenance mode" — apenas bugs críticos e questões de segurança serão corrigidos, e os demais issues e PRs são recusados.

## Por que importa
Decidir entre JUnit 4 e JUnit 5 é a pergunta de arquitetura de teste Java mais frequente em bases legadas; a posição oficial do projeto encerra o debate sobre novos recursos no 4.x.

## Como funciona
O desenvolvimento contínuo migrou para o repositório junit-framework, e a própria página indexa JavaDocs, FAQ, wiki de idioms e notas de versão 4.9 até 4.13.1 — o material de referência permanece completo, só não cresce.

## Exemplo
Abra junit.org/junit4 e confirme o banner de manutenção com o link para o repositório junit-framework; em seguida compare com seu pom.xml: se a dependência é 4.13.x, você está na linha de manutenção, não na de corte.

## Limites e trade-offs
"Modo manutenção" não significa abandonado para segurança nem fim do suporte da sua versão específica — o projeto não publica uma matriz de versões suportadas, então trate a política conforme declarada, sem extrapolar.

## Como verificar
Confirme na página About em junit.org/junit4 o parágrafo de manutenção, a definição xUnit e os dois exemplos de código com assertThat e matchers aninhados.

## Conexões
- [[junit4-run-without-build]] — Veja também: Rodar um teste JUnit 4 direto com JUnitCore.

## Fontes
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
- [JUnit 4 — Getting started (wiki)](https://github.com/junit-team/junit4/wiki/Getting-started) — jars, javac/java, JUnitCore e formatos de saída; consultado em 2026-10-03.
