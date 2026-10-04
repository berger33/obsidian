---
id: software.devops.tranche15.001405
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
fontes: ["https://project-copacetic.github.io/copacetic/website/quick-start", "https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md", "https://github.com/project-copacetic/copacetic"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Copacetic: autodeteccão e configuração de endpoints BuildKit (`--addr`)

## Em uma frase
O `copa` depende de uma instância do BuildKit para resolver e aplicar a camada de patch, autodetectando backends disponíveis na máquina ou conectando-se a um endereço customizado via `--addr`.

## Por que importa
Em estações de trabalho, servidores de CI ou jobs Kubernetes, o BuildKit pode estar embutido no Docker Engine, exposto via builder `docker buildx`, rodando em Podman ou em um daemon `buildkitd` dedicado sem privilégios.

## Como funciona
Quando `--addr` não é informado, o Copacetic tenta conectar-se automaticamente na seguinte ordem de precedência: 1) BuildKit embutido do Docker (requer Docker v24.0+ com containerd image store habilitado para imagens locais); 2) builder ativo do `docker buildx` (`docker buildx create --use`); 3) socket padrão do daemon BuildKit em `/run/buildkit/buildkitd.sock`.

## Exemplo
```bash
copa patch --addr buildx://copa-builder -i docker.io/library/nginx:1.21.6 -r nginx-report.json
```

## Limites e trade-offs
Ao tentar aplicar patches em imagens que existem apenas localmente no Docker sem o *containerd image store* habilitado no Docker Engine v24+, o BuildKit embutido não enxerga a imagem local e falha no pull.

## Como verificar
Execute `docker buildx ls` ou verifique a existência de `/run/buildkit/buildkitd.sock` antes de rodar `copa patch` em pipelines de CI/CD.

## Conexões
- [[copacetic-ubuntu-chiseled-images-dpkg-status-vs-manifest-wall]] — Veja também: Project Copacetic: aplicação de patches em imagens Ubuntu Chiseled (`dpkg/status` vs `manifest.wall`).
- [[copacetic-compressao-camadas-patch-uncompressed-force-compression]] — Veja também: Project Copacetic: controle de compressão da camada de patch (`--compression` e `--force-compression`).

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://project-copacetic.github.io/copacetic/website/quick-start) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
