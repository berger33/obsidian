---
id: software.devops.tranche17.001642
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
fontes: ["https://openyurt.io/docs/core-concepts/architecture/", "https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md", "https://github.com/openyurtio/openyurt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenYurt `YurtHub`: proxy sidecar de nó e cache em disco local para autonomia de borda em desconexões

## Em uma frase
O `YurtHub` é um Static Pod executado em cada worker node do OpenYurt que intercepta todas as requisições enviadas pelos componentes locais (`kubelet`, `kube-proxy`, plugins CNI como Flannel e Pods de aplicação) ao `kube-apiserver` na nuvem, armazenando as respostas em cache no disco local.

## Por que importa
Quando um nó de borda perde conectividade com a nuvem e reinicia, um `kubelet` padrão apontando diretamente para o `kube-apiserver` remoto não consegue recuperar a lista de Pods atribuídos àquele nó e encerra ou deixa de iniciar os containers locais.

## Como funciona
No modo `edge`, o `kubelet` e o `kube-proxy` do nó são configurados para apontar para o endereço local do `YurtHub` (`127.0.0.1:10261`). Enquanto a rede está saudável, o `YurtHub` encaminha as chamadas ao `kube-apiserver` e grava os objetos no disco local; quando a conexão nuvem-borda cai, o `YurtHub` serve as respostas diretamente do cache local em disco, garantindo que o nó e todas as suas aplicações continuem operando mesmo após um reboot completo offline.

## Exemplo
```bash
# No nó de borda:
curl -s http://127.0.0.1:10267/v1/healthz
ls -la /etc/kubernetes/cache/kubelet/
```

## Limites e trade-offs
O `YurtHub` opera em dois modos (`edge` e `cloud`): nos nós da nuvem (`openyurt.io/is-edge-worker: false`), o `YurtHub` atua como proxy sem precisar manter cache offline em disco, enquanto nos nós de borda o cache persistente é ativado.

## Como verificar
Consulte o endpoint local de saúde do `YurtHub` e verifique o diretório `/etc/kubernetes/cache/` no nó de borda para confirmar que os manifestos do `kubelet` e `kube-proxy` estão persistidos em disco.

## Conexões
- [[openyurt-arquitetura-nao-intrusiva-cloud-edge-cncf-incubating]] — Veja também: OpenYurt: arquitetura cloud-edge não intrusiva CNCF Incubating (`YurtHub`, `Yurt-Manager`, `Raven` e `YurtIoTDock`).
- [[openyurt-nodepool-gerenciamento-regioes-fisicas-isolamento-trafego]] — Veja também: OpenYurt `NodePool`: agrupamento declarativo de nós por região física e fechamento de tráfego intra-pool.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://openyurt.io/docs/core-concepts/architecture/) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
