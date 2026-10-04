---
id: software.seguranca.tranche19.001891
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

# Cilium Network Policies: Selecionar endpoints por identidade

## Em uma frase
**Cilium Network Policies — Selecionar endpoints por identidade:** Endpoint selectors usam labels para aplicar política a conjuntos de pods e Cilium associa endpoints a identidades de segurança.

## Por que importa
O recorte de **selecionar endpoints por identidade** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **selecionar endpoints por identidade**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Selecione somente pods `app=api` em namespace canário e confira endpoints correspondentes. Teste em staging autorizado.

## Limites e trade-offs
Selector amplo pode incluir pods adicionais quando novos labels são reutilizados. Exceções exigem responsável e prazo.

## Como verificar
Inspecione endpoints selecionados e teste um pod com label esperado e outro sem ela. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-entender-transicao-para-default-deny]] — Complementa o tópico com cilium network policies: entender transição para default-deny.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
