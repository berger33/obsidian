---
id: software.devops.tranche05.000446
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

# Arquitetura de componentes do MetalLB: Deployment controller (alocação) e DaemonSet speaker (anúncio)

## Em uma frase
A implementação das duas funções centrais descritas em `metallb.io/concepts/` divide-se em dois componentes executados no cluster Kubernetes: o **`controller`** (implantado como um `Deployment` de escopo de cluster), que observa objetos `Service` do tipo `LoadBalancer` e gerencia a **alocação de endereços IP** a partir dos `IPAddressPools`; e o **`speaker`** (implantado como um `DaemonSet` que roda em cada nó do cluster com rede do host), que realiza o **anúncio externo** dos IPs alocados utilizando ARP/NDP (modo Layer 2) ou estabelecendo sessões BGP (modo BGP).

## Por que importa
Separar a alocação de IPs (`controller`) do anúncio de protocolo de rede nos hosts (`speaker`) permite diagnosticar imediatamente um problema: se o `Service` continua com `EXTERNAL-IP <pending>`, o problema está na configuração de pools ou no `controller`; se o `Service` já recebeu um `EXTERNAL-IP` mas não responde na rede, o problema está no `speaker` ou no firewall/roteador.

## Como funciona
Monitore separadamente a disponibilidade do Deployment `controller` e do DaemonSet `speaker` no namespace `metallb-system`, garantindo que os pods `speaker` tenham permissão de rede de host e tráfego liberado nas portas de protocolo necessárias (como TCP 179 para BGP e lista de membros Memberlist).

## Exemplo
Quando um serviço recebe o IP `10.10.50.10` mas clientes externos sofrem timeout de conexão, o engenheiro sabe que o `controller` já cumpriu seu papel de alocação e foca a investigação nos pods `speaker` e nos filtros de VLAN do switch físico.

## Limites e trade-offs
Se você aplicar seletores de nós (`nodeSelectors`) ao DaemonSet `speaker` ou às políticas de `L2Advertisement`/`BGPAdvertisement`, certifique-se de que os nós selecionados não estejam isolados por regras de firewall que bloqueiem pacotes ARP/NDP ou sessões BGP.

## Como verificar
Execute `kubectl get pods -n metallb-system -o wide` e confirme que o pod `controller` e todos os pods `speaker` nos nós elegíveis estão `Running` e `Ready`.

## Conexões
- [[metallb-bgp-mode-peering-and-true-multi-node-load-balancing]] — Veja também: Modo BGP do MetalLB: sessões de peering com roteadores e balanceamento de carga real entre múltiplos nós.
- [[metallb-externaltrafficpolicy-local-versus-cluster-with-metallb]] — Veja também: Comportamento de externalTrafficPolicy: Cluster vs Local em serviços gerenciados pelo MetalLB.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
