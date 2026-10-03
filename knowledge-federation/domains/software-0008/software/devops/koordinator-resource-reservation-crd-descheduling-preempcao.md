---
id: software.devops.tranche16.001567
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
fontes: ["https://koordinator.sh/docs/architecture/overview/", "https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md", "https://github.com/koordinator-sh/koordinator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Koordinator: reserva explícita de recursos de nó via CRD `Reservation` e `NodeReservation`

## Em uma frase
O Koordinator introduz o CRD `Reservation` (`scheduling.koordinator.sh/v1alpha1`) para reservar preventivamente recursos específicos de um nó para Pods futuros ou em migração, sem precisar criar Pods "pause" fictícios (*balloon pods*).

## Por que importa
No Kubernetes padrão, quando um Descheduler remove um Pod de um nó sobrecarregado ou durante uma migração/upgrade, outro Pod concorrente na fila pode "roubar" a vaga no nó de destino antes que o Pod migrado seja recriado, deixando a aplicação original `Pending`.

## Como funciona
Um objeto `Reservation` funciona como um contrato de reserva de capacidade avaliado nativamente pelo `koord-scheduler`: ele aloca virtualmente CPU, memória, GPUs ou portas em um nó para um `allocateOnce` ou proprietário específico (`owners` por seletor de labels/controller) com tempo de expiração (`ttl`). Adicionalmente, o recurso de *Node Reservation* permite reservar fatias do nó para processos importantes que rodam fora do Kubernetes (daemons systemd não containerizados).

## Exemplo
```yaml
apiVersion: scheduling.koordinator.sh/v1alpha1
kind: Reservation
metadata:
  name: reserve-for-checkout-migration
spec:
  ttl: 15m
  allocateOnce: true
  template:
    spec:
      schedulerName: koord-scheduler
      containers:
        - name: placeholder
          resources:
            requests:
              cpu: "4"
              memory: "8Gi"
  owners:
    - labelSelector:
        matchLabels:
          app: checkout
```

## Limites e trade-offs
Sempre defina um `spec.ttl` (ou `expires`) razoável nas `Reservations` para evitar que uma reserva órfã (cujo workload alvo foi cancelado) retenha capacidade ociosa no cluster indefinidamente.

## Como verificar
Execute `kubectl get reservation` e confirme que a fase passa para `Available` quando o `koord-scheduler` vincula a reserva a um nó compatível, passando para `Succeeded` quando o Pod proprietário a consome.

## Conexões
- [[koordinator-koordlet-qos-manager-supressao-dinamica-interferencia]] — Veja também: Koordinator: detecção de interferência e supressão dinâmica de cargas batch pelo `koordlet` QoS Manager.
- [[koordinator-koord-descheduler-rebalanceamento-carga-seguro]] — Veja também: Koordinator: `koord-descheduler` com migração segura apoiada em `Reservation` e balanceamento de carga.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
