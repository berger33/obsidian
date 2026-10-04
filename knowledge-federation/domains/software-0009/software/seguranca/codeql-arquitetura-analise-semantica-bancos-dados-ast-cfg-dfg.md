---
id: software.seguranca.tranche11.001071
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

# **GitHub CodeQL (`github/codeql`)**: Arquitetura de **Análise Semântica de Código (*Code as Data*)**, Extratores de Linguagem e Bancos Relacionais (`AST`, `CFG`, `DFG`)

## Em uma frase
Criado originalmente pela **Semmle** (pesquisa da Universidade de Oxford) e hoje motor central do **GitHub Advanced Security / Code Scanning (`github/codeql`)**, o **CodeQL** revolucionou a Análise Estática de Segurança (SAST) e a pesquisa de vulnerabilidades (*Variant Analysis*) ao tratar **código-fonte como um banco de dados relacional consultável**!

## Por que importa
Qual é a diferença arquitetural entre um buscador de padrões sintáticos e o **CodeQL**? Conforme documenta o guia oficial do `codeql-cli`, o processo do CodeQL ocorre em três fases: **(1) `codeql database create`** — um **Extrator (*Extractor*)** específico da linguagem intercepta a compilação real (para linguagens compiladas como **C/C++, C#, Go, Java, Kotlin, Rust e Swift**) ou analisa os módulos diretamente (para **JavaScript/TypeScript, Python, Ruby e GitHub Actions**), extraindo a **Árvore de Sintaxe Abstrata (`AST`)**, o **Grafo de Fluxo de Controle (`CFG`)**, a **Hierarquia de Tipos** e o **Grafo de Fluxo de Dados (`DFG`)** em um banco relacional imutável!

## Como funciona
Depois, **(2) `codeql database analyze`** executa consultas escritas na linguagem lógica declarativa orientada a objetos **QL (`.ql`)** (derivada de *Datalog*), gerando alertas interprocedurais precisos em **SARIF**; e **(3) `codeql github upload-results`** publica os caminhos de código no GitHub!

## Exemplo
```bash
# Criar bancos de dados CodeQL para um repositorio multi-linguagem (Java e Python) e executar a analise gerando SARIF
codeql database create codeql-dbs \
  --source-root=. \
  --db-cluster \
  --language=java,python

codeql database analyze codeql-dbs/python \
  codeql/python-queries:codeql-suites/python-security-extended.qls \
  --format=sarif-latest \
  --output=python-results.sarif
```

## Limites e trade-offs
Observe a flag **`--db-cluster`** no comando `codeql database create` acima: quando um repositório contém múltiplas linguagens (por exemplo, backend em `java` ou `go` e scripts/serviços em `python` e `javascript`), `--db-cluster` cria sub-bancos separados para cada linguagem em uma única invocação!

## Como verificar
Nota técnica da documentação oficial: a CLI do CodeQL requer distribuições Linux baseadas em `glibc` (Ubuntu/Debian/RHEL) e não suporta diretamente containers `musl` (Alpine Linux) sem camada de compatibilidade.

## Conexões
- [[codeql-linguagem-ql-predicados-classes-logica-declarativa-datalog]] — Veja também: Fundamentos da Linguagem **QL (`.ql`)** no CodeQL: Estrutura **`from ... where ... select`**, Predicados Lógicos, Classes de AST e Recursão Transitiva (`+` e `*`).
- [[codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers]] — Referência cruzada direta com codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers.
- [[mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif]] — Referência cruzada direta com mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
