---
id: software.seguranca.tranche19.001898
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

# Cilium Network Policies: Usar DNS policy com allowlist

## Em uma frase
**Cilium Network Policies — Usar DNS policy com allowlist:** Cilium pode associar tráfego DNS a regras que permitem destinos observados por nomes de domínio.

## Por que importa
O recorte de **usar dns policy com allowlist** ajuda a aplicar segmentação baseada em identidade de endpoint e regras de rede observáveis no datapath eBPF. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar dns policy com allowlist**, Cilium seleciona endpoints por labels e aplica regras ingress/egress, podendo combinar filtros CIDR, portas, serviços e protocolo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Resolva domínio de teste pelo caminho monitorado e permita apenas serviço externo requerido. Teste em staging autorizado.

## Limites e trade-offs
DNS policy depende de visibilidade das consultas e não impede todo tráfego a IP obtido fora desse fluxo. Exceções exigem responsável e prazo.

## Como verificar
Teste consulta, resposta, TTL e conexão direta ao IP para revelar bypasses. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cilium-network-policy-observar-policy-verdicts-e-hubble]] — Complementa o tópico com cilium network policies: observar policy verdicts e hubble.

## Fontes
- [Cilium — Network policy introduction](https://docs.cilium.io/en/stable/security/policy/intro/) — documentação oficial de modelo de policy, selectors e enforcement/default-deny; consultado em 2026-10-04.
- [Cilium — L3 policy](https://docs.cilium.io/en/stable/security/policy/layer3/) — guia oficial de regras L3, endpoint selectors, entities, CIDR e DNS; consultado em 2026-10-04.
