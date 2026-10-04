---
id: software.seguranca.tranche19.001869
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
fontes: ["https://kubernetes.io/docs/concepts/services-networking/network-policies/", "https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kubernetes NetworkPolicy: Tratar endereços IP e mudanças de serviço

## Em uma frase
**Kubernetes NetworkPolicy — Tratar endereços IP e mudanças de serviço:** Regras por CIDR são sensíveis a mudanças de rede, NAT e endereços que podem ser dinâmicos.

## Por que importa
O recorte de **tratar endereços ip e mudanças de serviço** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **tratar endereços ip e mudanças de serviço**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use selectors de pods para comunicação interna estável e documente CIDRs externos inevitáveis. Teste em staging autorizado.

## Limites e trade-offs
CIDR antigo pode deixar conexão indisponível ou permitir faixa maior do que a esperada. Exceções exigem responsável e prazo.

## Como verificar
Teste do pod efetivo, incluindo caminho de NAT e DNS do ambiente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-validar-trafego-com-testes-de-integracao]] — Complementa o tópico com kubernetes networkpolicy: validar tráfego com testes de integração.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
