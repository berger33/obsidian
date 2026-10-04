---
id: software.seguranca.tranche11.001079
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

# Engenharia de Qualidade em Regras SAST: Pacotes **`qlpack.yml`** e Testes Unitários Automatizados de Consultas `.ql` com **`codeql test run`** (`.expected`)

## Em uma frase
Em equipes maduras de Engenharia de Segurança, regras de detecção de vulnerabilidades (`.ql`) são tratadas como código de produção: toda consulta customizada precisa residir em um **Pacote CodeQL (`qlpack.yml`)** versionado no Git e possuir **Testes Unitários Automatizados (`codeql test run`)** que garantam que ela detecta os verdadeiros positivos e não dispara em código seguro!

## Por que importa
Como funciona a estrutura de um teste unitário no CodeQL? Para uma consulta `SqlInjectionCustom.ql`, você cria uma pasta de teste contendo: **(1)** Um pequeno arquivo de código de exemplo (ex.: ` test.py`) com casos vulneráveis (`# BAD`) e casos seguros sanitizados (`# GOOD`); **(2)** Um arquivo `.qlref` apontando para a sua query; e **(3)** Um arquivo de gabarito **`SqlInjectionCustom.expected`** contendo a tabela exata de linhas e mensagens que a query deve produzir!

## Como funciona
Ao rodar **`codeql test run ./tests`**, o CodeQL constrói um mini-banco de dados de teste em segundos, executa a query e compara a saída com o arquivo `.expected` (`diff`), falhando se qualquer falso positivo novo surgir ou se um caso vulnerável deixar de ser detectado!

## Exemplo
```yaml
# qlpack.yml — Definicao de um pacote de consultas CodeQL customizadas da equipe de AppSec com dependencia da biblioteca Python
name: corp-secops/python-custom-queries
version: 1.0.0
dependencies:
  codeql/python-all: "*"
extractor: python
```

## Limites e trade-offs
Para inicializar um novo pacote de consultas ou um pacote de testes pela linha de comando, basta rodar **`codeql pack init corp-secops/minhas-queries`** e instalar as dependências com **`codeql pack install`**!

## Como verificar
Ao abrir um Pull Request adicionando ou alterando uma regra `.ql` ou um Model Pack YAML da empresa, configure o GitHub Actions para rodar `codeql test run`: isso garante zero regressões nas regras SAST da organização.

## Conexões
- [[codeql-auditoria-workflows-github-actions-injection-pwn-requests]] — Veja também: Auditoria de Segurança de Pipelines CI/CD (**GitHub Actions**) com CodeQL (`--language=actions`): Detectando **Expression Injection** e **`pull_request_target` (*Pwn Requests*)**.
- [[codeql-otimizacao-performance-ram-threads-cache-ci-cd]] — Veja também: Otimização de Performance e Recursos do CodeQL em Grande Escala: Calibração de **`--threads`**, **`--ram`**, Compilation Cache e Exclusão de Caminhos (`paths-ignore`).
- [[codeql-model-packs-data-extensions-frameworks-internos-yaml]] — Referência cruzada direta com codeql-model-packs-data-extensions-frameworks-internos-yaml.
- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — Referência cruzada direta com codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg.

## Fontes
- [GitHub CodeQL Official Repository — Standard Libraries, Security Queries & Model Packs](https://raw.githubusercontent.com/github/codeql/main/README.md) — repositório oficial do GitHub CodeQL contendo as bibliotecas padrão QL, suítes de consultas de segurança e extensões de modelos; consultado em 2026-10-03.
- [GitHub Official Documentation — About the CodeQL CLI (`database create`, `database analyze`, `github upload-results`)](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli) — documentação oficial da CLI do CodeQL cobrindo criação de bancos de dados relacionais de código, análise SARIF e suporte multi-linguagem; consultado em 2026-10-03.
