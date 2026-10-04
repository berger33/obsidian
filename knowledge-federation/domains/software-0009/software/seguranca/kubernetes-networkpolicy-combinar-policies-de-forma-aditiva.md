---
id: software.seguranca.tranche19.001864
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

# Kubernetes NetworkPolicy: Combinar policies de forma aditiva

## Em uma frase
**Kubernetes NetworkPolicy — Combinar policies de forma aditiva:** Regras de allow de múltiplas policies aplicáveis são combinadas, não ordenadas como firewall sequencial.

## Por que importa
O recorte de **combinar policies de forma aditiva** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **combinar policies de forma aditiva**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Divida acesso por finalidade em policies pequenas e avalie a união das permissões. Teste em staging autorizado.

## Limites e trade-offs
Uma policy adicional ampla pode reabrir tráfego bloqueado por outra regra. Exceções exigem responsável e prazo.

## Como verificar
Inspecione todas as policies que selecionam pod e teste fluxo através de cada combinação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-combinar-podselector-e-namespaceselector]] — Complementa o tópico com kubernetes networkpolicy: combinar podselector e namespaceselector.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
