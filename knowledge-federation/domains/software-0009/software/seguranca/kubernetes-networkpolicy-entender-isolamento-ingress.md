---
id: software.seguranca.tranche19.001862
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

# Kubernetes NetworkPolicy: Entender isolamento ingress

## Em uma frase
**Kubernetes NetworkPolicy — Entender isolamento ingress:** Ao selecionar um pod para ingress, policy passa a restringir conexões de entrada segundo regras permitidas.

## Por que importa
O recorte de **entender isolamento ingress** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **entender isolamento ingress**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie policy ingress default-deny em namespace de teste e permita apenas chamada do frontend autorizado. Teste em staging autorizado.

## Limites e trade-offs
Policy sem allow correspondente pode interromper health checks ou acesso de operação. Exceções exigem responsável e prazo.

## Como verificar
Teste conexões de origem autorizada e negada em pods distintos. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-entender-isolamento-egress]] — Complementa o tópico com kubernetes networkpolicy: entender isolamento egress.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
