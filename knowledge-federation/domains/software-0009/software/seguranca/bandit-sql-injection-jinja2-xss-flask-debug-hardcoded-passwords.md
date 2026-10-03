---
id: software.seguranca.tranche03.000267
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

# Bandit AppSec Web (`B608` SQL Injection, `B701` Jinja2 `autoescape`, `B201` Flask Debug, `B104` Bind `0.0.0.0` e `B105`–`B107` Senhas)

## Em uma frase
Para aplicações web e APIs Python (Django, Flask, FastAPI, SQLAlchemy), o Bandit inclui detectores dedicados para **Injeção SQL (`B608` `hardcoded_sql_expressions`)**, **XSS em templates Jinja2 (`B701` `jinja2_autoescape_false`)**, **Flask Debug em produção (`B201` `flask_debug_true` — que expõe o debugger interativo Werkzeug com execução de código)** e **senhas hardcoded (`B105`, `B106`, `B107`)**.

## Por que importa
Com a adoção de f-strings (`f"SELECT * FROM users WHERE username = '{user}'"`) no Python 3, tornou-se muito fácil construir inadvertidamente uma query SQL vulnerável via interpolação de string em vez de usar parâmetros vinculados (*bind parameters*) do driver de banco.

## Como funciona
O plugin `B608` inspeciona nós de formatação de strings (`%`, `.format()`, `JoinedStr` / f-strings e concatenação `+`) que se parecem com instruções `SELECT`, `INSERT`, `UPDATE` ou `DELETE`, alertando sempre que variáveis são interpoladas diretamente na query.

## Exemplo
```python
import jinja2

# SEGURO contra XSS (B701): habilita explicitamente autoescape=True no ambiente Jinja2:
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"),
    autoescape=jinja2.select_autoescape(["html", "htm", "xml"])
)
```

## Limites e trade-offs
Em ambientes Jinja2 criados manualmente no código (`jinja2.Environment(...)`), o padrão histórico do Jinja2 é `autoescape=False`! Sempre passe `autoescape=True` ou `select_autoescape()` para satisfazer o check `B701`.

## Como verificar
Rode `bandit -t B201,B608,B701 -r .` sobre suas rotas web e camada de persistência.

## Conexões
- [[bandit-criptografia-fraca-random-hashes-md5-sha1-tls-b303-b311-b501]] — Veja também: Bandit Criptografia, PRNG e TLS (`B303`/`B324` MD5/SHA1, `B311` `random` vs `secrets`, `B501` `verify=False` e `B502` SSL/TLS).
- [[bandit-filtragem-severidade-confianca-ll-ii-baseline-legado]] — Veja também: Bandit Filtragem por Severidade (`-l`/`-ll`/`-lll`), Confiança (`-i`/`-ii`/`-iii`) e Adoção Incremental com `--baseline` (`-b`).

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://bandit.readthedocs.io/en/latest/config.html) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
