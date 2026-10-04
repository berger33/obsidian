---
id: software.devops.tranche05.000444
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

# Modo Layer 2 do MetalLB: anúncio externo via ARP (IPv4) e NDP (IPv6) na rede local

## Em uma frase
Após alocar um IP externo a um `Service`, o MetalLB precisa informar à rede fora do cluster que aquele IP "vive" dentro do cluster. No **modo Layer 2 (`L2Advertisement`)**, documentado em `metallb.io/concepts/`, **uma máquina do cluster assume a propriedade do serviço** e responde a protocolos padrão de descoberta de endereço na camada de enlace — **ARP (Address Resolution Protocol) para IPv4** e **NDP (Neighbor Discovery Protocol) para IPv6** — tornando esses IPs alcançáveis diretamente na rede local. Do ponto de vista da LAN, a máquina anunciante simplesmente aparenta possuir múltiplos endereços IP associados à sua interface de rede.

## Por que importa
A grande vantagem do modo Layer 2 é sua universalidade e simplicidade: ele não exige nenhum roteador corporativo especial nem configuração de BGP nos switches, funcionando em qualquer rede Ethernet doméstica, de laboratório ou VLAN corporativa padrão onde os nós do cluster estejam no mesmo domínio de broadcast L2.

## Como funciona
Utilize o modo Layer 2 (`L2Advertisement` vinculado ao `IPAddressPool`) quando não tiver controle administrativo sobre os roteadores da rede física para fechar sessões BGP ou quando operar clusters menores em uma mesma sub-rede L2.

## Exemplo
Em uma filial corporativa sem roteadores BGP disponíveis para a equipe de Kubernetes, o operador cria um `IPAddressPool` na sub-rede da VLAN local e um objeto `L2Advertisement`; o pod `speaker` do MetalLB eleito líder passa a responder requisições ARP pelo IP do serviço e encaminha os pacotes via `kube-proxy`/CNI.

## Limites e trade-offs
Compreenda a limitação fundamental do modo Layer 2 documentada em `metallb.io/concepts/layer2/`: como um único nó responde ao ARP/NDP por vez para determinado IP de serviço, todo o tráfego de entrada daquele IP passa inicialmente pela placa de rede daquele único nó líder antes de ser distribuído aos pods, e o failover em caso de queda do nó depende da atualização da tabela ARP/NDP dos clientes.

## Como verificar
A partir de uma máquina externa na mesma LAN, execute `arping <EXTERNAL-IP>` (ou `ip neigh`) e confirme que o endereço MAC retornado corresponde à interface do nó trabalhador que assumiu o anúncio L2 do serviço.

## Conexões
- [[metallb-public-colocation-subnet-versus-private-rfc1918-pools]] — Veja também: Configuração de múltiplos pools de IP no MetalLB: sub-redes públicas em colocation e faixas privadas RFC1918.
- [[metallb-bgp-mode-peering-and-true-multi-node-load-balancing]] — Veja também: Modo BGP do MetalLB: sessões de peering com roteadores e balanceamento de carga real entre múltiplos nós.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
