---
id: software.seguranca.tranche19.001870
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

# Kubernetes NetworkPolicy: Validar tráfego com testes de integração

## Em uma frase
**Kubernetes NetworkPolicy — Validar tráfego com testes de integração:** Teste funcional de rede confirma efeito real da policy com CNI, labels e pods em execução.

## Por que importa
O recorte de **validar tráfego com testes de integração** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **validar tráfego com testes de integração**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Inclua probe de cliente para destino permitido e negado no pipeline de staging. Teste em staging autorizado.

## Limites e trade-offs
YAML válido e objeto `kubectl get` não demonstram enforcement do plano de dados. Exceções exigem responsável e prazo.

## Como verificar
Guarde resultado, CNI e labels dos pods e repita após mudança de versão do cluster. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-definir-constrainttemplate]] — Complementa o tópico com opa gatekeeper: definir constrainttemplate.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
