---
id: software.devops.tranche05.000441
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

# MetalLB como implementação de Services do tipo LoadBalancer para Kubernetes bare-metal

## Em uma frase
O MetalLB (`metallb.io`), licenciado sob Apache-2.0, é uma implementação de balanceador de carga de rede para clusters **Kubernetes bare-metal** que utiliza protocolos padrão de rede e roteamento. Em um cluster Kubernetes rodando em provedores de nuvem pública (como AWS, GCP ou Azure), criar um `Service` do tipo `type: LoadBalancer` aciona automaticamente um balanceador de carga gerenciado pago da nuvem; já em clusters bare-metal (on-premises, colocation ou laboratórios locais), o Kubernetes não possui implementação nativa de balanceador de carga externo e deixa o campo `EXTERNAL-IP` perpetuamente em estado `<pending>`. O MetalLB preenche exatamente essa lacuna conectando-se ao cluster para viabilizar serviços `type: LoadBalancer` fora da nuvem pública.

## Por que importa
Sem o MetalLB (ou equivalente), expor serviços em clusters bare-metal fica limitado a `NodePort` (portas altas acima de 30000 acopladas ao IP individual de um nó) ou `externalIPs` manuais sem failover automático, dificultando a operação de controladores de Ingress e Gateways em data centers próprios.

## Como funciona
Implante o MetalLB em clusters Kubernetes on-premises, bare-metal ou de borda para que controladores de Ingress (como NGINX Ingress, Traefik ou Envoy) e serviços críticos recebam endereços IP externos dedicados automaticamente via `type: LoadBalancer`.

## Exemplo
Em um cluster Kubernetes bare-metal recém-provisionado no data center corporativo, o serviço do controlador de Ingress ficava travado em `EXTERNAL-IP <pending>`; após instalar o MetalLB e configurar um pool de endereços IP da rede local, o serviço recebe imediatamente um IP roteável na LAN.

## Limites e trade-offs
Observe o alerta em destaque (`# WARNING`) no README oficial do MetalLB: a branch `main` é a branch de desenvolvimento e consumir manifestos diretamente da `main` pode resultar em implantações instáveis ou sem compatibilidade retroativa; consuma **sempre uma branch/release estável** conforme descrito em `metallb.io/installation/`.

## Como verificar
Crie um `Service` com `type: LoadBalancer` no cluster com MetalLB configurado e verifique com `kubectl get svc` que `EXTERNAL-IP` muda de `<pending>` para um endereço IP válido do pool.

## Conexões
- [[metallb-address-allocation-and-ipaddresspool-management]] — Veja também: Alocação de endereços IP e gerenciamento de recursos IPAddressPool no MetalLB.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
