---
id: software.devops.tranche05.000442
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

# Alocação de endereços IP e gerenciamento de recursos IPAddressPool no MetalLB

## Em uma frase
A documentação oficial de conceitos (`metallb.io/concepts/`) explica que o MetalLB opera combinando duas responsabilidades: **alocação de endereços (address allocation)** e **anúncio externo (external announcement)**. Como o MetalLB não pode criar endereços IP do nada ("cannot create IP addresses out of thin air"), o administrador deve fornecer a ele pools de endereços IP utilizáveis por meio de recursos **`IPAddressPool`**. O MetalLB encarrega-se de atribuir e liberar endereços individuais à medida que serviços `LoadBalancer` são criados e removidos, entregando exclusivamente IPs que pertençam aos seus pools configurados.

## Por que importa
Quando um ou mais IPs são atribuídos a um `Service`, o MetalLB mantém esses IPs vinculados àquele serviço durante todo o seu ciclo de vida; caso esses IPs sejam removidos da configuração (por exclusão ou edição do `IPAddressPool` de origem), o MetalLB reatribui automaticamente outro conjunto de IPs disponíveis ao serviço.

## Como funciona
Defina um ou mais objetos `IPAddressPool` no namespace do MetalLB especificando faixas CIDR ou intervalos (`start-end`) reservados exclusivamente para o MetalLB na sua sub-rede, garantindo que o servidor DHCP da rede não entregue esses mesmos IPs a outros hosts.

## Exemplo
O administrador de rede reserva a faixa `.200` a `.250` da VLAN de servidores e o engenheiro de plataforma cria um `IPAddressPool` com esse intervalo no MetalLB; cada novo `Service` do tipo `LoadBalancer` recebe automaticamente o próximo IP livre da faixa.

## Limites e trade-offs
Nunca inclua no `IPAddressPool` endereços IP que já estejam em uso por servidores físicos, gateways ou dentro do escopo dinâmico do servidor DHCP da rede local, pois isso causará conflito de IP imediato na LAN.

## Como verificar
Inspecione os recursos `kubectl get ipaddresspools -n metallb-system` e os eventos do `Service` confirmando a alocação a partir do pool esperado.

## Conexões
- [[metallb-bare-metal-loadbalancer-service-implementation]] — Veja também: MetalLB como implementação de Services do tipo LoadBalancer para Kubernetes bare-metal.
- [[metallb-public-colocation-subnet-versus-private-rfc1918-pools]] — Veja também: Configuração de múltiplos pools de IP no MetalLB: sub-redes públicas em colocation e faixas privadas RFC1918.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
