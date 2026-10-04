---
id: software.seguranca.tranche19.001854
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

# Kubernetes Pod Security Admission: Migrar de warn para enforce

## Em uma frase
**Kubernetes Pod Security Admission — Migrar de warn para enforce:** Modos de audit e warn ajudam encontrar violações antes de bloquear admissões.

## Por que importa
O recorte de **migrar de warn para enforce** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **migrar de warn para enforce**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Colete warnings de deployments de staging e corrija cada manifesto antes da mudança para enforce. Teste em staging autorizado.

## Limites e trade-offs
Warnings ignorados viram bloqueios em rollout futuro, inclusive em réplicas substituídas. Exceções exigem responsável e prazo.

## Como verificar
Monitore eventos de deploy e confirme que controller consegue criar pod novo após enforcement. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-entender-escopo-das-verificacoes]] — Complementa o tópico com kubernetes pod security admission: entender escopo das verificações.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
