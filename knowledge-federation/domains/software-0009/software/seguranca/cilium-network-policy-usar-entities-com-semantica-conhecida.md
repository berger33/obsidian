---
id: software.seguranca.tranche19.001895
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

# Cilium Network Policies: Usar entities com semântica conhecida

## Em uma frase
**Cilium Network Policies — Usar entities com semântica conhecida:** Entities nomeadas representam conjuntos especiais como cluster, host ou world, conforme documentação da versão.

## Por que importa
O recorte de **usar entities com semântica conhecida** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar entities com semântica conhecida**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita acesso ao entity estritamente necessário para um teste de saída controlado. Teste em staging autorizado.

## Limites e trade-offs
Entity ampla como world pode aceitar destinos externos inesperados. Exceções exigem responsável e prazo.

## Como verificar
Leia semântica da versão Cilium instalada e valide destino permitido e bloqueado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-combinar-politica-l3-e-l4]] — Complementa o tópico com cilium network policies: combinar política l3 e l4.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
