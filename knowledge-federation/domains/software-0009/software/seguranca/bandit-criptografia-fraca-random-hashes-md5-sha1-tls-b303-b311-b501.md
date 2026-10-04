---
id: software.seguranca.tranche03.000266
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

# Bandit Criptografia, PRNG e TLS (`B303`/`B324` MD5/SHA1, `B311` `random` vs `secrets`, `B501` `verify=False` e `B502` SSL/TLS)

## Em uma frase
O Bandit audita falhas criptográficas e de transporte em Python através dos plugins **`B311` (`random`)**, **`B303` / `B324` (`md5`/`sha1` em `hashlib`)**, **`B304` / `B305` (cifras fracas/modos inseguros)**, **`B501` (`request_with_no_cert_validation`)** e **`B502`–`B504` (`ssl_with_bad_version` / `bad_defaults`)**.

## Por que importa
Dois erros clássicos em backends Python são: 1) usar o módulo `random` (`random.choice`, `random.randint` — baseado no Mersenne Twister previsível) para gerar tokens de recuperação de senha ou códigos OTP; e 2) passar `requests.get(url, verify=False)` ou omitir `timeout=` (`B113` `request_without_timeout`), desativando a validação de certificados TLS ou permitindo travamento indefinido de workers!

## Como funciona
Para geração de segredos e tokens em Python, o Bandit orienta usar o módulo criptográfico **`secrets`** (`secrets.token_urlsafe`, `secrets.SystemRandom`); para `hashlib.md5()` usado apenas para checksum não-criptográfico (ex.: ETag de cache), passe **`usedforsecurity=False`** (Python 3.9+) para informar ao Bandit e ao modo FIPS que o hash não tem fim criptográfico!

## Exemplo
```python
import hashlib
import secrets
import requests

def generate_reset_token_and_fetch(url: str) -> tuple[str, str]:
    token = secrets.token_urlsafe(32)
    cache_key = hashlib.md5(url.encode("utf-8"), usedforsecurity=False).hexdigest()
    resp = requests.get(url, verify=True, timeout=10)
    return token, cache_key + ":" + str(resp.status_code)
```

## Limites e trade-offs
A verificação **`B113` (`request_without_timeout`)** do Bandit é vital para a disponibilidade em produção: chamadas `requests.get/post` sem o parâmetro `timeout=` nunca expiram por padrão se o servidor remoto aceitar o TCP SYN e parar de responder, esgotando todas as threads do Gunicorn/Uvicorn!

## Como verificar
Execute `bandit -t B113,B311,B324,B501 -r .` para encontrar chamadas HTTP sem timeout ou sem verificação TLS.

## Conexões
- [[bandit-desserializacao-insegura-pickle-yaml-load-marshal-b301-b506]] — Veja também: Bandit Desserialização Insegura e XML (`B301` `pickle`, `B506` `yaml.load`, `B314`–`B320` XXE `defusedxml`).
- [[bandit-sql-injection-jinja2-xss-flask-debug-hardcoded-passwords]] — Veja também: Bandit AppSec Web (`B608` SQL Injection, `B701` Jinja2 `autoescape`, `B201` Flask Debug, `B104` Bind `0.0.0.0` e `B105`–`B107` Senhas).

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://bandit.readthedocs.io/en/latest/config.html) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
