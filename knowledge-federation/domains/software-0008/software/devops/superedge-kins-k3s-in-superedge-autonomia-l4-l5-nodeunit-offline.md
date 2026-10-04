---
id: software.devops.tranche17.001653
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

# SuperEdge `Kins` (*K3s in SuperEdge*): autonomia de borda L4 e L5 com clusters K3s leves por `NodeUnit`

## Em uma frase
Introduzido no SuperEdge v0.9.0 e gerenciado pelo controlador `site-manager`, o recurso **Kins** (*K3s in SuperEdge*) eleva a autonomia de borda para os níveis **L4** (1 master K3s local) e **L5** (3 masters K3s locais em HA) provisionando automaticamente um plano de controle K3s leve dentro de cada `NodeUnit` de borda.

## Por que importa
Na autonomia L3 (apenas cache de leitura do `lite-apiserver`), se um nó dentro de uma fábrica de 10 servidores queimar enquanto o link de internet com a nuvem estiver cortado, os Pods daquele servidor não podem ser reagendados nos outros 9 servidores locais da mesma fábrica porque não há scheduler nem apiserver gravável no local.

## Como funciona
Com o `Kins` habilitado em uma `NodeUnit`, o `site-manager` implanta containers leves de K3s diretamente nos nós daquela unidade de borda. Mesmo que o site fique 100% isolado da nuvem (offline), a `NodeUnit` opera um plano de controle local completo (single-master em L4 ou HA 3-masters em L5) capaz de criar, atualizar, deletar e reagendar Pods localmente.

## Exemplo
```bash
kubectl get nodeunits
kubectl get nodegroups
```

## Limites e trade-offs
Ao escolher entre autonomia L4 e L5 em uma `NodeUnit`, lembre-se de que o nível L5 exige no mínimo 3 nós na mesma `NodeUnit` para formar o quórum local dos 3 masters K3s.

## Como verificar
Verifique os recursos `NodeUnit` gerenciados pelo `site-manager` e valide a operação de comandos locais no cluster K3s da unidade quando isolada da WAN.

## Conexões
- [[superedge-lite-apiserver-proxy-tls-cn-cache-bolt-badger-autonomia-l3]] — Veja também: SuperEdge `lite-apiserver`: proxy HTTPS por Common Name TLS e cache persistente (`file`, `bolt`, `badger`) para autonomia L3.
- [[superedge-edge-health-monitoramento-distribuido-consenso-admission]] — Veja também: SuperEdge `edge-health` e `edge-health-admission`: detecção distribuída de saúde na borda e proteção contra falsos positivos.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
