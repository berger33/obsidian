---
id: software.devops.tranche17.001667
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
fontes: ["https://docs.akri.sh/architecture/architecture-overview", "https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md", "https://raw.githubusercontent.com/project-akri/akri/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Akri: compartilhamento multi-nó e alta disponibilidade de dispositivos de rede com `spec.capacity`

## Em uma frase
Para dispositivos acessíveis pela rede local (como câmeras IP ONVIF ou CLPs OPC UA), o campo `spec.capacity` da `Configuration` controla quantos nós do cluster podem executar simultaneamente um broker Pod conectado ao mesmo dispositivo físico.

## Por que importa
Em um cluster de borda de 3 Raspberry Pis na mesma VLAN de uma câmera IP crítica: se `capacity: 1`, apenas 1 nó processa o stream por vez (com failover automático para outro Pi se o primeiro cair); se `capacity: 2`, 2 nós processam o stream em ativo-ativo para alta disponibilidade imediata sem tempo de cold-start.

## Como funciona
Os Akri Agents dos 3 nós descobrem a mesma câmera IP, geram exatamente o mesmo hash determinístico de nome de `Instance` e registram-se na lista `spec.nodes` daquela `Instance`. O Akri Controller e os Agents usam os slots `deviceUsage` do objeto `Instance` para garantir que no máximo `capacity` nós aloquem brokers simultaneamente.

## Exemplo
```yaml
apiVersion: akri.sh/v0
kind: Configuration
metadata:
  name: akri-onvif-cameras
spec:
  capacity: 2
  discoveryHandler:
    name: onvif
    discoveryDetails: |
      ipAddresses:
        action: Exclude
        items: []
      macAddresses:
        action: Exclude
        items: []
      discoveryTimeoutSeconds: 5
```

## Limites e trade-offs
Para dispositivos conectados localmente a um barramento físico exclusivo de um único host (como uma câmera USB descoberta via `udev`), `shared` é `false` e apenas o nó físico onde o cabo está plugado pode hospedar o broker Pod.

## Como verificar
Configure `capacity: 2` para um recurso compartilhado (`onvif` ou `debugEcho` com `shared: true`) em um cluster de 3 nós e verifique que exatamente 2 broker Pods são criados em 2 nós distintos.

## Conexões
- [[akri-controller-reconciliacao-broker-pods-instance-configuration-services]] — Veja também: Akri Controller: orquestração automática de Broker Pods, Services por instância e Services por configuração.
- [[akri-debug-echo-discovery-handler-simulacao-testes-ci]] — Veja também: Akri: simulação de dispositivos folha intermitentes em CI/CD com o handler `debugEcho`.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
