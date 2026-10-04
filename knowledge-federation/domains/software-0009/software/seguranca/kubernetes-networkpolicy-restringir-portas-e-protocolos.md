---
id: software.seguranca.tranche19.001866
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

# Kubernetes NetworkPolicy: Restringir portas e protocolos

## Em uma frase
**Kubernetes NetworkPolicy — Restringir portas e protocolos:** Rules podem limitar tráfego por protocolo e número ou nome de porta conforme o tipo de destino.

## Por que importa
O recorte de **restringir portas e protocolos** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **restringir portas e protocolos**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita TCP na porta do serviço necessária e negue conexão a outra porta no mesmo pod. Teste em staging autorizado.

## Limites e trade-offs
Port name ou protocolo omitido pode não coincidir com portas reais do container. Exceções exigem responsável e prazo.

## Como verificar
Confirme portas declaradas e teste conexão em porta autorizada e não autorizada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-confirmar-suporte-do-cni]] — Complementa o tópico com kubernetes networkpolicy: confirmar suporte do cni.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
