---
id: software.seguranca.tranche16.001586
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

# Governança de Exceções no `pip-audit`: Ignorando Vulnerabilidades Específicas (**`--ignore-vuln PYSEC-...`**) e Tratamento de Exit Codes em CI/CD

## Em uma frase
O que fazer quando o `pip-audit` encontra uma vulnerabilidade (ex.: `PYSEC-2026-123` ou `GHSA-xxxx-yyyy-zzzz`) em uma dependência transitiva que ainda não possui versão corrigida publicada, mas a sua equipe de AppSec já analisou o código-fonte, verificou o campo `ecosystem_specific.imports` do `pypa/advisory-database` e confirmou que a função vulnerável **não é importada nem usada pela sua aplicação**?

## Por que importa
Como destaca a seção *Exit codes* do `README.md` oficial: o código de saída `1` do `pip-audit` não pode ser desligado globalmente se houver vulnerabilidades abertas.

## Como funciona
A maneira oficial e auditável de registrar uma exceção aprovada é passar **`--ignore-vuln <ID>`** (que pode ser repetida múltiplas vezes para cada ID revisado)!

## Exemplo
```bash
# Executar o pip-audit ignorando explicitamente uma vulnerabilidade triada como nao-exploravel (--ignore-vuln) e salvando o JSON auditado
pip-audit \
  -r ./requirements.txt \
  --strict \
  --ignore-vuln PYSEC-2024-9999 \
  --aliases \
  -f json -o ./pip-audit-result.json
```

## Limites e trade-offs
Atenção a um detalhe muito importante ao usar **`--ignore-vuln <ID>`**: o `pip-audit` compara o ID passado em `--ignore-vuln` tanto contra o ID primário (ex.: `PYSEC-2024-9999`) quanto contra seus **Aliases (`CVE-*` e `GHSA-*`)** se a resolução de aliases estiver habilitada!

## Como verificar
E quando você usa `--ignore-vuln` combinado com `--format json`, a vulnerabilidade ignorada **não desaparece silenciosamente sem deixar rastro** — ela pode ser auditada no controle de versão onde o comando `--ignore-vuln` foi declarado (sempre acompanhado de um comentário com o número do ticket de risco e a data de reavaliação)!

## Conexões
- [[pip-audit-geracao-sbom-cyclonedx-json-xml-formatos-markdown-sarif]] — Veja também: Geração Nativa de **SBOM CycloneDX (`-f cyclonedx-json` / `cyclonedx-xml`)**, Relatórios **Markdown (`-f markdown`)** e **JSON** no `pip-audit`.
- [[pip-audit-indices-privados-index-url-extra-index-url-cache-offline]] — Veja também: Usando o `pip-audit` com **Repositórios PyPI Privados (`--index-url` / `--extra-index-url`)**, Autenticação `keyring` e Cache HTTP (`--cache-dir`).
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.
- [[pip-audit-anatomia-pypa-advisory-database-osv-schema-imports]] — Referência cruzada direta com pip-audit-anatomia-pypa-advisory-database-osv-schema-imports.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
