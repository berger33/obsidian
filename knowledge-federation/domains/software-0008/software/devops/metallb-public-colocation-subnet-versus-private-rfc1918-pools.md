---
id: software.devops.tranche05.000443
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

# Configuração de múltiplos pools de IP no MetalLB: sub-redes públicas em colocation e faixas privadas RFC1918

## Em uma frase
A seção *Address allocation* de `metallb.io/concepts/` detalha como obter e combinar diferentes categorias de endereços IP no MetalLB de acordo com o ambiente: se o cluster bare-metal roda em uma instalação de **colocation**, o provedor de hospedagem normalmente aluga blocos de IPs públicos (por exemplo, um `/26` com 64 endereços), que podem ser entregues a um `IPAddressPool` para expor serviços na internet; se o cluster é **puramente privado** atendendo apenas uma LAN corporativa, escolhe-se uma faixa de endereços privados (**RFC1918**) gratuitos; ou **pode-se usar ambos simultaneamente**, já que o MetalLB permite definir quantos pools de endereços forem necessários sem se importar com o "tipo" do endereço.

## Por que importa
Em infraestruturas híbridas on-premises, expor um serviço interno de banco de dados ou painel de métricas em um IP público caro de colocation é um erro grave de segurança e desperdício de endereços IPv4 públicos. Ter múltiplos `IPAddressPools` (um público e um privado RFC1918) separa claramente o tráfego externo do interno.

## Como funciona
Crie `IPAddressPools` separados para tráfego externo público (ex.: `public-wan-pool`) e tráfego interno corporativo (ex.: `internal-lan-pool`), controlando qual serviço consome qual pool por meio de anotações ou políticas de alocação de namespace/serviço.

## Exemplo
Em um data center de colocation, o Ingress público de clientes aloca um IP do pool `/26` público, enquanto o Ingress interno do Backstage e do Grafana aloca um IP privado `10.20.30.x` do pool RFC1918 da LAN corporativa.

## Limites e trade-offs
Defina `autoAssign: false` no `IPAddressPool` de endereços públicos escassos para impedir que qualquer `Service` criado sem anotação explícita consuma acidentalmente um IP público roteável na internet.

## Como verificar
Verifique nos serviços internos e externos que cada `Service` recebeu um endereço `EXTERNAL-IP` pertencente exatamente ao `IPAddressPool` pretendido.

## Conexões
- [[metallb-address-allocation-and-ipaddresspool-management]] — Veja também: Alocação de endereços IP e gerenciamento de recursos IPAddressPool no MetalLB.
- [[metallb-layer-2-mode-arp-ipv4-and-ndp-ipv6-announcement]] — Veja também: Modo Layer 2 do MetalLB: anúncio externo via ARP (IPv4) e NDP (IPv6) na rede local.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
