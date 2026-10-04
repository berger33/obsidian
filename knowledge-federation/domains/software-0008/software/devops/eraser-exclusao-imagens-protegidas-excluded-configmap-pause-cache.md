---
id: software.devops.tranche15.001496
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

# Eraser: listas de exclusão (`eraser.sh/cleanup.exclude`) para proteger imagens críticas e pré-cacheadas

## Em uma frase
O Eraser permite definir listas de imagens excluídas da limpeza por meio de ConfigMaps rotulados no namespace `eraser-system`, garantindo que imagens base pré-carregadas (*pre-pulled*) ou imagens de sistema nunca sejam apagadas mesmo quando nenhum Pod as utiliza no instante da varredura.

## Por que importa
Em clusters de baixa latência onde imagens pesadas de IA/ML ou imagens de emergência são pré-aquecidas nos nós antes do tráfego chegar, remover essas imagens apenas porque nenhum Pod está ativo naquele minuto destruiria a estratégia de *pre-warming*.

## Como funciona
O container `collector` lê todos os ConfigMaps de exclusão configurados e filtra essas referências (por tag ou digest) antes de repassar a lista de candidatas ao `scanner` e ao `remover`. Além disso, nós específicos podem ser excluídos do agendamento do Eraser por meio de labels de seleção de nó.

## Exemplo
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: excluded-base-images
  namespace: eraser-system
  labels:
    eraser.sh/cleanup.exclude: "true"
data:
  excluded.json: |
    {"excluded": ["registry.k8s.io/pause:*", "ghcr.io/org/golden-base:*"]}
```

## Limites e trade-offs
Certifique-se de que o JSON dentro do ConfigMap de exclusão é sintaticamente válido sob a chave `"excluded"`, caso contrário o `collector` reportará erro ao processar as regras de isenção.

## Como verificar
Verifique nos logs do container `remover` que as imagens listadas no ConfigMap de exclusão foram preservadas no nó após a conclusão do job.

## Conexões
- [[eraser-crd-imagelist-remocao-seletiva-lista-imagens-comprometidas]] — Veja também: Eraser: remoção sob demanda de imagens específicas em todo o cluster via CRD `ImageList`.
- [[eraser-demo-daemonset-alpine-validacao-containerd-kind-ctr]] — Veja também: Eraser: fluxo de validação prática com DaemonSet de teste e inspeção de `containerd` via `ctr -n k8s.io`.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
