---
id: software.seguranca.tranche19.001892
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

# Cilium Network Policies: Entender transição para default-deny

## Em uma frase
**Cilium Network Policies — Entender transição para default-deny:** Quando regra seleciona endpoint para uma direção, tráfego daquela direção pode passar a depender de allow rules.

## Por que importa
O recorte de **entender transição para default-deny** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **entender transição para default-deny**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Adicione policy em staging e observe antes quais ingress e egress serão afetados. Teste em staging autorizado.

## Limites e trade-offs
Aplicar regra de observação sem perceber default-deny pode cortar DNS e health checks. Exceções exigem responsável e prazo.

## Como verificar
Teste fluxos necessários, consulte policy verdicts e mantenha rollback ao ativar enforcement. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-permitir-trafego-l3-por-labels]] — Complementa o tópico com cilium network policies: permitir tráfego l3 por labels.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
