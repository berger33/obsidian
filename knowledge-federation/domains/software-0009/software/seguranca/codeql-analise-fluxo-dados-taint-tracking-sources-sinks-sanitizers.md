---
id: software.seguranca.tranche11.001073
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/github/codeql/main/README.md", "https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Análise Interprocedural de **Fluxo de Dados e *Taint Tracking*** no CodeQL (`DataFlow::ConfigSig` / `TaintTracking::Global`): **`isSource`**, **`isSink`** e **`isBarrier`**

## Em uma frase
O verdadeiro superpoder do CodeQL sobre scanners baseados em regex ou AST local é a sua capacidade de realizar **Taint Tracking Interprocedural Global**: rastrear um dado não-confiável controlado pelo usuário (**`Source`**) desde o controlador HTTP (`req.query.id`), passando por 12 funções, 4 objetos DTO e 3 arquivos diferentes, até chegar a uma operação perigosa (**`Sink`**, como `cursor.execute(sql)` ou `os.system(cmd)`) — verificando se em algum ponto do caminho houve uma função de validação/escape (**`Barrier` / `Sanitizer`**)!

## Por que importa
Na API moderna do CodeQL (`DataFlow::ConfigSig` e `TaintTracking::Global<MyConfig>`), você modela qualquer vulnerabilidade de injeção implementando apenas três predicados em um módulo `module MyFlowConfig implements DataFlow::ConfigSig`: **(1) ` predicate isSource(DataFlow::Node source)`**; **(2) `predicate isSink(DataFlow::Node sink)`**; e **(3) `predicate isBarrier(DataFlow::Node node)`** (e opcionalmente `isAdditionalFlowStep` para propagar o taint através de serializadores customizados)!

## Como funciona
Qual é a diferença entre `DataFlow` e `TaintTracking` no CodeQL? **`DataFlow`** rastreia apenas quando o valor exato é preservado (`y = x`), enquanto **`TaintTracking`** rastreia mesmo quando o valor contaminado é modificado ou concatenado (`y = "SELECT * FROM t WHERE id=" + x`)!

## Exemplo
```ql
/**
 * @name Fluxo de Taint de entrada HTTP ate execucao de comando de sistema
 * @kind path-problem
 * @problem.severity error
 * @id js/custom-command-injection-flow
 */
import javascript
import DataFlow::PathGraph

module CmdInjectionConfig implements DataFlow::ConfigSig {
  predicate isSource(DataFlow::Node source) {
    source instanceof RemoteFlowSource
  }

  predicate isSink(DataFlow::Node sink) {
    exists(SystemCommandExecution sys | sink = sys.getACommandArgument())
  }
}

module CmdInjectionFlow = TaintTracking::Global<CmdInjectionConfig>;

from CmdInjectionFlow::PathNode source, CmdInjectionFlow::PathNode sink
where CmdInjectionFlow::flowPath(source, sink)
select sink.getNode(), source, sink, "Comando de sistema construido a partir de $@.", source.getNode(), "entrada HTTP nao confiavel"
```

## Limites e trade-offs
Olhe que arquitetura limpa na query `@kind path-problem` acima: ao importar **`DataFlow::PathGraph`** e selecionar `select sink.getNode(), source, sink, ...`, o GitHub Code Scanning e o VS Code desenham na tela do desenvolvedor **cada linha e cada chamada de função intermediária por onde o dado malicioso viajou desde a requisição HTTP (`RemoteFlowSource`) até o `child_process.exec`**!

## Como verificar
Quando um time usa uma função interna de validação (ex.: `validarUuidEstrito(input)`), basta adicioná-la em `predicate isBarrier(DataFlow::Node node)` para eliminar falsos positivos em todo o repositório.

## Conexões
- [[codeql-linguagem-ql-predicados-classes-logica-declarativa-datalog]] — Veja também: Fundamentos da Linguagem **QL (`.ql`)** no CodeQL: Estrutura **`from ... where ... select`**, Predicados Lógicos, Classes de AST e Recursão Transitiva (`+` e `*`).
- [[codeql-suites-consultas-default-security-extended-security-and-quality]] — Veja também: Suítes Oficiais de Consultas do CodeQL (**`.qls`**): Diferenças entre **`default`**, **`security-extended`** e **`security-and-quality`** e Filtros de Query Suite.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.
- [[codeql-variant-analysis-pesquisa-vulnerabilidades-zero-day-escala]] — Referência cruzada direta com codeql-variant-analysis-pesquisa-vulnerabilidades-zero-day-escala.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
