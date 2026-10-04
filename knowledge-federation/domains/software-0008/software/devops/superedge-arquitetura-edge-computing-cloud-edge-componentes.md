---
id: software.devops.tranche17.001651
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

# SuperEdge: arquitetura de gerenciamento de containers em múltiplas regiões de borda

## Em uma frase
O SuperEdge (iniciado por Tencent, Intel, VMware, Huya, Cambricon, Capitalonline e Meituan, licenciado sob Apache 2.0) é um sistema de gerenciamento de containers nativo de Kubernetes para computação de borda que administra recursos e aplicações espalhados em múltiplas regiões de borda como um único cluster Kubernetes.

## Por que importa
Converter um cluster Kubernetes tradicional para operar centenas de sites de borda exige resolver simultaneamente quatro desafios: túneis reversos através de NAT (`tunnel`), autonomia local em desconexões (`lite-apiserver` / `Kins`), consenso distribuído de saúde na borda (`edge-health`) e fechamento de tráfego regional (`ServiceGroup`).

## Como funciona
A arquitetura do SuperEdge divide-se em componentes de **Nuvem** (`tunnel-cloud`, `application-grid-controller`, `edge-health-admission` e `site-manager`) e componentes de **Borda** (`lite-apiserver`, `edge-health`, `tunnel-edge` e `application-grid-wrapper`), instaláveis via `edgeadm` sem alterar o código-fonte do Kubernetes upstream.

## Exemplo
```bash
./edgeadm init --kubernetes-version=1.22.6 \
  --image-repository superedge.tencentcloudcr.com/superedge \
  --service-cidr=10.96.0.0/12 \
  --pod-network-cidr=192.168.0.0/16 \
  --enable-edge=true --edge-version=0.9.0
```

## Limites e trade-offs
Para ingressar um nó de borda no cluster SuperEdge com `./edgeadm join`, é obrigatório passar a flag `--enable-edge=true` para que o `lite-apiserver` e os agentes de borda sejam configurados no nó.

## Como verificar
Execute `kubectl get pods -n edge-system` após o bootstrap com `edgeadm` e confirme a execução dos componentes de nuvem e de borda.

## Conexões
- [[superedge-lite-apiserver-proxy-tls-cn-cache-bolt-badger-autonomia-l3]] — Veja também: SuperEdge `lite-apiserver`: proxy HTTPS por Common Name TLS e cache persistente (`file`, `bolt`, `badger`) para autonomia L3.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
