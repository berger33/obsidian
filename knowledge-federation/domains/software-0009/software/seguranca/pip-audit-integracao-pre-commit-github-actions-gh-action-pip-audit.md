---
id: software.seguranca.tranche16.001588
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/pypa/pip-audit/main/README.md", "https://raw.githubusercontent.com/pypa/advisory-database/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Automação Shift-Left do `pip-audit`: Hook Oficial **`pre-commit`** e GitHub Action Oficial (**`pypa/gh-action-pip-audit`**)

## Em uma frase
Como impedir que um desenvolvedor faça commit de uma biblioteca Python vulnerável no `requirements.txt` ou `pyproject.toml` **antes mesmo de abrir o Pull Request (via `pre-commit`)** e validar novamente em cada Pull Request e agendado diariamente no **GitHub Actions**?

## Por que importa
Conforme documentado no `README.md` oficial, o projeto mantém integrações nativas oficiais para ambos: **(1) Suporte nativo ao `pre-commit`** (apontando para `repo: https://github.com/pypa/pip-audit` com `id: pip-audit` e `args: ["-r", "requirements.txt"]`) e **(2) A GitHub Action oficial `pypa/gh-action-pip-audit`**!

## Como funciona
A GitHub Action oficial `pypa/gh-action-pip-audit` aceita entradas declarativas (`inputs: requirements.txt`, `vulnerability-service: osv`, `require-hashes: true`, `virtual-environment: ...`) e gera resumos formatados diretamente no *Job Summary* do GitHub Actions!

## Exemplo
```yaml
# Exemplo de configuracao oficial do hook pip-audit no arquivo .pre-commit-config.yaml da raiz do repositorio Python
repos:
  - repo: https://github.com/pypa/pip-audit
    rev: v2.10.1
    hooks:
      - id: pip-audit
        args: ["-r", "requirements.txt", "--strict"]
```

## Limites e trade-offs
Preste atenção à nota oficial no `README.md` sobre o serviço em nuvem **`pre-commit.ci`**: como o ambiente sandboxed do `pre-commit.ci` bloqueia chamadas de rede externas (e o `pip-audit` precisa consultar a API PyPI/OSV na rede), se você usar `pre-commit.ci` adicione `ci: skip: [pip-audit]` no `.pre-commit-config.yaml` e execute a **`pypa/gh-action-pip-audit`** no seu workflow normal do GitHub Actions!

## Como verificar
No workflow do GitHub Actions, além do gatilho `on: [push, pull_request]`, inclua sempre um gatilho agendado **`on: schedule: - cron: '0 6 * * *'`** (diariamente às 06:00): assim, mesmo que nenhum código tenha mudado no repositório, se uma nova CVE (`PYSEC-*`) for descoberta hoje em uma biblioteca já em produção, o pipeline avisa sua equipe na manhã seguinte!

## Conexões
- [[pip-audit-indices-privados-index-url-extra-index-url-cache-offline]] — Veja também: Usando o `pip-audit` com **Repositórios PyPI Privados (`--index-url` / `--extra-index-url`)**, Autenticação `keyring` e Cache HTTP (`--cache-dir`).
- [[pip-audit-anatomia-pypa-advisory-database-osv-schema-imports]] — Veja também: Anatomia da Base **`pypa/advisory-database`**: Formato **OpenSSF OSV YAML (`PYSEC-*`)**, Validação `check-jsonschema` e **`ecosystem_specific.imports`**.
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.
- [[pip-audit-modos-varredura-requirements-pyproject-locked-local-venv]] — Referência cruzada direta com pip-audit-modos-varredura-requirements-pyproject-locked-local-venv.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
