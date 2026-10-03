---
id: software.seguranca.tranche11.001072
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

# Fundamentos da Linguagem **QL (`.ql`)** no CodeQL: Estrutura **`from ... where ... select`**, Predicados Lógicos, Classes de AST e Recursão Transitiva (`+` e `*`)

## Em uma frase
Por que a linguagem **QL** do CodeQL parece SQL à primeira vista (`from ... where ... select`), mas é capaz de atravessar chamadas recursivas e hierarquias de herança complexas em segundos?

## Por que importa
Porque sob a sintaxe familiar `from <variaveis> where <condicoes_logicas> select <resultado>`, o QL é uma **Linguagem de Programação em Lógica Declarativa baseada em Datalog** com semântica de ponto fixo (*least fixed point*)!

## Como funciona
Em uma consulta `.ql`, você declara variáveis tipadas pelas classes da biblioteca padrão da linguagem (ex.: `import python`, `import javascript`, `import cpp`, `import java`): **`Function`** (funções/métodos), **`Call` / `MethodCall`** (chamadas de função), **`Expr`** (expressões), **`IfStmt`** (blocos condicionais) e **`Parameter`**; além disso, os operadores de **Fechamento Transitivo `+` (1 ou mais passos)** e **`*` (0 ou mais passos)** permitem consultar em 1 caractere se uma classe herda transitivamente de outra ou se uma função chama outra através de `N` camadas!

## Exemplo
```ql
/**
 * @name Funcoes Python que invocam eval() ou exec() diretamente
 * @kind problem
 * @problem.severity error
 * @id py/custom-direct-eval-call
 */
import python

from Call call, Name funcName
where
  call.getFunc() = funcName and
  funcName.getId() in ["eval", "exec"]
select call, "Chamada perigosa a " + funcName.getId() + "() detectada dentro do modulo."
```

## Limites e trade-offs
Repare no bloco de metadados **`/** ... @name ... @kind problem ... */`** no topo da consulta `.ql`: no CodeQL, esse cabeçalho **JSDoc/QLDoc não é um comentário decorativo** — ele é obrigatório para o gerador SARIF saber se a query retorna um alerta simples (`@kind problem`) ou um grafo completo de fluxo de dados (`@kind path-problem`), qual é a severidade (`@problem.severity`) e qual é o CWE (`@tags security external/cwe/cwe-094`)!

## Como verificar
Use a extensão oficial **`CodeQL for Visual Studio Code` (`GitHub.vscode-codeql`)** para escrever queries `.ql` com autocompletar (`IntelliSense`) e visualização interativa da AST (`View AST`).

## Conexões
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Veja também: **GitHub CodeQL (`github/codeql`)**: Arquitetura de **Análise Semântica de Código (*Code as Data*)**, Extratores de Linguagem e Bancos Relacionais (`AST`, `CFG`, `DFG`).
- [[codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers]] — Veja também: Análise Interprocedural de **Fluxo de Dados e *Taint Tracking*** no CodeQL (`DataFlow::ConfigSig` / `TaintTracking::Global`): **`isSource`**, **`isSink`** e **`isBarrier`**.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
