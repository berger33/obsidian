---
id: software.seguranca.tranche11.001075
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

# **Variant Analysis** com CodeQL e **Multi-Repository Variant Analysis (MRVA)**: Encontrando Todas as Variantes de um *Zero-Day / Bug* em Milhares de Repositórios

## Em uma frase
O conceito de **Variant Analysis (Análise de Variantes)** é a razão pela qual equipes de pesquisa de vulnerabilidades (como o **GitHub Security Lab**, Google Project Zero e Microsoft MSRC) usam o CodeQL diariamente.

## Por que importa
Como funciona o ciclo de *Variant Analysis*? Quando uma vulnerabilidade é descoberta em uma auditoria manual, pentest ou programa de Bug Bounty (o "Bug Semente"), um engenheiro comum apenas corrige aquela linha de código específica e fecha o chamado. Já o engenheiro de segurança que pratica **Variant Analysis** faz uma pergunta muito mais estratégica: ***"Qual é o padrão semântico exato que tornou essa linha vulnerável, e em quais outros lugares deste repositório — ou dos outros 1.000 repositórios da empresa — nós cometemos exatamente o mesmo erro?"***

## Como funciona
Você transforma o bug encontrado em uma consulta `.ql` generalizada e a executa contra o banco do projeto ou, usando o **Multi-Repository Variant Analysis (MRVA)** no VS Code + GitHub Actions, dispara a consulta em paralelo contra **até 1.000 repositórios de uma só vez**!

## Exemplo
```bash
# Baixar pacotes oficiais de queries do CodeQL via CLI e executar uma consulta customizada de Variant Analysis contra multiplos bancos
codeql pack download codeql/python-queries codeql/javascript-queries
codeql database analyze codeql-dbs/python \
  ./queries-internas/variante-idor-checkout.ql \
  --format=sarif-latest \
  --output=variant-hunt.sarif
```

## Limites e trade-offs
Na prática corporativa, sempre que um pentest externo ou incidente de produção encontrar uma falha de lógica ou autorização (ex.: um endpoint interno que esqueceu de chamar o decorador `@require_tenant_scope` antes de acessar o banco), escreva uma query `.ql` de 15 linhas que verifica todos os endpoints que acessam o banco sem o decorador: você não apenas encontra todas as variantes ocultas hoje, como impede que o erro volte a acontecer no futuro!

## Como verificar
Adicione um teste unitário para sua nova query `.ql` usando **`codeql test run`**!

## Conexões
- [[codeql-suites-consultas-default-security-extended-security-and-quality]] — Veja também: Suítes Oficiais de Consultas do CodeQL (**`.qls`**): Diferenças entre **`default`**, **`security-extended`** e **`security-and-quality`** e Filtros de Query Suite.
- [[codeql-model-packs-data-extensions-frameworks-internos-yaml]] — Veja também: Extensão Semântica sem Escrever Código QL: **CodeQL Model Packs & Data Extensions (`models-as-data` em YAML)** para Mapear Bibliotecas Internas.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.
- [[codeql-linguagem-ql-predicados-classes-logica-declarativa-datalog]] — Referência cruzada direta com codeql-linguagem-ql-predicados-classes-logica-declarativa-datalog.
- [[codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers]] — Referência cruzada direta com codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
