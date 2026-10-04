---
id: software.devops.tranche13.001286
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md", "https://kube-vip.io/docs/about/architecture/", "https://github.com/kube-vip/kube-vip"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kube-vip: Arquivo de Configuração de Runtime (--config-file), Ordem de Precedência e Validação Estrita

## Em uma frase
Os subcomandos `manager` e `service` do `kube-vip` aceitam um arquivo de configuração YAML ou JSON estrito via flag `--config-file PATH` ou variável de ambiente `config_file`, resolvendo valores na ordem de precedência: **1º flags de CLI explícitas, 2º variáveis de ambiente, 3º arquivo de configuração e 4º defaults do comando**.

## Por que importa
Misturar flags de linha de comando, variáveis de ambiente no manifesto do Pod e arquivos de configuração sem conhecer a regra de precedência faz com que um valor booleano `false` ou string vazia sobrescreva configurações de forma inesperada.

## Como funciona
Qualquer valor explicitamente fornecido (mesmo `false`, `0` ou `""`) em uma fonte de maior prioridade sobrescreve fontes de menor prioridade, enquanto valores omitidos não sobrescrevem. Além disso, o parser de runtime rejeita chaves desconhecidas ou chaves exclusivas de geração de manifesto (`loadBalancers`, `bgpPeers`, `singleNode`, `startAsLeader`, `addPeersAsBackends`, `isDualStack`, `requireDualStack`).

## Exemplo
```yaml
# Exemplo de arquivo de configuracao de runtime valido para --config-file:
address: "192.168.1.100"
port: 6443
interface: "eth0"
enableControlPlane: true
enableServices: true
enableARP: true
enableLeaderElection: true
```

## Limites e trade-offs
Incluir chaves derivadas em tempo de execução (`isDualStack`, `requireDualStack`) ou chaves de gerador (`singleNode`, `startAsLeader`) dentro do arquivo passado em `--config-file` faz o `kube-vip` abortar a inicialização por chave desconhecida.

## Como verificar
Use apenas os nomes externos documentados (`enableARP`, `dnsDualStackMode`, `bgpConfig.routerID`, `bgpConfig.peers`) no arquivo de `--config-file`.

## Conexões
- [[kubevip-service-loadbalancer-cloud-provider-ipam-annotations]] — Veja também: kube-vip: Balanceamento de Kubernetes Services (svc_enable) e Integração com kube-vip-cloud-provider.
- [[kubevip-gateway-api-loadbalancer-sem-endpoints-annotation]] — Veja também: kube-vip: Suporte a Services LoadBalancer de Gateway API sem Endpoints (allow-reconcile-without-endpoints).

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
