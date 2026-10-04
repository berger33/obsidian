---
id: software.seguranca.tranche01.000028
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

# OSV-Scanner `osv-scanner.toml`: supressão auditável (`IgnoredVulns` com `ignoreUntil`) e sobrescrita (`PackageOverrides`)

## Em uma frase
O arquivo de configuração **`osv-scanner.toml`** (ou especificado via `--config`) permite gerenciar exceções de vulnerabilidades (`IgnoredVulns`) e sobrescritas de pacotes/licenças (`PackageOverrides`) com **data de expiração obrigatória (`ignoreUntil`)** e justificativa obrigatória (`reason`).

## Por que importa
Quando uma CVE é confirmada como não explorável no contexto da aplicação, silenciá-la para sempre sem data de revisão faz a exceção ser esquecida; exigir `ignoreUntil = 2026-12-31` força a reavaliação automática quando o prazo vence.

## Como funciona
Dentro do `osv-scanner.toml`, cada entrada `IgnoredVulns` declara o `id` da vulnerabilidade (ex.: `"GHSA-..."` ou `"CVE-..."`), `ignoreUntil` (data YYYY-MM-DD) e `reason`. Já `PackageOverrides` permite ignorar um pacote de teste ou sobrescrever a licença detectada (`license.override = ["MIT"]`) quando os metadados originais do pacote estão incompletos.

## Exemplo
```toml
[IgnoredVulns.ghsa_xxxx]
id = "GHSA-xxxx-yyyy-zzzz"
ignoreUntil = 2026-12-31
reason = "Função vulnerável só existe no modo servidor HTTP, que não é habilitado neste binário CLI."

[PackageOverrides.internal_test_helper]
name = "internal-test-helper"
ecosystem = "npm"
ignore = true
reason = "Pacote usado exclusivamente em mocks locais."
```

## Limites e trade-offs
Conforme documentado em `Usage`, a diretiva `PackageOverrides` com `ignore = true` tem precedência inclusive sobre a flag `--all-packages`.

## Como verificar
Execute `osv-scanner scan source --config ./osv-scanner.toml .` para validar a aplicação das regras de exceção.

## Conexões
- [[osvscanner-offline-scanning-download-offline-databases-air-gapped]] — Veja também: OSV-Scanner Modo Offline (`--offline-vulnerabilities` e `--download-offline-databases`): operação em redes isoladas e *air-gapped*.
- [[osvscanner-formatos-saida-sarif-cyclonedx-html-gh-annotations-pre-commit]] — Veja também: OSV-Scanner Formatos de Saída (`--format`) e Integração `pre-commit` / GitHub Actions (`sarif`, `cyclonedx-1-5`, `gh-annotations`).

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://google.github.io/osv-scanner/usage/) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
