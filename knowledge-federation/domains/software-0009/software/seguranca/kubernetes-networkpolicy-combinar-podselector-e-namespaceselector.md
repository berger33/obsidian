---
id: software.seguranca.tranche19.001865
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

# Kubernetes NetworkPolicy: Combinar podSelector e namespaceSelector

## Em uma frase
**Kubernetes NetworkPolicy — Combinar podSelector e namespaceSelector:** Seletores no mesmo peer podem restringir namespace e pods simultaneamente; seletores separados podem representar alternativas.

## Por que importa
O recorte de **combinar podselector e namespaceselector** ajuda a segmentar comunicação entre workloads Kubernetes e aplicar padrões de allowlist revisados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **combinar podselector e namespaceselector**, policies selecionam pods por namespace e labels; regras ingress/egress são combinadas de forma aditiva pelo plugin de rede. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita apenas pods `api` no namespace `backend` usando seletor combinado de teste. Teste em staging autorizado.

## Limites e trade-offs
YAML com `from`/`to` em forma incorreta pode autorizar namespace mais amplo. Exceções exigem responsável e prazo.

## Como verificar
Use casos de pod certo/namespace errado e namespace certo/pod errado para validar conjunção. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-restringir-portas-e-protocolos]] — Complementa o tópico com kubernetes networkpolicy: restringir portas e protocolos.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — guia oficial de seletores, ingress/egress, default deny e implementação; consultado em 2026-10-04.
- [Kubernetes — NetworkPolicy API](https://kubernetes.io/docs/reference/kubernetes-api/networking/network-policy-v1/) — referência oficial de campos e semântica da API NetworkPolicy v1; consultado em 2026-10-04.
