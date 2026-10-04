---
id: software.seguranca.tranche19.001853
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
fontes: ["https://kubernetes.io/docs/concepts/security/pod-security-admission/", "https://kubernetes.io/docs/concepts/security/pod-security-standards/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kubernetes Pod Security Admission: Fixar versão do padrão

## Em uma frase
**Kubernetes Pod Security Admission — Fixar versão do padrão:** Labels de versão podem fixar comportamento do Pod Security Standard à versão de Kubernetes escolhida.

## Por que importa
O recorte de **fixar versão do padrão** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **fixar versão do padrão**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Declare `pod-security.kubernetes.io/enforce-version` durante upgrade planejado do cluster. Teste em staging autorizado.

## Limites e trade-offs
Usar `latest` pode mudar regras após upgrade do servidor sem revisão de workload. Exceções exigem responsável e prazo.

## Como verificar
Compare resultado do pod canário contra versão do padrão registrada no namespace. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-migrar-de-warn-para-enforce]] — Complementa o tópico com kubernetes pod security admission: migrar de warn para enforce.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
