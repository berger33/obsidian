---
id: software.seguranca.tranche16.001587
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

# Usando o `pip-audit` com **Repositórios PyPI Privados (`--index-url` / `--extra-index-url`)**, Autenticação `keyring` e Cache HTTP (`--cache-dir`)

## Em uma frase
Em empresas que utilizam um repositório de artefatos privado (**JFrog Artifactory, Sonatype Nexus, AWS CodeArtifact, Google Artifact Registry ou `devpi`**) configurado como espelho do PyPI (`PEP 503 Simple Repository API`), como configurar o `pip-audit` para resolver dependências internas no repositório privado enquanto consulta as vulnerabilidades públicas no **PyPI / OSV.dev**?

## Por que importa
Usando as flags **`--index-url <URL>`** e **`--extra-index-url <URL>`** combinadas com **`-s osv`** (ou `-s pypi`), além do suporte nativo do `pip` a credenciais via `netrc` ou pacote **`keyring`**!

## Como funciona
Por que usar **`-s osv` (`--vulnerability-service osv`)** é especialmente importante quando você usa um `--index-url` corporativo interno? Porque muitos servidores PyPI privados internos (como Nexus/Artifactory) implementam a API simples de download de pacotes (`PEP 503`), mas **não espelham o campo `vulnerabilities` da JSON API proprietária do Warehouse PyPI (`pypi.org`)**; já com `-s osv`, o `pip-audit` resolve os pacotes no seu índice privado e consulta as vulnerabilidades diretamente na API aberta do **OSV.dev**!

## Exemplo
```bash
# Auditar um projeto que usa indice PyPI corporativo privado (--index-url) consultando o servico de vulnerabilidades OSV (-s osv) e cache dedicado
pip-audit \
  -r ./requirements.txt \
  --index-url https://pypi.interno.empresa.br/simple \
  -s osv \
  --cache-dir /var/cache/pip-audit \
  --timeout 30 \
  --strict
```

## Limites e trade-offs
Veja no comando acima as flags **`--cache-dir /var/cache/pip-audit`** e **`--timeout 30`**: por padrão, o `pip-audit` compartilha o cache HTTP do próprio `pip` (`~/.cache/pip`), mas em runners de CI/CD containerizados apontar `--cache-dir` para um volume persistente acelera drasticamente execuções repetidas!

## Como verificar
E lembre-se da boa prática de Supply Chain Security em Python contra ataques de **Dependency Confusion**: evite misturar `--index-url` público com `--extra-index-url` privado sem fixar hashes (`--require-hashes`), preferindo um único grupo virtual no Artifactory/Nexus via `--index-url` com regras de namespace para pacotes internos!

## Conexões
- [[pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes]] — Veja também: Governança de Exceções no `pip-audit`: Ignorando Vulnerabilidades Específicas (**`--ignore-vuln PYSEC-...`**) e Tratamento de Exit Codes em CI/CD.
- [[pip-audit-integracao-pre-commit-github-actions-gh-action-pip-audit]] — Veja também: Automação Shift-Left do `pip-audit`: Hook Oficial **`pre-commit`** e GitHub Action Oficial (**`pypa/gh-action-pip-audit`**).
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.
- [[pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo]] — Referência cruzada direta com pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
