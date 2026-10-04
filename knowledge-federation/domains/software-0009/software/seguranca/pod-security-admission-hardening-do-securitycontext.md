---
id: software.seguranca.tranche19.001857
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

# Kubernetes Pod Security Admission: Hardening do securityContext

## Em uma frase
**Kubernetes Pod Security Admission — Hardening do securityContext:** O nível restricted exige controles como usuário não-root, capabilities limitadas e perfil de seccomp compatível.

## Por que importa
O recorte de **hardening do securitycontext** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **hardening do securitycontext**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Adicione securityContext ao pod de teste e valide que container inicia sob política restricted. Teste em staging autorizado.

## Limites e trade-offs
Uma configuração pode atender admission e ainda conter vulnerabilidade na aplicação. Exceções exigem responsável e prazo.

## Como verificar
Examine securityContext do pod efetivo e faça teste funcional sem privilégios. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-revisar-mutacoes-de-admission]] — Complementa o tópico com kubernetes pod security admission: revisar mutações de admission.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
