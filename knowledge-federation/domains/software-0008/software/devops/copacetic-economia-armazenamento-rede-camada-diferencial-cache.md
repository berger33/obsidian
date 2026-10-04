---
id: software.devops.tranche15.001409
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

# Project Copacetic: redução de custos de armazenamento, tráfego de rede e tempo de resposta a incidentes

## Em uma frase
Por adicionar apenas uma única camada diferencial contendo os binários atualizados do SO, o Copacetic reduz drasticamente o consumo de banda, o espaço em registry e o tempo de pull nos nós Kubernetes em comparação a um rebuild completo da imagem.

## Por que importa
Em um rebuild tradicional de Dockerfile após atualização da imagem base, o hash da primeira camada muda e invalida todas as camadas subsequentes (incluindo camadas pesadas de assets, modelos ou binários), forçando o download integral de centenas de megabytes em todos os nós do cluster.

## Como funciona
Com o `copa`, todas as camadas originais da imagem (`layer 0 .. layer N`) permanecem exatamente com os mesmos digests SHA-256 já cacheados no containerd dos worker nodes. Quando o Deployment é atualizado para a tag `-patched`, o Kubelet baixa apenas a camada de patch de poucos megabytes no topo da pilha.

## Exemplo
```bash
docker inspect docker.io/library/nginx:1.21.6 --format '{{json .RootFS.Layers}}' > base-layers.json
docker inspect docker.io/library/nginx:1.21.6-patched --format '{{json .RootFS.Layers}}' > patched-layers.json
diff -u base-layers.json patched-layers.json || true
```

## Limites e trade-offs
O acúmulo indefinido de múltiplos patches sucessivos sobre a mesma imagem (`-patched-1`, `-patched-2`) adicionaria camadas extras; a recomendação operacional é sempre aplicar o novo patch a partir da imagem original base daquela versão ou incorporar a atualização no próximo ciclo normal de release.

## Como verificar
Compare as listas `.RootFS.Layers` entre a imagem original e a imagem corrigida e confirme que a imagem corrigida contém exatamente os mesmos hashes da original seguidos por um único hash adicional.

## Conexões
- [[copacetic-arquitetura-extensivel-adaptadores-pkgmgr-scanners]] — Veja também: Project Copacetic: arquitetura extensível de adaptadores de gerenciadores de pacotes e scanners.
- [[copacetic-integracao-pipelines-devsecops-assinatura-cosign-kubescape]] — Veja também: Project Copacetic: integração em pipelines DevSecOps com Trivy, Cosign, Notation e Kubescape.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://project-copacetic.github.io/copacetic/website/quick-start) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
