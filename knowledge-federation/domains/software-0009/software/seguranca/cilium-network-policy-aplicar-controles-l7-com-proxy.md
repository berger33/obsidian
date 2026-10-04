---
id: software.seguranca.tranche19.001897
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

# Cilium Network Policies: Aplicar controles L7 com proxy

## Em uma frase
**Cilium Network Policies — Aplicar controles L7 com proxy:** Filtros L7 inspecionam protocolos suportados e podem encaminhar tráfego via proxy do datapath.

## Por que importa
O recorte de **aplicar controles l7 com proxy** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **aplicar controles l7 com proxy**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em ambiente isolado, permita método HTTP e path esperados entre frontend e API. Teste em staging autorizado.

## Limites e trade-offs
L7 pode afetar latência, TLS passthrough e compatibilidade de protocolo. Exceções exigem responsável e prazo.

## Como verificar
Teste methods permitidos e negados, latência e logs antes de aplicar em produção. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-usar-dns-policy-com-allowlist]] — Complementa o tópico com cilium network policies: usar dns policy com allowlist.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
