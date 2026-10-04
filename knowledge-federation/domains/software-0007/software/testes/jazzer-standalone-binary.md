---
id: software.testes.tranche21.001551
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://github.com/CodeIntelligenceTesting/jazzer/releases"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: binário standalone da página de releases

## Em uma frase
Os arquivos de release trazem um binário jazzer que sobe a própria JVM já configurada para fuzzing; basta apontar o classpath e a classe do fuzz test.

## Por que importa
O caminho do binário não exige plugin de build nem instrumentação manual — é o jeito mais curto de experimentar o fuzzer em um projeto existente.

## Como funciona
Baixe e extraia o release, compile o teste com o jazzer_standalone.jar no classpath e invoque ./jazzer --cp=... --target_class=... (jazzer.exe no Windows).

## Exemplo
Se aparecer erro de libjvm.so não encontrada, aponte JAVA_HOME para uma JDK e repita — a correção consta do próprio README.

## Limites e trade-offs
A JVM do release é fixa ao pacote; se o projeto exige outra versão de runtime, o caminho é invocar a main class com a sua própria JVM.

## Como verificar
Extraia o release, rode um alvo mínimo e confirme que o fuzzer imprime o log de iterações sem setup adicional.

## Conexões
- [[jazzer-coverage-guided-jvm]] — Veja também: Jazzer: fuzzing em processo para a JVM.
- [[jazzer-main-class-invocation]] — Veja também: Jazzer: chamar a classe main diretamente.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — releases no GitHub](https://github.com/CodeIntelligenceTesting/jazzer/releases) — binários standalone e notas de versão; consultado em 2026-10-03.
