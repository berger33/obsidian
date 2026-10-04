---
id: software.devops.tranche15.001408
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md", "https://project-copacetic.github.io/copacetic/website/quick-start", "https://github.com/project-copacetic/copacetic"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Copacetic: arquitetura extensível de adaptadores de gerenciadores de pacotes e scanners

## Em uma frase
O motor interno do Copacetic desacopla a leitura de relatórios de vulnerabilidades (`pkg/report`) da execução de atualizações de pacotes (`pkg/pkgmgr`), permitindo adicionar suporte a novos scanners e distribuições Linux via interfaces Go modulares.

## Por que importa
Organizações frequentemente combinam scanners distintos (Trivy, Grype, Qualys, Wiz) com distribuições variadas (Debian/Ubuntu `apt`, Alpine `apk`, RHEL/AlmaLinux `dnf`/`rpm`, Azure Linux/Mariner `tdnf`, SUSE `zypper`).

## Como funciona
Quando `copa patch` é invocado, o parser de relatórios normaliza o JSON do scanner em uma lista agnóstica de atualizações; em seguida, o Copacetic inspeciona `/etc/os-release` dentro da imagem alvo para selecionar o adaptador `pkgmgr` apropriado, montando um estado temporário de ferramentas de pacote caso a imagem final seja distroless.

## Exemplo
```bash
copa patch --help
trivy image --vuln-type os -f json -o app-os.json ghcr.io/org/service:v2.1
copa patch -i ghcr.io/org/service:v2.1 -r app-os.json -t v2.1-patched
```

## Limites e trade-offs
Se a imagem base utilizar uma distribuição Linux customizada cujo arquivo `/etc/os-release` foi removido ou adulterado sem manter metadados de pacotes padrão, o Copacetic não conseguirá identificar o adaptador correto.

## Como verificar
Verifique nos logs de execução do `copa patch` a detecção automática do sistema operacional e da versão da imagem alvo.

## Conexões
- [[copacetic-multi-platform-patching-oci-image-index-preservacao]] — Veja também: Project Copacetic: aplicação de patches em imagens multiplataforma e preservação de OCI Image Index.
- [[copacetic-economia-armazenamento-rede-camada-diferencial-cache]] — Veja também: Project Copacetic: redução de custos de armazenamento, tráfego de rede e tempo de resposta a incidentes.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://project-copacetic.github.io/copacetic/website/quick-start) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
