---
id: software.seguranca.tranche01.000022
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

# OSV-Scanner `scan source`: varredura de 19+ lockfiles, manifestos SBOM (`CycloneDX`/`SPDX`) e hashes de commits Git (`C/C++`)

## Em uma frase
O subcomando **`osv-scanner scan source`** (padrão ao rodar `osv-scanner scan`) varre diretórios recursivamente (`-r`) ou arquivos explícitos (`-L`), analisando automaticamente lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `go.mod`, `Cargo.lock`, `poetry.lock`, `pom.xml`, `composer.lock`), documentos **SBOM** (CycloneDX e SPDX) e submódulos/diretórios Git de código C/C++ vendorizado.

## Por que importa
Projetos em C e C++ raramente possuem um lockfile central como `package-lock.json`; em vez disso, incluem bibliotecas terceiras via submódulos Git ou diretórios clonados, onde a maioria dos scanners SCA falha em detectar CVEs.

## Como funciona
O OSV-Scanner determina o hash exato do commit Git dos diretórios e submódulos C/C++ e o consulta diretamente contra o ecossistema `GIT` do banco OSV.dev, descobrindo vulnerabilidades em bibliotecas C/C++ sem exigir arquivo de manifesto proprietário!

## Exemplo
```bash
# Escaneando um lockfile específico ou um SBOM CycloneDX existente:
osv-scanner scan source -L package-lock.json
osv-scanner scan source --sbom bom.cdx.json
```

## Limites e trade-offs
A flag `--no-resolve` pode ser usada caso você deseje desabilitar a resolução transitiva de dependências via rede em manifestos como `pom.xml` do Maven.

## Como verificar
Execute `osv-scanner scan source -r . --all-packages --format=json` para listar todo o inventário de pacotes extraído.

## Conexões
- [[osvscanner-arquitetura-osv-dev-osv-scalibr-extracao-matching]] — Veja também: OSV-Scanner V2: arquitetura em duas fases (*Package Extraction* via `OSV-Scalibr` e *Vulnerability Matching* via `OSV.dev`).
- [[osvscanner-scan-image-containers-layer-aware-distros-artifacts]] — Veja também: OSV-Scanner `scan image`: varredura *layer-aware* de imagens de container (pacotes Alpine/Debian/Ubuntu e artefatos Go/Java/Node/Python).

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://google.github.io/osv-scanner/usage/) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
