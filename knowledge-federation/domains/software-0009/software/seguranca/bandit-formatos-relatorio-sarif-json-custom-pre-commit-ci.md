---
id: software.seguranca.tranche03.000269
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

# Bandit Formatos de Saída (`json`, `sarif`, `xml`, `html`, `custom`) e Integração com `pre-commit` e GitHub Code Scanning

## Em uma frase
Por meio da flag **`-f` / `--format`** (`csv`, `custom`, `html`, `json`, `screen`, `txt`, `xml`, `yaml` e **`sarif`** via `bandit-sarif-formatter`), o Bandit integra-se diretamente aos hooks locais do **`pre-commit`**, ao **GitHub Code Scanning**, ao **GitLab SAST** e ao **OWASP DefectDojo (`Bandit Scan`)**.

## Por que importa
Quando o desenvolvedor descobre um erro do Bandit apenas 10 minutos depois de abrir o Pull Request no servidor de CI, o ciclo de correção é lento; rodando o Bandit no hook de `pre-commit` (que analisa em menos de 1 segundo apenas os arquivos `.py` modificados no commit), o erro é corrigido antes mesmo do `git push`!

## Como funciona
Conforme documentado na página oficial `config.html`, ao configurar o hook do Bandit no `.pre-commit-config.yaml` lendo o `pyproject.toml`, lembre-se de declarar **`additional_dependencies: ["bandit[toml]"]`** para que o ambiente virtual isolado do `pre-commit` inclua o parser TOML!

## Exemplo
```yaml
# Trecho oficial em .pre-commit-config.yaml (conforme bandit.readthedocs.io/en/latest/config.html):
repos:
  - repo: https://github.com/PyCQA/bandit
    rev: 1.8.3
    hooks:
      - id: bandit
        args: ["-c", "pyproject.toml"]
        additional_dependencies: ["bandit[toml]"]
```

## Limites e trade-offs
Use a flag `-q` (`--quiet` / `--silent`) em pipelines automatizadas para que o Bandit imprima saída apenas quando encontrar problemas ou para gerar relatórios JSON limpos (`bandit -q -r ./src -f json -o bandit-report.json`).

## Como verificar
Valide o relatório JSON gerado com `jq '.results | length' bandit-report.json`.

## Conexões
- [[bandit-filtragem-severidade-confianca-ll-ii-baseline-legado]] — Veja também: Bandit Filtragem por Severidade (`-l`/`-ll`/`-lll`), Confiança (`-i`/`-ii`/`-iii`) e Adoção Incremental com `--baseline` (`-b`).
- [[bandit-escrita-plugins-ast-customizados-entry-points-blacklist]] — Veja também: Bandit Extensibilidade: criação de Plugins AST Customizados (`@test.checks('Call')`) para regras internas de segurança.

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://bandit.readthedocs.io/en/latest/config.html) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
