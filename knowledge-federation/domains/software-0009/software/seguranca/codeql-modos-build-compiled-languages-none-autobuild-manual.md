---
id: software.seguranca.tranche11.001077
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

# Criando Bancos CodeQL para Linguagens Compiladas (**C/C++, Java, Kotlin, C#, Go, Rust, Swift**): Modos **`build-mode: none`**, **`autobuild`** e **`manual`**

## Em uma frase
Historicamente, analisar linguagens compiladas (como **Java, Kotlin, C# e C/C++**) no CodeQL exigia sempre compilar o projeto inteiro dentro do pipeline de segurança para que o extrator do CodeQL interceptasse as chamadas ao compilador (`javac`, `kotlinc`, `csc`, `gcc`, `clang`).

## Por que importa
Hoje, a CLI moderna do CodeQL suporta três modos de construção (**`--build-mode`**) que você deve escolher de acordo com a linguagem e a velocidade desejada: **(1) `--build-mode=none` (*Buildless / Sem Compilação*)** — já suportado para **Java, C# e Rust** (além de Python/JS/Ruby), gera o banco de dados CodeQL analisando diretamente o código-fonte e resolvendo dependências sem precisar rodar o build completo (muito mais rápido e resiliente quando o build exige credenciais ou infraestrutura complexa!); **(2) `--build-mode=autobuild`** — o CodeQL detecta automaticamente Maven, Gradle, MSBuild, Ant ou CMake e executa o build;

## Como funciona
e **(3) `--build-mode=manual` (`--command="..."`)** — você passa o script exato de compilação (obrigatório para builds C/C++ customizados)!

## Exemplo
```bash
# Comparar a criacao de banco CodeQL em modo Buildless (--build-mode=none para Java) vs modo Manual (--command para C/C++)
codeql database create java-db \
  --language=java \
  --build-mode=none \
  --source-root=.

codeql database create cpp-db \
  --language=cpp \
  --command="make -j4 clean all" \
  --source-root=.
```

## Limites e trade-offs
Quando usar `--build-mode=none` vs `--build-mode=manual` em projetos **Java / C#**? Use **`--build-mode=none`** para triagem rápida em larga escala (ou quando você não tem acesso aos servidores de artefatos privados do cliente durante uma auditoria de código!) e use **`--build-mode=autobuild` / `manual`** nos repositórios onde parte do código-fonte é gerada dinamicamente durante a compilação (como *annotation processors*, Protobuf ou gRPC)!

## Como verificar
Em projetos **C/C++**, se o comando `make` já tiver compilado os arquivos `.o` antes de você chamar `codeql database create`, o compilador não fará nada e o banco ficará vazio: por isso inclua sempre `make clean` (ou `cmake --build . --clean-first`) dentro de `--command`!

## Conexões
- [[codeql-model-packs-data-extensions-frameworks-internos-yaml]] — Veja também: Extensão Semântica sem Escrever Código QL: **CodeQL Model Packs & Data Extensions (`models-as-data` em YAML)** para Mapear Bibliotecas Internas.
- [[codeql-auditoria-workflows-github-actions-injection-pwn-requests]] — Veja também: Auditoria de Segurança de Pipelines CI/CD (**GitHub Actions**) com CodeQL (`--language=actions`): Detectando **Expression Injection** e **`pull_request_target` (*Pwn Requests*)**.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.
- [[codeql-otimizacao-performance-ram-threads-cache-ci-cd]] — Referência cruzada direta com codeql-otimizacao-performance-ram-threads-cache-ci-cd.
- [[mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif]] — Referência cruzada direta com mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
