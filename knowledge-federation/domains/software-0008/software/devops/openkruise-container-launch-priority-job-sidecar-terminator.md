---
id: software.devops.tranche16.001557
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

# OpenKruise: ordenação de partida (`Container Launch Priority`) e encerramento de sidecars em Jobs (`Sidecar Terminator`)

## Em uma frase
O OpenKruise resolve dois problemas clássicos de coordenação multi-container dentro de um Pod: garantir a ordem de inicialização entre containers regulares via `apps.kruise.io/container-launch-priority` e encerrar automaticamente sidecars quando o container principal de um `Job` termina.

## Por que importa
Antes ou fora de KEP-753 (Native Sidecar Containers), se o container da aplicação iniciar antes do proxy de rede ou agente de cofre estar pronto, as primeiras requisições falham; e quando um `Job` batch termina seu processamento principal, o Pod nunca passa para `Completed` porque o container sidecar continua rodando indefinidamente.

## Como funciona
Ao definir a variável de ambiente `KRUISE_CONTAINER_PRIORITY` (ou a anotação `apps.kruise.io/container-launch-priority: Ordered`), o OpenKruise bloqueia a partida dos containers de menor prioridade até que os de maior prioridade estejam prontos. Já o *Sidecar Job Terminator* monitora Pods do tipo `Job` (`restartPolicy: Never`/`OnFailure`) e envia sinal de término aos sidecars marcados com `kruise.io/sidecar-target` assim que os containers principais concluem com código `0`.

## Exemplo
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ordered-startup-pod
  annotations:
    apps.kruise.io/container-launch-priority: Ordered
spec:
  containers:
    - name: mesh-proxy
      image: envoyproxy/envoy:v1.31.0
    - name: business-app
      image: ghcr.io/org/app:v1.0
```

## Limites e trade-offs
No modo `Ordered`, os containers iniciam estritamente na ordem em que estão declarados na lista `spec.containers` (ou segundo os valores inteiros atribuídos a `KRUISE_CONTAINER_PRIORITY`, do maior para o menor).

## Como verificar
Descreva o Pod (`kubectl describe pod ordered-startup-pod`) e verifique nos eventos que `business-app` só foi iniciado após `mesh-proxy` passar em seu `startupProbe`/`readinessProbe`.

## Conexões
- [[openkruise-sidecarset-injecao-upgrade-independente-sidecars]] — Veja também: OpenKruise SidecarSet: injeção mutante e atualização in-place independente de containers sidecar.
- [[openkruise-workloadspread-uniteddeployment-distribuicao-multi-dominio]] — Veja também: OpenKruise: distribuição multi-domínio elástica com `WorkloadSpread` e `UnitedDeployment`.

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
