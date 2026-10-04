---
id: software.seguranca.tranche19.001858
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

# Kubernetes Pod Security Admission: Revisar mutações de admission

## Em uma frase
**Kubernetes Pod Security Admission — Revisar mutações de admission:** Mutating webhooks podem alterar pod antes de validação ou criar configurações diferentes do source manifest.

## Por que importa
O recorte de **revisar mutações de admission** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **revisar mutações de admission**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Compare objeto enviado e objeto admitido em namespace de staging com webhook habilitado. Teste em staging autorizado.

## Limites e trade-offs
Confiar apenas no YAML original perde visibilidade sobre mudanças feitas no cluster. Exceções exigem responsável e prazo.

## Como verificar
Capture objeto após admission e confirme que política aplicada corresponde ao resultado final. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-observar-audit-events]] — Complementa o tópico com kubernetes pod security admission: observar audit events.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
