---
id: software.seguranca.tranche19.001894
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://docs.cilium.io/en/stable/security/policy/intro/", "https://docs.cilium.io/en/stable/security/policy/layer3/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cilium Network Policies: Restringir destinos por CIDR

## Em uma frase
**Cilium Network Policies — Restringir destinos por CIDR:** Regras `toCIDR` e `fromCIDR` definem faixas IP para destinos ou origens não representadas como endpoint.

## Por que importa
O recorte de **restringir destinos por cidr** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **restringir destinos por cidr**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita CIDR estreito de serviço de teste, documentando dono e motivo do endereço externo. Teste em staging autorizado.

## Limites e trade-offs
IP de service, NAT ou endpoint pode mudar e tornar CIDR obsoleto. Exceções exigem responsável e prazo.

## Como verificar
Verifique conexão pelo endereço observado no datapath e teste IP dentro e fora da faixa. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-usar-entities-com-semantica-conhecida]] — Complementa o tópico com cilium network policies: usar entities com semântica conhecida.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
