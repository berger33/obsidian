---
id: software.devops.tranche16.001556
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/openkruise/kruise/master/README.md", "https://openkruise.io/docs/user-manuals/cloneset/", "https://github.com/openkruise/kruise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenKruise SidecarSet: injeção mutante e atualização in-place independente de containers sidecar

## Em uma frase
O `SidecarSet` (`apps.kruise.io/v1alpha1`) desacopla o ciclo de vida de containers auxiliares (como coletores de logs Fluent Bit, agentes de monitoramento, proxies Envoy ou agentes de segurança) do ciclo de vida do container principal da aplicação.

## Por que importa
Em clusters Kubernetes padrão, atualizar a versão do agente de log ou proxy sidecar exige reeditar e fazer redeploy de centenas de `Deployments` de todas as equipes de produto, reiniciando desnecessariamente os processos das aplicações principais.

## Como funciona
Com o `SidecarSet`, a equipe de plataforma define o template do sidecar e um seletor de Pods (`spec.selector`). O webhook do OpenKruise injeta automaticamente o sidecar na criação de qualquer Pod correspondente e, quando a imagem do `SidecarSet` é atualizada, o controlador realiza o upgrade *in-place* apenas do container sidecar em toda a frota de Pods em execução, sem reiniciar o container da aplicação principal.

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1alpha1
kind: SidecarSet
metadata:
  name: log-collector-sidecar
spec:
  selector:
    matchLabels:
      logging.platform.io/enabled: "true"
  updateStrategy:
    type: RollingUpdate
    maxUnavailable: 10%
  containers:
    - name: fluent-bit
      image: fluent/fluent-bit:3.1.9
```

## Limites e trade-offs
Para que a atualização in-place de um sidecar ocorra sem recriação do Pod, apenas campos mutáveis pelo kubelet (essencialmente `image`) podem ser alterados no container do `SidecarSet`; adicionar novos containers ao `SidecarSet` só surtirá efeito em Pods criados posteriormente.

## Como verificar
Execute `kubectl get sidecarset log-collector-sidecar` após atualizar a tag da imagem e confirme que `UPDATED` atinge o total de `MATCHED` sem incremento de `RESTARTS` no container principal da aplicação.

## Conexões
- [[openkruise-advanced-statefulset-parallel-in-place-unordered-ready]] — Veja também: OpenKruise Advanced StatefulSet: escalonamento paralelo, rollout não ordenado e atualização in-place.
- [[openkruise-container-launch-priority-job-sidecar-terminator]] — Veja também: OpenKruise: ordenação de partida (`Container Launch Priority`) e encerramento de sidecars em Jobs (`Sidecar Terminator`).

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
