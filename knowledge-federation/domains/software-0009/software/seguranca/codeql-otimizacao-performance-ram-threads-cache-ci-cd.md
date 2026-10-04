---
id: software.seguranca.tranche11.001080
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

# Otimização de Performance e Recursos do CodeQL em Grande Escala: Calibração de **`--threads`**, **`--ram`**, Compilation Cache e Exclusão de Caminhos (`paths-ignore`)

## Em uma frase
Ao rodar o CodeQL sobre monorepos grandes de **C/C++, Java ou TypeScript**, duas configurações incorretas de infraestrutura podem fazer a análise demorar horas ou falhar com erro de falta de memória (`Out of Memory — OOM` no avaliador QL): subdimensionar a RAM reservada para o avaliador ou analisar milhões de linhas de código minificado/gerado (`dist/`, `vendor/`, `node_modules/`).

## Por que importa
Conforme recomenda a documentação oficial (`Recommended hardware resources for running CodeQL`), utilize três alavancas técnicas no `codeql database analyze`: **(1) `--threads=0`** — instrui o CodeQL a detectar e usar todos os núcleos de CPU disponíveis no runner; **(2) `--ram=<MB>`** — define o orçamento explícito de memória RAM (em megabytes) para o motor de avaliação QL e JVM (deixando pelo menos 1,5 GB a 2 GB livres para o sistema operacional do container para evitar que o Linux OOM Killer mate o processo!);

## Como funciona
e **(3) `paths-ignore` / filtros de extração** para excluir código de terceiros (`vendor/`, `third_party/`, `*.min.js`)!

## Exemplo
```bash
# Executar o codeql database analyze utilizando todos os nucleos de CPU (--threads=0), alocando 12 GB de RAM (--ram=12288) e cache
codeql database analyze codeql-dbs/java \
  codeql/java-queries:codeql-suites/java-security-extended.qls \
  --threads=0 \
  --ram=12288 \
  --format=sarif-latest \
  --output=java-extended.sarif
```

## Limites e trade-offs
Dica para linguagens dinâmicas (**JavaScript/TypeScript e Python**): arquivos JavaScript *bundled/minified* (`*.bundle.js`, `*.min.js`, `dist/`, `build/`) não devem ser incluídos no banco CodeQL — além de triplicarem o tempo de análise e consumo de RAM, alertas apontando para a coluna `48592` de um arquivo minificado não servem para o desenvolvedor corrigir o código original!

## Como verificar
Se uma única consulta customizada estiver demorando muito na sua suíte, adicione a flag **`--evaluator-log=eval.log`** e execute `codeql generate log-summary eval.log` para identificar exatamente qual predicado `.ql` está gerando um produto cartesiano custoso.

## Conexões
- [[codeql-testes-unitarios-qlpacks-codeql-test-run-expected]] — Veja também: Engenharia de Qualidade em Regras SAST: Pacotes **`qlpack.yml`** e Testes Unitários Automatizados de Consultas `.ql` com **`codeql test run`** (`.expected`).
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.
- [[codeql-suites-consultas-default-security-extended-security-and-quality]] — Referência cruzada direta com codeql-suites-consultas-default-security-extended-security-and-quality.
- [[codeql-modos-build-compiled-languages-none-autobuild-manual]] — Referência cruzada direta com codeql-modos-build-compiled-languages-none-autobuild-manual.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
