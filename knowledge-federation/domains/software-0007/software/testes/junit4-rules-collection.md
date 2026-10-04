---
id: software.testes.tranche23.001678
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
fontes: ["https://github.com/junit-team/junit4/wiki/Rules", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O kit de regras: ExternalResource, ErrorCollector, Verifier, TestWatcher

## Em uma frase
A página Rules define o propósito do mecanismo — adicionar ou redefinir de forma flexível o comportamento de cada método de teste, com a opção de estender as regras fornecidas ou escrever a sua — e documenta quatro utilitárias: ExternalResource para conectar recursos antes e desconectar depois (override before/after), ErrorCollector para continuar após o primeiro problema e reportar todos juntos, Verifier para transformar teste verde em falha ao final, TestWatcher para observar ações sem modificá-las.

## Por que importa
Coletores de erro e watchers existem para padrões que asserts isolados não expressam: validar todas as linhas de uma tabela antes de falhar, logar causas de falha, fechar sockets com garantia — tudo reutilizável entre classes.

## Como funciona
A página ancora a linhagem: TestWatcher substituiu TestWatchman desde o 4.9 (TestRule em vez da MethodRule, esta deprecada), e os exemplos mostram as quatro classes compostas no mesmo teste, com ErrorCollector somando dois Throwable reportados de uma vez.

## Exemplo
Adicione um ErrorCollector a um teste que valida N linhas de arquivo e substitua o assert do laço por collector.checkThat; com duas linhas erradas, a falha deve listar os dois problemas, não o primeiro.

## Limites e trade-offs
A página documenta os contratos, não as armadilhas de composição: a ordem de várias regras no mesmo campo/classe segue os detalhes do mecanismo TestRule (Statement encadeado), e a própria página Rules mantém exemplos que a doc de exceções já marcou como deprecados, sinal de wiki com idades mistas.

## Como verificar
Abra a página Rules do wiki do junit4 e confira a definição de propósito, o padrão before/after do ExternalResource, o exemplo duplo do ErrorCollector e a nota de linhagem TestWatchman/TestWatcher.

## Conexões
- [[junit4-temporaryfolder]] — Veja também: TemporaryFolder apaga sozinha — e pode cobrar prova disso.
- [[junit4-parameterized]] — Veja também: Parameterized: o produto cartesiano entre testes e dados.

## Fontes
- [JUnit 4 — Rules (wiki)](https://github.com/junit-team/junit4/wiki/Rules) — TemporaryFolder, ExternalResource, ErrorCollector, Verifier e TestWatcher; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
