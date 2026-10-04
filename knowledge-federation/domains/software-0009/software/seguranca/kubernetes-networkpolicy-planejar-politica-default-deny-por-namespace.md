---
id: software.seguranca.tranche19.001868
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

# Kubernetes NetworkPolicy: Planejar política default-deny por namespace

## Em uma frase
**Kubernetes NetworkPolicy — Planejar política default-deny por namespace:** Uma policy com selector adequado e regras vazias pode introduzir isolamento para todos os pods selecionados.

## Por que importa
O recorte de **planejar política default-deny por namespace** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **planejar política default-deny por namespace**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Implante primeiro allowlists mínimas em namespace canário e só depois habilite deny. Teste em staging autorizado.

## Limites e trade-offs
Policy ampla pode cortar tráfego de controladores e serviços compartilhados. Exceções exigem responsável e prazo.

## Como verificar
Faça inventário de fluxo e teste rollout com rollback antes de expandir namespaces. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-tratar-enderecos-ip-e-mudancas-de-servico]] — Complementa o tópico com kubernetes networkpolicy: tratar endereços ip e mudanças de serviço.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
