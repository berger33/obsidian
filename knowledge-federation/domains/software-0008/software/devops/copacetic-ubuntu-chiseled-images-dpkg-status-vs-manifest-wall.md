---
id: software.devops.tranche15.001404
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

# Project Copacetic: aplicação de patches em imagens Ubuntu Chiseled (`dpkg/status` vs `manifest.wall`)

## Em uma frase
O Copacetic suporta dois formatos de imagens distroless Ubuntu Chiseled: imagens sem `apt` que preservam `/var/lib/dpkg/status` e imagens Chisel nativas governadas por `/var/lib/chisel/manifest.wall`.

## Por que importa
Imagens Ubuntu Chiseled removem o gerenciador `apt` e o shell para reduzir drasticamente o tamanho e a superfície de ataque, o que inviabilizava a aplicação tradicional de patches via comandos de gerenciador de pacotes dentro da imagem.

## Como funciona
Para imagens Chiseled que mantêm `/var/lib/dpkg/status`, o Copacetic suporta tanto patching direcionado (`--report`) quanto abrangente. Já para imagens Chisel nativas com `/var/lib/chisel/manifest.wall`, o Copacetic suporta exclusivamente o modo abrangente (rejeitando `--report`) e utiliza `--chisel-release` (ou infere `ubuntu-<VERSION_ID>` de `/etc/os-release`) para recortar novamente todas as fatias (*slices*) instaladas.

## Exemplo
```bash
copa patch \
  -i ghcr.io/org/chiseled-app:1.0.0 \
  --chisel-release ubuntu-24.04 \
  -t 1.0.0-patched
```

## Limites e trade-offs
Em versões como o Trivy `v0.69.3`, o scanner não extrai inventário de pacotes de arquivos `/var/lib/chisel/manifest.wall` nativos; portanto, um resultado de zero vulnerabilidades no Trivy para esse layout não prova por si só que a imagem foi atualizada.

## Como verificar
Verifique os logs de saída do `copa patch` confirmando a validação do `manifest.wall` substituto e do filesystem gerenciado, e execute o smoke test funcional da aplicação antes de promovê-la.

## Conexões
- [[copacetic-comprehensive-patching-atualizacao-completa-sem-relatorio]] — Veja também: Project Copacetic: patching abrangente (Comprehensive Patching) sem relatório de scanner.
- [[copacetic-autodeteccao-instancias-buildkit-docker-buildx-socket]] — Veja também: Project Copacetic: autodeteccão e configuração de endpoints BuildKit (`--addr`).

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://project-copacetic.github.io/copacetic/website/quick-start) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
