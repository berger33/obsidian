---
id: software.testes.tranche18.001184
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://junit.org/junit5/docs/current/user-guide/", "https://github.com/junit-team/junit5"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit 5: habilitar execução paralela

## Em uma frase
A execução paralela é opcional e configurada por parâmetros que definem modo padrão, modo por classe e estratégia de paralelismo.

## Por que importa
Suítes grandes reduzem o tempo de retorno quando os casos são independentes, e a configuração explícita evita surpresas de concorrência.

## Como funciona
Habilite por configuração, escolha a estratégia de paralelismo e marque como concorrentes apenas os escopos que suportam execução simultânea.

## Exemplo
É possível manter classes sequenciais e permitir que métodos de uma mesma classe rodem em paralelo, conforme a natureza dos recursos usados.

## Limites e trade-offs
Recursos compartilhados sem sincronização produzem falhas intermitentes, e o paralelismo não corrige testes que dependem de ordem.

## Como verificar
Execute a suíte com e sem paralelismo e compare o resultado, investigando divergências como sinal de estado compartilhado.

## Conexões
- [[junit5-dependency-injection]] — Veja também: JUnit 5: receber parâmetros resolvidos.
- [[junit5-tagging-and-filtering]] — Veja também: JUnit 5: selecionar testes com etiquetas.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
