---
id: software.seguranca.tranche03.000268
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

# Bandit Filtragem por Severidade (`-l`/`-ll`/`-lll`), Confiança (`-i`/`-ii`/`-iii`) e Adoção Incremental com `--baseline` (`-b`)

## Em uma frase
O Bandit permite calibrar o limiar de falha da pipeline de CI/CD repetindo as flags **`-l` (`--level`)** para Severidade (`-l` = ALL, **`-ll`** = `MEDIUM` e `HIGH`, **`-lll`** = apenas `HIGH`) e **`-i` (`--confidence`)** para Confiança (`-i` = ALL, **`-ii`** = `MEDIUM` e `HIGH`, **`-iii`** = apenas `HIGH`), além de suportar um arquivo de linha de base (**`-b` / `--baseline baseline.json`**).

## Por que importa
Ao introduzir o Bandit em um monorepo Python legado que já possui 200 avisos históricos de severidade baixa/média, quebrar a pipeline em todos os 200 itens no primeiro dia trava as entregas da equipe.

## Como funciona
Você pode adotar o Bandit sem atrito em duas frentes: 1) bloquear o build imediatamente para achados de **Média/Alta Severidade e Média/Alta Confiança (`bandit -r . -ll -ii`)**; ou 2) gerar um snapshot JSON do legado (`bandit -r . -f json -o bandit-baseline.json`) e rodar **`bandit -r . -b bandit-baseline.json`** no CI para falhar exclusivamente em novos problemas introduzidos no Pull Request!

## Exemplo
```bash
# 1. Executando o Bandit exigindo Severidade >= MEDIUM (-ll) e Confiança >= MEDIUM (-ii):
bandit -c pyproject.toml -r ./src -ll -ii

# 2. Gerando um arquivo de baseline JSON e comparando novos commits contra a baseline:
bandit -c pyproject.toml -r ./src -f json -o .bandit-baseline.json || true
bandit -c pyproject.toml -r ./src -b .bandit-baseline.json
```

## Limites e trade-offs
Atenção a não confundir `-i` minúsculo sem repetição quando misturado com `--ignore-nosec`: para maior clareza em scripts de CI/CD, você também pode combinar `-ll` com `--confidence-level=medium` ou `-ii`.

## Como verificar
Teste executar `bandit -r ./src -ll -ii` e verifique no cabeçalho os filtros `Severity` e `Confidence` ativos.

## Conexões
- [[bandit-sql-injection-jinja2-xss-flask-debug-hardcoded-passwords]] — Veja também: Bandit AppSec Web (`B608` SQL Injection, `B701` Jinja2 `autoescape`, `B201` Flask Debug, `B104` Bind `0.0.0.0` e `B105`–`B107` Senhas).
- [[bandit-formatos-relatorio-sarif-json-custom-pre-commit-ci]] — Veja também: Bandit Formatos de Saída (`json`, `sarif`, `xml`, `html`, `custom`) e Integração com `pre-commit` e GitHub Code Scanning.

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://bandit.readthedocs.io/en/latest/config.html) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
