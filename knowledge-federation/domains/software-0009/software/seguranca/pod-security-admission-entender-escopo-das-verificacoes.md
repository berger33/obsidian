---
id: software.seguranca.tranche19.001855
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

# Kubernetes Pod Security Admission: Entender escopo das verificações

## Em uma frase
**Kubernetes Pod Security Admission — Entender escopo das verificações:** PSA avalia requests de Pod e aplica o nível definido ao objeto recebido no admission.

## Por que importa
O recorte de **entender escopo das verificações** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **entender escopo das verificações**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Teste pod de Deployment em vez de validar apenas o objeto Deployment no lint local. Teste em staging autorizado.

## Limites e trade-offs
Controladores ou webhooks podem gerar pods diferentes do template originalmente revisado. Exceções exigem responsável e prazo.

## Como verificar
Inspecione Pod admitido e eventos do controller para identificar violação real. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-excecoes-de-usuarios-namespaces-e-runtime-classes]] — Complementa o tópico com kubernetes pod security admission: exceções de usuários, namespaces e runtime classes.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
