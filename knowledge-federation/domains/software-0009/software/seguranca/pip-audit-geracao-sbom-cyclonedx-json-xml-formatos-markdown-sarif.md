---
id: software.seguranca.tranche16.001585
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

# Geração Nativa de **SBOM CycloneDX (`-f cyclonedx-json` / `cyclonedx-xml`)**, Relatórios **Markdown (`-f markdown`)** e **JSON** no `pip-audit`

## Em uma frase
Você sabia que o `pip-audit` não é apenas um scanner de vulnerabilidades, mas também um **Gerador Oficial de SBOM (*Software Bill of Materials*) no padrão `CycloneDX` (JSON e XML)** para projetos Python?

## Por que importa
Conforme documentado na opção **`-f FORMAT` (`--format`)** do `README.md` oficial, o `pip-audit` suporta 5 formatos nativos de saída: **`columns`** (padrão para terminal), **`json`** (com `--desc` e `--aliases` ativados automaticamente por padrão no modo `auto`!), **`markdown`** (pronto para colar diretamente em comentários de Pull Request no GitHub/GitLab!), **`cyclonedx-json`** e **`cyclonedx-xml`**!

## Como funciona
Assim, em um único comando durante o build da sua aplicação Python, o `pip-audit` audita as vulnerabilidades **E** emite o SBOM `CycloneDX` completo contendo todos os pacotes Python e as vulnerabilidades associadas para ingestão direta no **OWASP Dependency-Track**!

## Exemplo
```bash
# Emitir um SBOM CycloneDX JSON completo e um relatorio em tabela Markdown para comentario de Pull Request usando o pip-audit
pip-audit -f cyclonedx-json -o ./sbom-python-cyclonedx.json
pip-audit -f markdown --aliases --desc -o ./relatorio-pr.md
```

## Limites e trade-offs
Veja na tabela de *Environment variables* do `README.md` que todas essas opções de formatação também podem ser controladas globalmente no seu runner de CI/CD via variáveis de ambiente sem alterar scripts de build: **`PIP_AUDIT_FORMAT=markdown`**, **`PIP_AUDIT_VULNERABILITY_SERVICE=osv`**, **`PIP_AUDIT_DESC=on`**, **`PIP_AUDIT_PROGRESS_SPINNER=off`** (ideal para logs de CI limpos!) e **`PIP_AUDIT_OUTPUT=/tmp/audit.json`**!

## Como verificar
Sempre defina **`PIP_AUDIT_PROGRESS_SPINNER=off`** (ou `--progress-spinner off`) em pipelines de CI/CD automatizados para evitar que os caracteres de animação do spinner poluam os logs de console do GitHub Actions/GitLab CI.

## Conexões
- [[pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo]] — Veja também: O Modelo de Segurança do `pip-audit` (**Security Model**): Por Que Auditar `requirements.txt` Não-Pinados Pode Executar `setup.py` e Como Prevenir com `--require-hashes`.
- [[pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes]] — Veja também: Governança de Exceções no `pip-audit`: Ignorando Vulnerabilidades Específicas (**`--ignore-vuln PYSEC-...`**) e Tratamento de Exit Codes em CI/CD.
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
