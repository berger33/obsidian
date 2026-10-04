---
id: software.seguranca.tranche16.001589
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

# Anatomia da Base **`pypa/advisory-database`**: Formato **OpenSSF OSV YAML (`PYSEC-*`)**, Validação `check-jsonschema` e **`ecosystem_specific.imports`**

## Em uma frase
Como funciona por dentro o repositório oficial **`pypa/advisory-database` (`Python Packaging Advisory Database`)** que alimenta tanto o `pip-audit`, quanto a **PyPI JSON API** e o **Google OSV.dev**, e como ele ajuda a reduzir falsos positivos mapeando exatamente quais símbolos Python são afetados?

## Por que importa
Conforme documentado no `README.md` do `pypa/advisory-database`, todos os avisos vivem no diretório `vulns/<pacote>/PYSEC-YYYY-NNN.yaml` seguindo estritamente o **OpenSSF OSV Schema (`ossf/osv-schema`)**!

## Como funciona
E o recurso mais avançado documentado na seção *Marking specific attributes as vulnerable* é o bloco **`ecosystem_specific.imports`**: cada entrada OSV pode declarar o array JSON/YAML `imports` contendo os **`modules`** (ex.: `["django.db.models", "django.db.models.fields.json"]` ou `["PIL"]`) e o **`attribute`** exato (ex.: `"JSONField"` ou `"ImageFont"`) onde reside a vulnerabilidade!

## Exemplo
```yaml
# Exemplo da estrutura ecosystem_specific.imports em um aviso PYSEC do pypa/advisory-database identificando o modulo e atributo vulneravel
id: PYSEC-2026-0001
affected:
  - package:
      name: pillow
      ecosystem: PyPI
    ranges:
      - type: ECOSYSTEM
        events:
          - introduced: "0"
          - fixed: "10.3.0"
    ecosystem_specific:
      imports:
        - attribute: ImageFont
          modules:
            - PIL
```

## Limites e trade-offs
Veja como validar estruturalmente qualquer arquivo YAML de advisory da base `pypa/advisory-database` usando o comando oficial documentado no `README.md`: **`pipx run check-jsonschema --schemafile https://raw.githubusercontent.com/ossf/osv-schema/main/validation/schema.json <CAMINHO_YAML>`**!

## Como verificar
Quando a sua equipe descobre ou analisa uma CVE em um pacote Python, verificar o bloco `ecosystem_specific.imports` no `pypa/advisory-database` (ou rodar um `grep -rn "ImageFont"` no código da sua aplicação) permite saber em segundos se o símbolo vulnerável é realmente importado pelo seu sistema!

## Conexões
- [[pip-audit-integracao-pre-commit-github-actions-gh-action-pip-audit]] — Veja também: Automação Shift-Left do `pip-audit`: Hook Oficial **`pre-commit`** e GitHub Action Oficial (**`pypa/gh-action-pip-audit`**).
- [[pip-audit-auditoria-containers-python-multistage-path-site-packages]] — Veja também: Auditando **Containers Python Distroless e Multi-Stage Builds** com `pip-audit`: Usando a Flag **`--path` (`site-packages`)** sem Instalar o `pip-audit` na Imagem Final.
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.
- [[pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes]] — Referência cruzada direta com pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
