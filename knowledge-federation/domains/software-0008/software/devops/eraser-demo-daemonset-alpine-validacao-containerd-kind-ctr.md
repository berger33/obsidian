---
id: software.devops.tranche15.001497
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
fontes: ["https://eraser-dev.github.io/eraser/docs/quick-start", "https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md", "https://github.com/eraser-dev/eraser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Eraser: fluxo de validação prática com DaemonSet de teste e inspeção de `containerd` via `ctr -n k8s.io`

## Em uma frase
O guia oficial de Quick Start do Eraser valida o funcionamento do operador implantando e removendo um `DaemonSet` com uma imagem vulnerável (`docker.io/library/alpine:3.7.3`) e inspecionando o namespace `k8s.io` do `containerd` nos worker nodes.

## Por que importa
Como um `DaemonSet` força o download da imagem em todos os worker nodes do cluster, apagá-lo em seguida reproduz exatamente o cenário real de "lixo residual de imagens vulneráveis" que fica retido indefinidamente no cache dos nós.

## Como funciona
Após executar `kubectl delete daemonset alpine`, o comando `docker exec kind-worker ctr -n k8s.io images list | grep alpine` comprova que o manifesto e os blobs de `alpine:3.7.3` continuam no nó; assim que os Pods `eraser-kind-*` completam (`0/3 Completed`), a mesma consulta retorna vazio.

## Exemplo
```bash
docker exec kind-worker ctr -n k8s.io images list | grep alpine || echo "Imagem removida com sucesso"
kubectl get pods -n eraser-system
```

## Limites e trade-offs
Ao inspecionar imagens diretamente no `containerd` de um nó Kubernetes com a ferramenta `ctr`, lembre-se sempre de passar a flag `-n k8s.io`, pois todas as imagens gerenciadas pelo Kubelet CRI ficam isoladas nesse namespace.

## Como verificar
Repita o comando `ctr -n k8s.io images list | grep alpine` em todos os nós (`kind-worker`, `kind-worker2`) após o término do job do Eraser e confirme que nenhuma referência restou.

## Conexões
- [[eraser-exclusao-imagens-protegidas-excluded-configmap-pause-cache]] — Veja também: Eraser: listas de exclusão (`eraser.sh/cleanup.exclude`) para proteger imagens críticas e pré-cacheadas.
- [[eraser-comparacao-kubelet-image-gc-thresholds-seguranca-cve]] — Veja também: Eraser vs Kubelet Image Garbage Collection: diferenças entre limpeza por pressão de disco e limpeza orientada a CVEs.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
