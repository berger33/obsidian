---
id: software.seguranca.tranche19.001893
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

# Cilium Network Policies: Permitir tráfego L3 por labels

## Em uma frase
**Cilium Network Policies — Permitir tráfego L3 por labels:** L3 selectors permitem definir peers por identidade Kubernetes em vez de IP mutável.

## Por que importa
O recorte de **permitir tráfego l3 por labels** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **permitir tráfego l3 por labels**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Autorize ingress de frontend apenas para endpoint backend identificado por labels. Teste em staging autorizado.

## Limites e trade-offs
Labels e namespace selectors precisam refletir fronteiras confiáveis de administração. Exceções exigem responsável e prazo.

## Como verificar
Altere label de pod não autorizado e confirme que não recebe a mesma permissão. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-restringir-destinos-por-cidr]] — Complementa o tópico com cilium network policies: restringir destinos por cidr.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
