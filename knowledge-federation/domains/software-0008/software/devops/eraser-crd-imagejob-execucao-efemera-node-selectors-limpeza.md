---
id: software.devops.tranche15.001499
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

# Eraser: coordenação distribuída de pods de limpeza por nó via recurso `ImageJob`

## Em uma frase
O recurso interno `ImageJob` orquestra a criação, o acompanhamento de status (`Success`, `Failed`, `Running`) e a remoção automática dos Pods de limpeza distribuídos em cada nó elegível do cluster.

## Por que importa
Se o controlador criasse Pods soltos sem um objeto coordenador de ciclo de vida, falhas em nós isolados ou a limpeza dos próprios Pods `Completed` após o término da tarefa ficariam órfãs no namespace `eraser-system`.

## Como funciona
Quando um ciclo agendado (`repeatInterval`) ou uma atualização de `ImageList` ocorre, o `eraser-controller-manager` cria um `ImageJob`, agenda um Pod por nó Linux elegível, aguarda todos os containers (`collector`, `scanner`, `remover`) finalizarem e apaga os Pods concluídos após o delay configurado de limpeza.

## Exemplo
```bash
kubectl get imagejobs -n eraser-system
kubectl describe imagejob -n eraser-system
```

## Limites e trade-offs
Por padrão, os Pods dos trabalhadores do Eraser são removidos automaticamente pouco tempo após atingirem o status `Completed`; para inspecionar seus logs durante troubleshooting, acompanhe a execução em tempo real ou ajuste os timers de retenção de sucesso/falha no ConfigMap.

## Como verificar
Acompanhe o ciclo completo com `kubectl get pods,imagejobs -n eraser-system -w` durante o disparo de uma limpeza.

## Conexões
- [[eraser-comparacao-kubelet-image-gc-thresholds-seguranca-cve]] — Veja também: Eraser vs Kubelet Image Garbage Collection: diferenças entre limpeza por pressão de disco e limpeza orientada a CVEs.
- [[eraser-governanca-cncf-openssf-scorecard-operacao-segura]] — Veja também: Eraser: governança CNCF, OpenSSF Scorecard e boas práticas operacionais com registries e mirrors.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
