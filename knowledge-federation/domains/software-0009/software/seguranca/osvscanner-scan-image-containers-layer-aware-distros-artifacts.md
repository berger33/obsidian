---
id: software.seguranca.tranche01.000023
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

# OSV-Scanner `scan image`: varredura *layer-aware* de imagens de container (pacotes Alpine/Debian/Ubuntu e artefatos Go/Java/Node/Python)

## Em uma frase
O subcomando **`osv-scanner scan image`** realiza inspeção profunda e consciente de camadas (*layer-aware*) em imagens de container (do daemon Docker local, registries remotos ou arquivos `.tar` OCI), identificando tanto pacotes do sistema operacional base (**Alpine**, **Debian**, **Ubuntu**) quanto artefatos compilados de linguagem (**binários Go**, **JARs Java**, **`node_modules` Node.js** e **pacotes Python**).

## Por que importa
Saber apenas que uma vulnerabilidade existe dentro de uma imagem de container de 800 MB não diz ao engenheiro se ela veio da imagem base (`FROM ubuntu:24.04`), de um `apt-get install` ou de um binário Go copiado em um estágio multi-stage.

## Como funciona
O relatório do `osv-scanner scan image` correlaciona cada pacote vulnerável à camada exata (`Layer`) do Dockerfile que o introduziu, diferenciando vulnerabilidades da imagem base das dependências da aplicação.

## Exemplo
```bash
# Escaneando uma imagem de container e abrindo o relatório interativo HTML localmente na porta 8000:
osv-scanner scan image minha-app:1.2.0 --serve

# Escaneando um arquivo de imagem OCI exportado em .tar gerando saída JSON:
osv-scanner scan image --archive ./app-image.tar --format json --output-file image-vulns.json
```

## Limites e trade-offs
A flag **`--serve`** gera o relatório visual em HTML (com filtro por camada, severidade e pacote) e sobe um servidor local na porta `8000` para inspeção imediata no navegador.

## Como verificar
Execute `osv-scanner scan image alpine:3.19` para verificar a extração de pacotes `apk` e camadas da imagem.

## Conexões
- [[osvscanner-scan-source-lockfiles-sbom-cyclonedx-spdx-git-commits]] — Veja também: OSV-Scanner `scan source`: varredura de 19+ lockfiles, manifestos SBOM (`CycloneDX`/`SPDX`) e hashes de commits Git (`C/C++`).
- [[osvscanner-call-analysis-reachability-go-rust-reducao-falsos-positivos]] — Veja também: OSV-Scanner Call Analysis (*Reachability*): análise de grafo de chamadas para verificar se a função vulnerável é realmente invocada.

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
