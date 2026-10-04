---
id: software.seguranca.tranche01.000029
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://google.github.io/osv-scanner/usage/", "https://raw.githubusercontent.com/google/osv-scanner/main/README.md", "https://github.com/google/osv-scanner"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OSV-Scanner Formatos de Saída (`--format`) e Integração `pre-commit` / GitHub Actions (`sarif`, `cyclonedx-1-5`, `gh-annotations`)

## Em uma frase
O OSV-Scanner suporta múltiplos formatos de saída via **`--format`** — incluindo `table`, `vertical`, `json`, `markdown`, **`sarif`**, **`gh-annotations`**, **`html`**, **`cyclonedx-1-4`** e **`cyclonedx-1-5`** — além de hooks oficiais para **`pre-commit`** (`osv-scanner` e `osv-scanner-docker`) e GitHub Actions reutilizáveis.

## Por que importa
A mesma ferramenta pode atuar simultaneamente como **gerador de SBOM CycloneDX** (`--format cyclonedx-1-5 --all-packages`), como anotador de Pull Requests no GitHub (`--format gh-annotations`) e como exportador SARIF para o painel de segurança.

## Como funciona
No `.pre-commit-config.yaml`, basta referenciar `repo: https://github.com/google/osv-scanner/` com `id: osv-scanner` para que qualquer alteração em `go.mod`, `package-lock.json` ou `requirements.txt` seja auditada localmente antes do commit.

## Exemplo
```bash
# Gerando um SBOM CycloneDX 1.5 completo (incluindo pacotes sem vulnerabilidades) com o OSV-Scanner:
osv-scanner scan source --all-packages --format cyclonedx-1-5 --output-file sbom.cdx.json .

# Gerando relatório SARIF para integração com plataformas DevSecOps:
osv-scanner scan source --format sarif --output-file osv-results.sarif .
```

## Limites e trade-offs
Para gerar um SBOM completo em CycloneDX ou JSON contendo todos os pacotes do projeto (e não apenas os pacotes vulneráveis), lembre-se de passar **`--all-packages`** junto com `--format`.

## Como verificar
Verifique o arquivo `sbom.cdx.json` gerado com `jq '.components | length' sbom.cdx.json`.

## Conexões
- [[osvscanner-configuracao-osv-scanner-toml-ignoredvulns-packageoverrides]] — Veja também: OSV-Scanner `osv-scanner.toml`: supressão auditável (`IgnoredVulns` com `ignoreUntil`) e sobrescrita (`PackageOverrides`).
- [[osvscanner-extensibilidade-osv-scalibr-plugins-arquitetura-v2]] — Veja também: OSV-Scanner e `OSV-Scalibr`: arquitetura modular de extratores e detectores na versão V2.

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://google.github.io/osv-scanner/usage/) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
