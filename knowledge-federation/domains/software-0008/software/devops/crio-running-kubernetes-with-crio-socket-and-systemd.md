---
id: software.devops.tranche04.000378
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Configuração do Kubelet com CRI-O via endpoint unix:///var/run/crio/crio.sock e systemd cgroup

## Em uma frase
A seção *Running Kubernetes with CRI-O* do README oficial demonstra os parâmetros fundamentais de integração entre o Kubernetes e o daemon `crio`: o driver de cgroups deve ser alinhado como `CGROUP_DRIVER=systemd`, o modo de runtime definido como `CONTAINER_RUNTIME=remote` e o endpoint do runtime configurado para `CONTAINER_RUNTIME_ENDPOINT='unix:///var/run/crio/crio.sock'` (correspondente a `--container-runtime-endpoint=unix:///var/run/crio/crio.sock` no Kubelet moderno).

## Por que importa
Conhecer o caminho canônico do socket Unix (`/var/run/crio/crio.sock`) e o requisito de `cgroup_driver=systemd` é indispensável ao provisionar clusters com `kubeadm`, scripts de bootstrap de nós ou ferramentas de diagnóstico como `crictl` (`/etc/crictl.yaml`).

## Como funciona
Configure `/etc/crictl.yaml` nos nós com `runtime-endpoint: unix:///var/run/crio/crio.sock` e `image-endpoint: unix:///var/run/crio/crio.sock` para que o `crictl` se comunique diretamente com o CRI-O sem avisos de descoberta de socket.

## Exemplo
Ao inicializar um nó Kubernetes com `kubeadm` usando CRI-O, o manifesto `KubeletConfiguration` define `cgroupDriver: systemd` e `criSocket: unix:///var/run/crio/crio.sock`, estabelecendo comunicação gRPC imediata após o início do serviço `crio.service`.

## Limites e trade-offs
Sempre inicie e habilite o serviço `crio` no systemd (`systemctl enable --now crio`) **antes** de iniciar o `kubelet`, pois o Kubelet entrará em falha de inicialização se o socket `/var/run/crio/crio.sock` ainda não existir.

## Como verificar
Execute `sudo crictl --runtime-endpoint unix:///var/run/crio/crio.sock version` e confirme que `RuntimeName` retorna `cri-o` em estado operacional.

## Conexões
- [[crio-oci-hooks-injection-and-annotations-migration]] — Veja também: Suporte a OCI Hooks e guia de migração de anotações no CRI-O.
- [[crio-metrics-tracing-and-evented-pleg-observability]] — Veja também: Observabilidade do CRI-O com métricas Prometheus, tracing distribuído e Evented PLEG.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
