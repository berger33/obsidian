---
id: software.devops.tranche09.000815
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/k3s-io/k3s/main/README.md", "https://docs.k3s.io/architecture", "https://github.com/k3s-io/k3s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K3s: proteção de identidade de nós com Secrets node-password.k3s e flag --with-node-id

## Em uma frase
O K3s protege a integridade da identidade de cada nó exigindo, além do token de join do cluster, uma senha aleatória gerada pelo agente em `/etc/rancher/node/password` e validada contra o hash armazenado no Secret `<node-name>.node-password.k3s` no namespace `kube-system`.

## Por que importa
Em clusters onde um mesmo token de join (`node-token`) é usado para provisionar dezenas de nós workers, se qualquer máquina pudesse simplesmente se registrar assumindo o hostname de um nó existente sem verificação adicional, um nó malicioso ou mal configurado poderia sequestrar a identidade e os certificados daquele nó. A seção `Node-password secrets` em `docs.k3s.io/architecture` explica como o K3s previne esse conflito e como lidar com recriação de máquinas.

## Como funciona
Na primeira vez que um nó se registra no cluster K3s, ele apresenta o join token e uma senha aleatória gerada localmente e salva em **`/etc/rancher/node/password`**. O servidor K3s grava um hash dessa senha em um Secret Kubernetes chamado **`<node-name>.node-password.k3s`** dentro do namespace `kube-system`. Qualquer tentativa futura de re-registrar ou renovar certificados usando aquele mesmo `<node-name>` deve apresentar a mesma senha. Quando um recurso `Node` é deletado do cluster (`kubectl delete node <nome>`), o K3s apaga automaticamente o Secret `<node-name>.node-password.k3s` correspondente.

## Exemplo
```bash
# Listar os Secrets de identidade de senha de nós (node-password.k3s) gerenciados pelo K3s no kube-system
sudo k3s kubectl get secrets -n kube-system | grep "\.node-password\.k3s"
```

## Limites e trade-offs
Conforme alerta a documentação oficial de arquitetura do K3s, se um nó worker for formatado/recriado do zero mantendo o mesmo hostname (perdendo o arquivo `/etc/rancher/node/password` antigo) sem antes ter sido removido do cluster, o novo nó será rejeitado com erro de senha inválida ao tentar entrar; para resolver isso, deve-se deletar o nó antigo (`kubectl delete node <nome>`) antes de reingressar, ou iniciar o K3s com a flag **`--with-node-id`** (que anexa automaticamente um ID único ao hostname do nó).

## Como verificar
Verifique a existência do arquivo `/etc/rancher/node/password` no host do nó K3s e confirme a correspondência com o Secret `<node-name>.node-password.k3s` em `kube-system`.

## Conexões
- [[k3s-arquitetura-servers-agents-tunel-websocket-loadbalancer]] — Veja também: K3s: arquitetura de nós Server e Agent, túnel WebSocket reverso do kubelet e load balancer client-side.
- [[k3s-auto-deploy-manifestos-helm-controller-crd]] — Veja também: K3s: auto-deploy em tempo real de manifestos em /var/lib/rancher/k3s/server/manifests e Helm-controller (CRD HelmChart).
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[k3s-gerenciamento-certificados-tls-rotacao-operacoes]] — Referência cruzada direta com k3s-gerenciamento-certificados-tls-rotacao-operacoes.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
