---
id: software.seguranca.tranche03.000261
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
fontes: ["https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst", "https://bandit.readthedocs.io/en/latest/config.html", "https://github.com/PyCQA/bandit"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# PyCQA Bandit: arquitetura do analisador estático de segurança (`SAST`) para Python baseado na árvore sintática (`AST`)

## Em uma frase
Conforme documentado no README oficial (`PyCQA/bandit`, originalmente criado no OpenStack Security Project e mantido pela **PyCQA — Python Code Quality Authority** sob licença Apache 2.0), o **Bandit** é um linter de segurança estático (**SAST**) para Python que analisa cada arquivo `.py`, constrói sua **Abstract Syntax Tree (AST)** usando o módulo nativo `ast` do Python e executa plugins especializados contra os nós da árvore (`Call`, `Import`, `ImportFrom`, `Assign`, `Str`, `Assert`).

## Por que importa
Buscar vulnerabilidades em código Python usando `grep` por palavras como `eval` ou `pickle` gera dezenas de falsos positivos quando essas palavras aparecem dentro de comentários, docstrings ou nomes de variáveis inofensivas.

## Como funciona
Por operar sobre a **AST real do Python** e rastrear imports e aliases (por exemplo, detectando `import subprocess as sp; sp.Popen(..., shell=True)` mesmo quando o módulo foi renomeado com `as sp`), o Bandit identifica com precisão chamadas inseguras, classificando cada achado em duas dimensões independentes: **`Severity` (`LOW`, `MEDIUM`, `HIGH`)** e **`Confidence` (`LOW`, `MEDIUM`, `HIGH`)**!

## Exemplo
```bash
# Instalando o Bandit e executando uma varredura recursiva (-r) sobre o pacote Python da aplicação:
pip install bandit
bandit -r ./src
```

## Limites e trade-offs
Conforme documentado no README oficial, as imagens de container oficiais do Bandit (`ghcr.io/pycqa/bandit/bandit`) são assinadas criptograficamente com **Sigstore Cosign** e podem ser verificadas com `cosign verify` antes da execução no CI/CD.

## Como verificar
Execute `bandit --version` e `bandit -r ./src` verificando o resumo final por severidade e confiança.

## Conexões
- [[bandit-configuracao-pyproject-toml-bandit-yaml-ini-tests-skips]] — Veja também: Bandit Configuração Declarativa (`pyproject.toml`, `bandit.yaml` e `.bandit`): controle de `exclude_dirs`, `tests` e `skips`.

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://bandit.readthedocs.io/en/latest/config.html) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
