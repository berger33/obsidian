---
id: software.seguranca.tranche11.001074
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

# Suítes Oficiais de Consultas do CodeQL (**`.qls`**): Diferenças entre **`default`**, **`security-extended`** e **`security-and-quality`** e Filtros de Query Suite

## Em uma frase
Ao configurar o CodeQL no GitHub Actions ou via `codeql database analyze`, qual **Query Suite (`.qls`)** você deve escolher? Muitos engenheiros deixam apenas o conjunto `default` e não percebem que dezenas de regras importantes de segurança não estão rodando!

## Por que importa
O repositório oficial `github/codeql` fornece três suítes graduadas para cada linguagem: **(1) `<lang>-code-scanning.qls` (`default`)** — executa apenas as regras de segurança de **altíssima precisão e baixíssimo falso positivo**, ideal como bloqueador obrigatório (*Merge Gate*) em Pull Requests; **(2) `<lang>-security-extended.qls` (`security-extended`)** — adiciona dezenas de consultas de segurança com precisão média/alta e heurísticas mais amplas de *taint tracking* (recomendado pela própria GitHub para auditorias completas de AppSec!); e **(3) `<lang>-security-and-quality.qls`** — inclui todas as regras de `security-extended` somadas a regras de manutenibilidade, *dead code* e confiabilidade!

## Como funciona
Além disso, você pode criar seu próprio arquivo **`.qls` (*Query Suite YAML*)** combinando seletores `queries`, `qlpack` e filtros `include` / `exclude` por `@precision`, `@problem.severity` ou `@tags`!

## Exemplo
```yaml
# custom-secops-suite.qls — Suite CodeQL customizada incluindo regras de seguranca com precisao high/very-high e consultas internas
- description: Suite Corporativa de AppSec (CodeQL Security Extended + Regras Internas)
- qlpack: codeql/python-queries
- include:
    kind:
      - problem
      - path-problem
    precision:
      - high
      - very-high
    tags contain:
      - security
- exclude:
    id: py/clear-text-logging-sensitive-data
```

## Limites e trade-offs
Executar a suíte **`default`** de forma síncrona nos Pull Requests (bloqueando o merge em menos de 3 minutos sem ruído) e agendar a suíte **`security-extended`** em um workflow semanal noturno para a equipe de AppSec triar no GitHub Security Tab / DefectDojo combina velocidade para o desenvolvedor com profundidade para a segurança.

## Como verificar
Use `codeql resolve queries custom-secops-suite.qls` na CLI para testar e listar exatamente quais arquivos `.ql` serão executados pela sua suíte customizada antes de colocá-la em produção.

## Conexões
- [[codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers]] — Veja também: Análise Interprocedural de **Fluxo de Dados e *Taint Tracking*** no CodeQL (`DataFlow::ConfigSig` / `TaintTracking::Global`): **`isSource`**, **`isSink`** e **`isBarrier`**.
- [[codeql-variant-analysis-pesquisa-vulnerabilidades-zero-day-escala]] — Veja também: **Variant Analysis** com CodeQL e **Multi-Repository Variant Analysis (MRVA)**: Encontrando Todas as Variantes de um *Zero-Day / Bug* em Milhares de Repositórios.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
