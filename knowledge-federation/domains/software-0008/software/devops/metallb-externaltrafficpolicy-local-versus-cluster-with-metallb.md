---
id: software.devops.tranche05.000447
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/metallb/metallb/main/README.md", "https://metallb.io/concepts/", "https://github.com/metallb/metallb"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Comportamento de externalTrafficPolicy: Cluster vs Local em serviços gerenciados pelo MetalLB

## Em uma frase
Ao expor um `Service` do tipo `LoadBalancer` com o MetalLB, a configuração **`spec.externalTrafficPolicy`** do serviço Kubernetes altera diretamente como o MetalLB anuncia o IP e como o tráfego flui pelos nós: com `externalTrafficPolicy: Cluster` (o padrão), qualquer nó elegível do cluster pode anunciar/receber o tráfego e o `kube-proxy`/CNI redireciona o pacote para o nó onde o pod de destino reside (fazendo SNAT do IP de origem do cliente); já com **`externalTrafficPolicy: Local`**, apenas os nós que possuem pelo menos um pod saudável daquele serviço em execução local anunciam o IP (via BGP ou participando da eleição Layer 2), preservando o **endereço IP real de origem do cliente** e eliminando um salto extra de rede entre nós.

## Por que importa
Controladores de Ingress, servidores DNS (como CoreDNS externo) e proxies de borda (como Envoy/Traefik) frequentemente precisam enxergar o IP real do cliente para aplicar listas de controle de acesso (ACLs), geolocalização e logs de auditoria precisos.

## Como funciona
Configure `externalTrafficPolicy: Local` nos serviços `LoadBalancer` de controladores de Ingress e proxies de entrada gerenciados pelo MetalLB quando precisar preservar o IP de origem do cliente e evitar saltos extras entre nós.

## Exemplo
No modo BGP com `externalTrafficPolicy: Local`, apenas os 3 nós onde rodam os pods do Ingress NGINX anunciam a rota `/32` do serviço ao roteador ToR; os roteadores enviam tráfego exclusivamente para esses 3 nós e os logs de acesso registram o IP verdadeiro de cada cliente.

## Limites e trade-offs
Com `externalTrafficPolicy: Local` no modo BGP, lembre-se de que os nós que não hospedam réplicas daquele pod retiram a rota BGP daquele IP; se todos os pods do serviço caírem, nenhum nó anunciará o IP até que ao menos um pod volte a ficar `Ready`.

## Como verificar
Inspecione os logs de acesso de um pod exposto via MetalLB com `externalTrafficPolicy: Local` e confirme o registro do IP real da máquina cliente em vez do IP interno CNI do nó Kubernetes.

## Conexões
- [[metallb-controller-and-speaker-pods-architecture]] — Veja também: Arquitetura de componentes do MetalLB: Deployment controller (alocação) e DaemonSet speaker (anúncio).
- [[metallb-ip-pool-reassignment-and-service-ip-persistence]] — Veja também: Persistência de IPs atribuídos a Services e reatribuição automática após edição de IPAddressPool.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
