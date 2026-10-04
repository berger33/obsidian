---
id: software.devops.tranche15.001498
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

# Eraser vs Kubelet Image Garbage Collection: diferenças entre limpeza por pressão de disco e limpeza orientada a CVEs

## Em uma frase
Enquanto o coletor de lixo de imagens do Kubelet (`imageGCHighThresholdPercent` / `imageGCLowThresholdPercent`) é acionado exclusivamente quando o disco do nó fica cheio e apaga imagens apenas por idade de último uso (LRU), o Eraser limpa proativamente imagens ociosas em janelas programadas e com base em vulnerabilidades de segurança.

## Por que importa
Em nós modernos com discos de 200 GiB ou 500 GiB, o limite de 85% de disco do Kubelet pode levar meses para ser atingido; durante todo esse período, imagens antigas com CVEs críticos permanecem nos nós e acionam falsos positivos em auditorias de conformidade.

## Como funciona
O Eraser complementa o Kubelet GC adicionando inteligência de segurança (via container `scanner` com Trivy) e controle declarativo via CRDs (`ImageList` e `ImageJob`), garantindo que imagens obsoletas e vulneráveis sejam eliminadas mesmo quando o disco está com apenas 10% de uso.

## Exemplo
```bash
kubectl logs -n eraser-system deployment/eraser-controller-manager --tail=30
```

## Limites e trade-offs
O Eraser não substitui a necessidade de manter os thresholds do Kubelet GC configurados como rede de segurança contra enchimento súbito de disco entre dois ciclos de `repeatInterval`.

## Como verificar
Compare a saída de scanners de conformidade de nós antes e depois da implantação do Eraser para medir a redução de alertas de CVEs em imagens inativas.

## Conexões
- [[eraser-demo-daemonset-alpine-validacao-containerd-kind-ctr]] — Veja também: Eraser: fluxo de validação prática com DaemonSet de teste e inspeção de `containerd` via `ctr -n k8s.io`.
- [[eraser-crd-imagejob-execucao-efemera-node-selectors-limpeza]] — Veja também: Eraser: coordenação distribuída de pods de limpeza por nó via recurso `ImageJob`.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://eraser-dev.github.io/eraser/docs/quick-start) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
