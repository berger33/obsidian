---
id: software.seguranca.tranche19.001859
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

# Kubernetes Pod Security Admission: Observar audit events

## Em uma frase
**Kubernetes Pod Security Admission — Observar audit events:** Audit mode registra violações sem bloquear para apoiar migração e monitoramento de mudanças.

## Por que importa
O recorte de **observar audit events** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **observar audit events**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Colete eventos de audit de namespace canário e encaminhe-os à equipe responsável por workloads. Teste em staging autorizado.

## Limites e trade-offs
Evento não significa que o pod foi bloqueado nem que alguém corrigirá a configuração. Exceções exigem responsável e prazo.

## Como verificar
Crie violação intencional e confirme registro, identidade do ator e namespace. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-coordenar-upgrade-do-cluster-e-politicas]] — Complementa o tópico com kubernetes pod security admission: coordenar upgrade do cluster e políticas.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
