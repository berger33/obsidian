---
id: software.seguranca.tranche19.001896
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

# Cilium Network Policies: Combinar política L3 e L4

## Em uma frase
**Cilium Network Policies — Combinar política L3 e L4:** Políticas podem restringir peer de rede por protocolo e porta além da seleção L3.

## Por que importa
O recorte de **combinar política l3 e l4** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **combinar política l3 e l4**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita TCP para porta 8443 apenas entre dois serviços de staging. Teste em staging autorizado.

## Limites e trade-offs
Porta errada ou protocolo implícito pode permitir tráfego que a aplicação não usa. Exceções exigem responsável e prazo.

## Como verificar
Rode probes para porta prevista e uma porta alternativa e confira verdict de policy. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-aplicar-controles-l7-com-proxy]] — Complementa o tópico com cilium network policies: aplicar controles l7 com proxy.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
