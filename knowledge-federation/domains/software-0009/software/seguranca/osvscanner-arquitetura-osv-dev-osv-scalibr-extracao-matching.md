---
id: software.seguranca.tranche01.000021
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
fontes: ["https://raw.githubusercontent.com/google/osv-scanner/main/README.md", "https://google.github.io/osv-scanner/usage/", "https://github.com/google/osv-scanner"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OSV-Scanner V2: arquitetura em duas fases (*Package Extraction* via `OSV-Scalibr` e *Vulnerability Matching* via `OSV.dev`)

## Em uma frase
O **OSV-Scanner** (mantido pelo Google sob licença Apache 2.0 e publicado com proveniência **SLSA Nível 3**) é a interface oficial de linha de comando para o banco de dados aberto de vulnerabilidades **[OSV.dev](https://osv.dev/)** e para a biblioteca de extração de inventário **[OSV-Scalibr](https://github.com/google/osv-scalibr)**.

## Por que importa
Scanners proprietários de composição de software (SCA) frequentemente dependem de bancos fechados com mapeamentos imprecisos de CPEs que geram falsos positivos entre pacotes de ecossistemas diferentes.

## Como funciona
Conforme a documentação oficial do OSV-Scanner V2, a ferramenta opera em um processo de duas etapas: 1) **Package Extraction** (usando o motor `OSV-Scalibr` para extrair pacotes de 11+ linguagens, 19+ formatos de lockfile, imagens de container e pacotes de SO Linux); e 2) **Vulnerability Matching** (consultando o banco aberto e autoritativo `OSV.dev`, que agrega GitHub Security Advisories, RustSec, PyPA, Go VulnDB, Ubuntu/Debian/Alpine Security Notices com precisão exata de commits e semver).

## Exemplo
```bash
# Instalando o OSV-Scanner V2 via Go ou binário oficial e escaneando recursivamente um repositório:
osv-scanner scan source -r ./meu-projeto
```

## Limites e trade-offs
Por usar o schema aberto **Open Source Vulnerability (OSV)**, cada aviso mapeia exatamente o ecossistema (`npm`, `PyPI`, `Go`, `Maven`, `crates.io`, `GIT`) e os intervalos de versão/commits introduzidos e corrigidos.

## Como verificar
Execute `osv-scanner --version` e `osv-scanner scan source -r .` para auditar as dependências do projeto.

## Conexões
- [[osvscanner-scan-source-lockfiles-sbom-cyclonedx-spdx-git-commits]] — Veja também: OSV-Scanner `scan source`: varredura de 19+ lockfiles, manifestos SBOM (`CycloneDX`/`SPDX`) e hashes de commits Git (`C/C++`).

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
