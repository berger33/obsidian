---
id: software.seguranca.tranche19.001867
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

# Kubernetes NetworkPolicy: Confirmar suporte do CNI

## Em uma frase
**Kubernetes NetworkPolicy — Confirmar suporte do CNI:** NetworkPolicy é API declarativa e precisa ser implementada pelo plugin de rede do cluster para ter efeito.

## Por que importa
O recorte de **confirmar suporte do cni** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **confirmar suporte do cni**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Antes de depender do gate, valide a CNI instalada em cluster descartável com teste de bloqueio. Teste em staging autorizado.

## Limites e trade-offs
Objeto NetworkPolicy aceito pelo API server pode não aplicar política se CNI ignorar o recurso. Exceções exigem responsável e prazo.

## Como verificar
Crie duas pods, aplique deny policy e prove bloqueio com teste de conectividade. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-planejar-politica-default-deny-por-namespace]] — Complementa o tópico com kubernetes networkpolicy: planejar política default-deny por namespace.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
