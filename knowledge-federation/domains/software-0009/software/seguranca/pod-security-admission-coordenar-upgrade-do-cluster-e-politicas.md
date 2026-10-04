---
id: software.seguranca.tranche19.001860
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

# Kubernetes Pod Security Admission: Coordenar upgrade do cluster e políticas

## Em uma frase
**Kubernetes Pod Security Admission — Coordenar upgrade do cluster e políticas:** Versão do padrão, API server e workloads precisam ser revisados em conjunto durante upgrade.

## Por que importa
O recorte de **coordenar upgrade do cluster e políticas** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **coordenar upgrade do cluster e políticas**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute avaliação de versão alvo em branch de migração antes de atualizar namespace para o novo padrão. Teste em staging autorizado.

## Limites e trade-offs
Mudança de comportamento do control plane pode aumentar violações em rollouts futuros. Exceções exigem responsável e prazo.

## Como verificar
Compare resultado pré e pós-upgrade com os mesmos manifests e documente diferenças. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubernetes-networkpolicy-selecionar-pods-protegidos]] — Complementa o tópico com kubernetes networkpolicy: selecionar pods protegidos.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
