---
id: software.seguranca.tranche11.001076
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

# Extensão Semântica sem Escrever Código QL: **CodeQL Model Packs & Data Extensions (`models-as-data` em YAML)** para Mapear Bibliotecas Internas

## Em uma frase
Imagine que sua empresa possui uma biblioteca interna proprietária em Java, C#, Python ou Go (ex.: `br.com.empresa.http.InternalRequest` para ler dados do usuário e `br.com.empresa.db.CustomJdbcWrapper.runRawSql()` para executar queries no banco).

## Por que importa
Por que o CodeQL padrão pode não reportar um SQL Injection quando os dados passam por essa biblioteca interna? Porque o pacote oficial do CodeQL conhece frameworks públicos (Spring, Django, Express, Hibernate, JDBC), mas **não sabe que `InternalRequest.getHeader()` é um `Source` de dados não-confiáveis nem que `CustomJdbcWrapper.runRawSql()` é um `Sink` de SQL Injection**!

## Como funciona
Em vez de ter que reescrever todas as consultas `.ql` oficiais da GitHub, o CodeQL introduziu os **Model Packs (`models-as-data` / Data Extensions em YAML)**: você escreve um simples arquivo YAML declarando `sourceModel`, `sinkModel` e `summaryModel` (propagação de taint) para os métodos da sua biblioteca interna, e **todas as centenas de queries oficiais de SQLi, XSS, SSRF e Command Injection do CodeQL passam automaticamente a enxergar seus métodos internos**!

## Exemplo
```yaml
# extensions/custom-corp-models.yml — Declarar Sources, Sinks e Summaries de bibliotecas internas em YAML (Models as Data)
extensions:
  - addsTo:
      pack: codeql/java-all
      extensible: sourceModel
    data:
      - ["br.com.empresa.http", "InternalRequest", True, "getUntrustedParam", "(String)", "", "ReturnValue", "remote", "manual"]
  - addsTo:
      pack: codeql/java-all
      extensible: sinkModel
    data:
      - ["br.com.empresa.db", "CustomJdbcWrapper", True, "runRawSql", "(String)", "", "Argument[0]", "sql-injection", "manual"]
```

## Limites e trade-offs
Olhe o ganho de escala de engenharia dos **Data Extensions (`models-as-data`)**: ao publicar um único pacote `corp-secops/java-internal-models` (via `codeql pack publish`) e passá-lo com `--model-packs`, você ensina a semântica dos seus SDKs internos para todas as queries do CodeQL sem duplicar uma única linha de lógica `.ql`!

## Como verificar
Você também pode usar o editor visual **`CodeQL Model Editor`** dentro da extensão oficial do VS Code para gerar esses arquivos YAML com poucos cliques.

## Conexões
- [[codeql-variant-analysis-pesquisa-vulnerabilidades-zero-day-escala]] — Veja também: **Variant Analysis** com CodeQL e **Multi-Repository Variant Analysis (MRVA)**: Encontrando Todas as Variantes de um *Zero-Day / Bug* em Milhares de Repositórios.
- [[codeql-modos-build-compiled-languages-none-autobuild-manual]] — Veja também: Criando Bancos CodeQL para Linguagens Compiladas (**C/C++, Java, Kotlin, C#, Go, Rust, Swift**): Modos **`build-mode: none`**, **`autobuild`** e **`manual`**.
- [[codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers]] — Referência cruzada direta com codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.
- [[codeql-testes-unitarios-qlpacks-codeql-test-run-expected]] — Referência cruzada direta com codeql-testes-unitarios-qlpacks-codeql-test-run-expected.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
