---
id: software.seguranca.tranche01.000030
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

# OSV-Scanner e `OSV-Scalibr`: arquitetura modular de extratores e detectores na versão V2

## Em uma frase
Na versão V2, o OSV-Scanner passou a utilizar por baixo dos panos a biblioteca extensível **[OSV-Scalibr](https://github.com/google/osv-scalibr)** do Google como motor unificado de extração de inventário de software (os pacotes `extractor` de filesystem/containers) e detecção de segurança.

## Por que importa
Antes da unificação com o `OSV-Scalibr`, manter parsers separados para lockfiles de código-fonte, bancos de pacotes de sistemas operacionais Linux (`/var/lib/dpkg/status`, `/lib/apk/db/installed`) e binários compilados duplicava esforços de engenharia.

## Como funciona
Graças ao `OSV-Scalibr`, é possível selecionar ou estender plugins específicos de extração — desde lockfiles padrão de linguagens até inspeção de binários Go compilados (lendo a tabela `buildinfo` embutida pelo compilador Go dentro do executável) e metadados de pacotes Java/Python dentro de imagens de container.

## Exemplo
```bash
# Escaneando um diretório que contém binários compilados ou múltiplos ecossistemas com o motor OSV-Scalibr:
osv-scanner scan source --verbosity info -r ./dist
```

## Limites e trade-offs
Ao compilar binários Go em produção sem símbolos de buildinfo (`-ldflags="-buildid="`), considere manter os metadados de módulos do Go para que o extrator do `OSV-Scalibr` possa auditar o binário diretamente na imagem de container final.

## Como verificar
Inspecione os pacotes extraídos em cada diretório ou imagem com `--verbosity info`.

## Conexões
- [[osvscanner-formatos-saida-sarif-cyclonedx-html-gh-annotations-pre-commit]] — Veja também: OSV-Scanner Formatos de Saída (`--format`) e Integração `pre-commit` / GitHub Actions (`sarif`, `cyclonedx-1-5`, `gh-annotations`).

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
