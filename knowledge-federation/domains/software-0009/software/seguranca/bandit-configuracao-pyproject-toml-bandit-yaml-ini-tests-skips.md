---
id: software.seguranca.tranche03.000262
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://bandit.readthedocs.io/en/latest/config.html", "https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst", "https://github.com/PyCQA/bandit"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bandit Configuração Declarativa (`pyproject.toml`, `bandit.yaml` e `.bandit`): controle de `exclude_dirs`, `tests` e `skips`

## Em uma frase
Conforme detalhado na documentação oficial de configuração (`bandit.readthedocs.io/en/latest/config.html`), o Bandit pode ser configurado via arquivo **`pyproject.toml`** (seção `[tool.bandit]`), arquivo **`bandit.yaml`** ou arquivo INI **`.bandit`**, definindo centralmente os diretórios excluídos (**`exclude_dirs`**), a lista de testes a incluir (**`tests`**) e a lista de testes a pular (**`skips`**).

## Por que importa
Em quase todo projeto Python usando `pytest`, os arquivos de teste em `tests/` usam a instrução `assert` centenas de vezes; se você não excluir `tests` em `exclude_dirs` (ou pular `B101` nos testes), o Bandit reportará centenas de alertas `B101 (assert_used)` irrelevantes!

## Como funciona
Ao centralizar a configuração em `[tool.bandit]` dentro do `pyproject.toml` (instalando `bandit[toml]`) e invocar **`bandit -c pyproject.toml -r .`**, tanto a execução local do desenvolvedor quanto o pre-commit e o pipeline de CI utilizam exatamente a mesma política.

## Exemplo
```toml
# Exemplo de configuração do Bandit unificada no arquivo pyproject.toml do projeto:
[tool.bandit]
exclude_dirs = ["tests", ".venv", "migrations"]
skips = ["B101"]
```

## Limites e trade-offs
Atenção à regra oficial documentada em `config.html`: é um erro incluir o mesmo ID de teste simultaneamente em `tests` e em `skips`; além disso, quando você usa `pyproject.toml` ou `bandit.yaml`, é obrigatório passar explicitamente **`-c pyproject.toml`** na linha de comando!

## Como verificar
Execute `bandit -c pyproject.toml -r .` e confirme no cabeçalho da saída que os diretórios de teste foram excluídos.

## Conexões
- [[bandit-arquitetura-pycqa-sast-python-ast-nodes-plugins]] — Veja também: PyCQA Bandit: arquitetura do analisador estático de segurança (`SAST`) para Python baseado na árvore sintática (`AST`).
- [[bandit-supressao-granular-nosec-id-especifico-prevencao-cegueira]] — Veja também: Bandit Supressão Segura de Falsos Positivos (`# nosec B602, B607`): por que nunca usar `# nosec` genérico sem ID.

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://bandit.readthedocs.io/en/latest/config.html) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
