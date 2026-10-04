---
id: software.seguranca.tranche19.001851
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

# Kubernetes Pod Security Admission: Distinguir níveis de Pod Security

## Em uma frase
**Kubernetes Pod Security Admission — Distinguir níveis de Pod Security:** Privileged é irrestrito; baseline bloqueia elevações comuns; restricted aplica conjunto mais rigoroso de hardening.

## Por que importa
O recorte de **distinguir níveis de pod security** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **distinguir níveis de pod security**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Classifique workloads de teste por necessidade e aplique primeiro nível compatível com sua política. Teste em staging autorizado.

## Limites e trade-offs
Escolher restricted sem validar requisitos de runtime pode interromper pods legítimos. Exceções exigem responsável e prazo.

## Como verificar
Teste manifests representativos e registre exceções concretas antes de ativar enforcement. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-aplicar-labels-de-namespace-por-modo]] — Complementa o tópico com kubernetes pod security admission: aplicar labels de namespace por modo.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
