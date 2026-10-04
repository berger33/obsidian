---
id: software.kubernetes.probes.000001
tipo: conceito
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
fontes: ["https://kubernetes.io/docs/concepts/workloads/pods/probes/", "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [Kubernetes probes, Liveness probe, Readiness probe, Startup probe]
lote: software-kubernetes-operacao-0005
---

# Probes de liveness, readiness e startup no Kubernetes

## Em uma frase
Probes dão ao kubelet sinais diferentes para decidir se o container ainda está iniciando, deve receber tráfego ou precisa ser reiniciado.

## Por que importa
Uma probe mal escolhida pode tirar uma instância saudável do serviço, reiniciar processos durante uma sobrecarga ou deixar uma aplicação ainda não inicializada receber requisições. As três probes não são nomes intercambiáveis: cada uma aciona uma resposta operacional distinta. A verificação também deve ser suficientemente barata e tolerante às características reais de inicialização e carga.

## Como funciona
Uma `startupProbe` verifica se a aplicação terminou de iniciar; enquanto ela não passa, liveness e readiness não são executadas. Uma `livenessProbe` detecta situações em que reiniciar o container pode ajudar, como um deadlock; se falhar além da tolerância configurada, o kubelet reinicia o container. Uma `readinessProbe` indica se o container pode aceitar tráfego; quando falha, o endereço do Pod é removido dos EndpointSlices dos Services correspondentes, sem que isso por si só reinicie o processo. Readiness e liveness são avaliadas independentemente.

## Exemplo
Um serviço que demora para carregar um modelo pode usar startup probe com uma janela compatível com o pior tempo de inicialização, readiness para só receber tráfego depois de carregar e liveness para detectar um processo que parou de progredir. A condição de liveness deve representar uma falha recuperável por reinício, não apenas indisponibilidade momentânea de uma dependência.

## Limites e trade-offs
A documentação alerta que liveness mal implementada pode causar falhas em cascata, especialmente se containers sob carga forem reiniciados repetidamente. Uma readiness permissiva pode mandar tráfego para uma instância incapaz de atender; uma readiness estrita demais pode retirar capacidade útil. Probes não substituem métricas, alertas ou tratamento correto de desligamento.

## Como verificar
Teste cada falha em um ambiente controlado: atraso de inicialização, processo travado e instância temporariamente incapaz de servir. Observe se startup adia as outras probes, se readiness altera os endpoints e se apenas a falha de liveness reinicia o container. Ajuste `periodSeconds`, `timeoutSeconds` e `failureThreshold` com base em latências medidas.

## Conexões
- [[deployment-rolling-update-kubernetes]] — prontidão influencia o progresso de uma atualização gradual.
- [[hpa-autoscaling-kubernetes]] — Pods prontos e métricas influenciam o comportamento de escala.
- [[pdb-disponibilidade-kubernetes]] — probes e orçamentos tratam aspectos distintos de disponibilidade.

## Fontes
- [Kubernetes — Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) — semântica, usos e riscos das três probes; acesso em 2026-10-01.
- [Kubernetes — Configure Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) — mecanismos e parâmetros de configuração; acesso em 2026-10-01.
