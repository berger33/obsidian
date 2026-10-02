---
id: software.kubernetes.requests-limits-recursos.000001
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
fontes: ["https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/", "https://kubernetes.io/docs/concepts/workloads/pods/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [Kubernetes resource requests, Resource limits, CPU requests, Memory limits]
lote: software-kubernetes-operacao-0005
---

# Requests e limits de CPU e memória no Kubernetes

## Em uma frase
Requests informam necessidades usadas pelo scheduler, enquanto limits definem tetos aplicados ao consumo de recursos do container.

## Por que importa
Valores ausentes ou mal calibrados podem deixar Pods sem espaço adequado, dificultar o agendamento ou produzir estrangulamento de CPU e encerramentos por memória. Requests e limits têm papéis diferentes: um request não é o mesmo que um teto, e o comportamento de CPU não é igual ao de memória. O impacto também depende de outras cargas presentes no nó.

## Como funciona
O scheduler usa requests para escolher um nó e o kubelet aplica os limites do container. Quando há recurso disponível no nó, um container pode usar mais que seu request. Em Linux, o limite de CPU é aplicado por throttling; ao se aproximar do limite, o kernel restringe acesso à CPU. Limites de memória são reativos: sob pressão de memória, ultrapassar o limite pode levar o kernel a encerrar o processo, frequentemente observado como `OOMKilled`; a terminação não precisa ocorrer no instante exato em que o valor é ultrapassado. Se um limit é definido sem request e nenhum mecanismo de admissão define um request, Kubernetes copia o limit como request.

## Exemplo
Um serviço HTTP pode começar com requests de CPU e memória medidos em carga representativa e limites alinhados ao perfil operacional. Antes de aumentar o limite de CPU para resolver latência, verifique throttling; antes de elevar memória, investigue crescimento de heap e limites do nó. Os números do manifesto devem ser específicos do serviço, não copiados sem medição.

## Limites e trade-offs
Requests influenciam posicionamento e capacidade reservada, não garantem que a aplicação terá desempenho suficiente em toda situação. Limites muito baixos podem prejudicar latência ou causar reinícios; limites excessivos podem concentrar risco de pressão no nó. Recursos de Pod-level requests/limits dependem da versão e dos feature gates; esta nota trata do modelo por container.

## Como verificar
Compare requests com consumo observado em períodos normais e picos; investigue throttling de CPU, eventos de pressão e reinícios `OOMKilled`. Teste o agendamento com a soma dos requests no nó e acompanhe os efeitos de qualquer ajuste em produção. Registre a versão do cluster e as políticas de admissão que podem preencher valores padrão.

## Conexões
- [[hpa-autoscaling-kubernetes]] — métricas percentuais de utilização são calculadas em relação aos requests correspondentes.
- [[deployment-rolling-update-kubernetes]] — surge temporário durante rollout pode exigir capacidade extra.
- [[pdb-disponibilidade-kubernetes]] — pressão de nó pode causar interrupções involuntárias que PDB não impede.

## Fontes
- [Kubernetes — Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) — agendamento, enforcement e diferença entre CPU e memória; acesso em 2026-10-01.
- [Kubernetes — Pods](https://kubernetes.io/docs/concepts/workloads/pods/) — visão geral de recursos de containers; acesso em 2026-10-01.
