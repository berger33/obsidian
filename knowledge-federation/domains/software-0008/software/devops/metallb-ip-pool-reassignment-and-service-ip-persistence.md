---
id: software.devops.tranche05.000448
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

# Persistência de IPs atribuídos a Services e reatribuição automática após edição de IPAddressPool

## Em uma frase
Conforme documentado na seção *Address allocation* de `metallb.io/concepts/`, uma vez que um ou mais endereços IP são atribuídos a um `Service`, **o MetalLB procura mantê-los atribuídos àquele mesmo serviço** enquanto ele existir. Entretanto, caso esses IPs sejam removidos dos pools configurados — por exemplo, pela exclusão ou edição do objeto `IPAddressPool` do qual aqueles IPs foram retirados —, o MetalLB detecta a mudança e **atribui automaticamente um novo conjunto de IPs disponíveis** ao serviço.

## Por que importa
Saber como o MetalLB reage à edição de um `IPAddressPool` evita surpresas durante migrações de sub-rede ou reestruturações de VLAN: encolher ou deletar um pool ativo revoga os IPs que ficaram fora do novo intervalo e força a troca imediata do `EXTERNAL-IP` dos serviços afetados.

## Como funciona
Durante migrações planejadas de sub-rede em clusters bare-metal, adicione o novo `IPAddressPool` primeiro, migre os serviços críticos de forma controlada (atualizando seus registros DNS ou via ExternalDNS) e só remova o `IPAddressPool` antigo quando nenhum serviço produtivo depender mais da faixa antiga.

## Exemplo
Ao descomissionar uma VLAN legada no data center, a equipe cria um segundo `IPAddressPool` na nova VLAN, migra os serviços gradualmente com apoio do ExternalDNS e, ao final, remove o pool antigo sem causar indisponibilidade surpresa.

## Limites e trade-offs
Não edite nem reduza a faixa de endereços de um `IPAddressPool` em horário de pico sem verificar antes quais `Services` estão usando IPs daquela subfaixa, pois os serviços afetados terão seu `EXTERNAL-IP` trocado imediatamente pelo controlador.

## Como verificar
Audite os `EXTERNAL-IP` ativos em `kubectl get svc -A` antes e depois de qualquer alteração planejada nos recursos `IPAddressPool`.

## Conexões
- [[metallb-externaltrafficpolicy-local-versus-cluster-with-metallb]] — Veja também: Comportamento de externalTrafficPolicy: Cluster vs Local em serviços gerenciados pelo MetalLB.
- [[metallb-stable-release-branches-versus-main-branch-deployments]] — Veja também: Governança de implantação do MetalLB: uso obrigatório de releases estáveis em vez da branch main.

## Fontes
- [MetalLB GitHub — README.md (Bare-Metal LoadBalancer, Stable Branch Warning & Security Reporting)](https://raw.githubusercontent.com/metallb/metallb/main/README.md) — README oficial do MetalLB descrevendo implementação de balanceador de carga para clusters Kubernetes bare-metal usando protocolos padrão de roteamento, alerta expresso contra consumo de manifestos da branch main de desenvolvimento em favor de branches estáveis e política de reporte de vulnerabilidades com meta de resposta inicial em 48 horas.; consultado em 2026-10-03.
- [MetalLB Official Documentation — Concepts (Address Allocation, IPAddressPool, Layer 2 ARP/NDP & BGP Mode)](https://metallb.io/concepts/) — Documentação oficial de conceitos do MetalLB detalhando alocação de endereços via IPAddressPool (ranges públicos alugados ou privados RFC1918), anúncio externo em modo Layer 2 (ARP para IPv4 e NDP para IPv6) e modo BGP com roteadores para balanceamento real multi-nó.; consultado em 2026-10-03.
- [MetalLB — Official GitHub Repository](https://github.com/metallb/metallb) — Repositório oficial Apache-2.0 do MetalLB na CNCF.; consultado em 2026-10-03.
