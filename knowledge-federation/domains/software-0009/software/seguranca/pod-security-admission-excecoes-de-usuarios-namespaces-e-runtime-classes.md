---
id: software.seguranca.tranche19.001856
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

# Kubernetes Pod Security Admission: Exceções de usuários, namespaces e runtime classes

## Em uma frase
**Kubernetes Pod Security Admission — Exceções de usuários, namespaces e runtime classes:** Exemptions podem excluir sujeitos ou recursos específicos e são configuradas no admission control do cluster.

## Por que importa
O recorte de **exceções de usuários, namespaces e runtime classes** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exceções de usuários, namespaces e runtime classes**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Se exceção for indispensável, limite-a a identidade e namespace documentados em laboratório. Teste em staging autorizado.

## Limites e trade-offs
Exemption ampla reduz controle sem necessariamente aparecer nas labels do namespace. Exceções exigem responsável e prazo.

## Como verificar
Audite configuração do API server e inventarie cada exceção com responsável e prazo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-hardening-do-securitycontext]] — Complementa o tópico com kubernetes pod security admission: hardening do securitycontext.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
