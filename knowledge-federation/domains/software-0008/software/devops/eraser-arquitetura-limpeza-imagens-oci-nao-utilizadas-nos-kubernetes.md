---
id: software.devops.tranche15.001491
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
fontes: ["https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md", "https://eraser-dev.github.io/eraser/docs/quick-start", "https://github.com/eraser-dev/eraser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CNCF Eraser: arquitetura de limpeza automatizada de imagens não executadas e vulneráveis nos nós Kubernetes

## Em uma frase
O Eraser (projeto CNCF Sandbox) é um operador Kubernetes que identifica e remove imagens de container que não estão em execução (*non-running images*) — especialmente imagens antigas ou com vulnerabilidades conhecidas — do cache de todos os nós do cluster.

## Por que importa
O Garbage Collector nativo do Kubelet só apaga imagens em cache quando o disco do nó atinge um limite alto de ocupação (como 85%); até lá, imagens antigas com CVEs críticos permanecem armazenadas no `/var/lib/containerd` dos nós, gerando alertas contínuos em scanners de segurança de nós e consumindo espaço.

## Como funciona
O `eraser-controller-manager` agenda periodicamente (ou sob demanda via `ImageJob`/`ImageList`) um Pod efêmero por nó no namespace `eraser-system`. Cada Pod executa até três containers coordenados (`collector`, `scanner` e `remover`) diretamente contra o socket CRI do nó, remove as imagens não utilizadas que reprovarem nos critérios e encerra (`Completed`), sendo limpo automaticamente em seguida.

## Exemplo
```bash
kubectl get pods -n eraser-system
kubectl get imagejobs,imagelists -A
```

## Limites e trade-offs
O Eraser nunca remove imagens que estejam associadas a containers em execução no nó naquele momento, protegendo as cargas de trabalho ativas contra remoção acidental de camadas em uso.

## Como verificar
Liste as imagens presentes no `containerd` do nó (`ctr -n k8s.io images list` ou `crictl images`) antes e depois da execução dos Pods do Eraser para confirmar a remoção.

## Conexões
- [[eraser-pipeline-tres-containers-collector-scanner-remover-pod]] — Veja também: Eraser: pipeline de três estágios por nó (`collector`, `scanner` e `remover`) nos Pods de limpeza.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://eraser-dev.github.io/eraser/docs/quick-start) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
