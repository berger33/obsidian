---
id: software.devops.tranche17.001650
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
fontes: ["https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md", "https://openyurt.io/docs/core-concepts/architecture/", "https://github.com/openyurtio/openyurt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenYurt: instalação de componentes de control plane e ingresso de nós de borda (`yurtadm join`)

## Em uma frase
A implantação do OpenYurt divide-se em duas fases claras: instalar os componentes de control plane no cluster Kubernetes (`yurt-manager`, `yurt-iot-dock`, `raven-agent`) via Helm e ingressar ou converter nós workers com `yurtadm join`.

## Por que importa
Permite transformar qualquer cluster Kubernetes upstream existente (até v1.34 certificado) em uma plataforma híbrida cloud-edge sem precisar reinstalar o control plane do Kubernetes.

## Como funciona
Na Parte 1, o administrador instala os charts do OpenYurt no cluster central. Na Parte 2, executa `yurtadm join <apiserver-ip:port> --token=<bootstrap-token> --node-type=edge` (ou `--node-type=cloud`) em cada máquina worker: o `yurtadm` configura automaticamente o Static Pod do `YurtHub`, aponta o `kubelet` para a porta local do `YurtHub` e rotula o nó com `openyurt.io/is-edge-worker`.

## Exemplo
```bash
yurtadm join 198.51.100.20:6443 \
  --token=abcdef.0123456789abcdef \
  --node-type=edge \
  --discovery-token-ca-cert-hash=sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
```

## Limites e trade-offs
Ao ingressar um nó com `--node-type=edge`, certifique-se de que as portas necessárias para o `YurtHub` local (`10261`/`10267`) não estejam ocupadas por outros processos no host.

## Como verificar
Após concluir o `yurtadm join`, execute `kubectl get nodes -L openyurt.io/is-edge-worker` e confirme que o novo nó ingressou como `Ready` e `openyurt.io/is-edge-worker=true`.

## Conexões
- [[openyurt-yurt-manager-controladores-webhooks-alta-disponibilidade]] — Veja também: OpenYurt `Yurt-Manager`: consolidação de controladores e webhooks cloud-edge em alta disponibilidade.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://openyurt.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
