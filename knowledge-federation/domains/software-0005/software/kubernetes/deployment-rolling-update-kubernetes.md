---
id: software.kubernetes.deployment-rolling-update.000001
tipo: tecnica
dominio: software
subdominio: kubernetes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://kubernetes.io/docs/concepts/workloads/controllers/deployment/", "https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [Kubernetes rolling update, Deployment RollingUpdate, maxSurge, maxUnavailable]
lote: software-kubernetes-operacao-0005
---

# Atualizações graduais de Deployment no Kubernetes

## Em uma frase
Um Deployment substitui gradualmente Pods antigos por novos e permite controlar a indisponibilidade e o excesso temporário de réplicas durante a atualização.

## Por que importa
Implantar uma versão nova é uma operação de disponibilidade, não só a troca de uma imagem. O rollout precisa respeitar capacidade do cluster, prontidão das réplicas e compatibilidade entre versões coexistentes. Configurações agressivas podem retirar muitas réplicas ao mesmo tempo ou criar Pods que não cabem nos nós disponíveis.

## Como funciona
A estratégia padrão do Deployment é `RollingUpdate`. `maxUnavailable` limita quantos Pods podem estar indisponíveis durante a atualização; `maxSurge` limita quantos Pods acima do número desejado podem ser criados. Os valores padrão documentados são 25% para cada um. Percentuais são arredondados para baixo em `maxUnavailable` e para cima em `maxSurge`. O controlador aumenta o novo ReplicaSet e reduz o antigo conforme as réplicas novas ficam disponíveis, e mantém histórico para permitir rollback de revisão.

## Exemplo
Com quatro réplicas e `maxSurge: 1`, o rollout pode criar uma instância temporária além das quatro desejadas. `maxUnavailable: 0` pede que nenhuma réplica disponível seja perdida por essa regra durante a troca, mas requer espaço para criar as novas antes de remover as antigas. Readiness probes e recursos disponíveis são parte da capacidade de progredir.

## Limites e trade-offs
RollingUpdate não garante ausência de downtime: isso depende de réplicas suficientes, prontidão correta, balanceamento e capacidade de atender carga. Pods em término ainda podem consumir recursos depois do limite previsto pelo surge. Rollback do Deployment não reverte mudanças de banco ou efeitos de negócio; versões sobrepostas precisam ser compatíveis com contratos e esquemas compartilhados.

## Como verificar
Acompanhe `kubectl rollout status`, réplicas disponíveis, eventos, capacidade do cluster e erros por versão. Em staging, simule uma imagem inválida e uma readiness que nunca passa; confirme que o rollout para e que rollback é operacional. Teste também deploy e rollback com migrations expand-contract quando houver alteração de esquema.

## Conexões
- [[probes-kubernetes-liveness-readiness-startup]] — readiness determina quando uma réplica nova está disponível para receber tráfego.
- [[requests-limits-cpu-memoria-kubernetes]] — surge temporário precisa de CPU e memória agendáveis.
- [[pdb-disponibilidade-kubernetes]] — PDB não limita rollouts de Deployment; a estratégia de rollout faz esse controle.
- [[migracoes-expand-contract]] — banco e aplicação podem coexistir durante a troca gradual.

## Fontes
- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — comportamento e parâmetros de atualização; acesso em 2026-10-01.
- [Kubernetes — Update a Deployment Without Downtime](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/) — configuração e monitoramento de um rollout; acesso em 2026-10-01.
