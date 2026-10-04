---
id: software.seguranca.tranche19.001899
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

# Cilium Network Policies: Observar policy verdicts e Hubble

## Em uma frase
**Cilium Network Policies — Observar policy verdicts e Hubble:** Observabilidade de fluxo ajuda explicar qual regra permitiu ou bloqueou a conexão entre endpoints.

## Por que importa
O recorte de **observar policy verdicts e hubble** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **observar policy verdicts e hubble**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Correlacione tentativa canário com identity, source, destination e verdict no ambiente de staging. Teste em staging autorizado.

## Limites e trade-offs
Ausência de evento no observador não prova que não houve fluxo ou bloqueio. Exceções exigem responsável e prazo.

## Como verificar
Compare resultados Hubble com probe cliente e logs do serviço. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-implantar-mudanca-incrementalmente]] — Complementa o tópico com cilium network policies: implantar mudança incrementalmente.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
