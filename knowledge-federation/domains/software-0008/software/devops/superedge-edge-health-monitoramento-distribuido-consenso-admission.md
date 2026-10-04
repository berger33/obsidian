---
id: software.devops.tranche17.001654
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/superedge/superedge/main/README.md", "https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md", "https://github.com/superedge/superedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SuperEdge `edge-health` e `edge-health-admission`: detecção distribuída de saúde na borda e proteção contra falsos positivos

## Em uma frase
O subsistema `edge-health` (DaemonSet nos nós de borda) e `edge-health-admission` (webhook na nuvem) realiza verificações de saúde P2P entre os nós da mesma região de borda para distinguir se um nó realmente falhou ou se apenas o link WAN entre a região e a nuvem está instável.

## Por que importa
Se o link de internet de uma filial cair por 10 minutos, o `kube-controller-manager` na nuvem para de receber heartbeats de todos os nós daquela filial e marca todos como `ConditionUnknown`, disparando evicções em massa mesmo que todos os servidores da filial estejam perfeitamente saudáveis na LAN local.

## Como funciona
Os agentes `edge-health` dentro da mesma `NodeUnit` (região de borda) sondam continuamente uns aos outros pela rede local e votam em consenso sobre a saúde real de cada par. Se o nó A perder contato com a nuvem, mas os nós B e C da mesma filial reportarem à nuvem que o nó A continua vivo na LAN, o `edge-health-admission` intercepta o controlador da nuvem e impede a marcação indevida de falha e a evicção dos Pods do nó A.

## Exemplo
```bash
kubectl get pods -n edge-system -l app=edge-health
kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations | grep edge-health
```

## Limites e trade-offs
Para que a votação distribuída do `edge-health` tenha efeito em uma região, a `NodeUnit` deve conter múltiplos nós capazes de se comunicar na mesma LAN local.

## Como verificar
Inspecione os logs e anotações de consenso de saúde gerados pelo `edge-health` nos objetos `Node` da mesma região (`kubectl describe node <edge-node>`).

## Conexões
- [[superedge-kins-k3s-in-superedge-autonomia-l4-l5-nodeunit-offline]] — Veja também: SuperEdge `Kins` (*K3s in SuperEdge*): autonomia de borda L4 e L5 com clusters K3s leves por `NodeUnit`.
- [[superedge-servicegroup-deploymentgrid-statefulsetgrid-servicegrid]] — Veja também: SuperEdge `ServiceGroup`: orquestração multi-região com `DeploymentGrid`, `StatefulSetGrid` e `ServiceGrid`.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
