---
id: software.devops.tranche17.001663
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

# Akri CRD `Instance`: representação de dispositivos individuais e coordenação de compartilhamento (`deviceUsage`)

## Em uma frase
Cada objeto `Instance` (`akri.sh/v0`) criado automaticamente pelo Akri Agent representa um único dispositivo físico visível ao cluster (por exemplo, se houver 5 câmeras IP na rede, existirão 5 objetos `Instance`), coordenando quais nós enxergam o dispositivo (`nodes`) e quais estão utilizando suas vagas (`deviceUsage`).

## Por que importa
Enquanto um dispositivo USB está fisicamente preso a 1 único nó (`shared: false`), uma câmera IP ONVIF ou servidor OPC UA na LAN pode ser enxergado por todos os 4 nós do cluster (`shared: true`). É preciso um mecanismo distribuído de estado para impedir que todos os 4 nós lancem brokers duplicados acima do limite `capacity` configurado.

## Como funciona
Quando o Agent descobre um dispositivo, ele cria ou atualiza o CRD `Instance` correspondente, preenchendo `brokerProperties` (variáveis de ambiente de conexão que serão injetadas no Pod broker), a lista `nodes` de nós que enxergam o recurso e um mapa `deviceUsage` com exatamente `Configuration.capacity` slots (`0` a `capacity - 1`).

## Exemplo
```bash
kubectl get akrii -o wide
kubectl get akrii <instance-name> -o yaml
```

## Limites e trade-offs
Os objetos `Instance` (`akrii`) armazenam o estado interno de coordenação entre os Agents e o Controller do Akri e nunca devem ser editados manualmente pelos usuários.

## Como verificar
Execute `kubectl get akrii -o yaml` após a descoberta de um dispositivo e inspecione os campos `spec.nodes`, `spec.shared`, `spec.deviceUsage` e `spec.brokerProperties`.

## Conexões
- [[akri-crd-configuration-brokerpodspec-capacity-servicespecs]] — Veja também: Akri CRD `Configuration`: definição de protocolo de descoberta, `capacity`, `brokerPodSpec` e `Services` automáticos.
- [[akri-agent-kubernetes-device-plugin-injecao-broker-properties-env]] — Veja também: Akri Agent: implementação dinâmica de Kubernetes Device Plugin e injeção de `brokerProperties` no container.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
