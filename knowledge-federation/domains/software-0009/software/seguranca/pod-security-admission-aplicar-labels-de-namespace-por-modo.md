---
id: software.seguranca.tranche19.001852
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

# Kubernetes Pod Security Admission: Aplicar labels de namespace por modo

## Em uma frase
**Kubernetes Pod Security Admission — Aplicar labels de namespace por modo:** Labels `enforce`, `audit` e `warn` definem como admission trata violações em pods novos ou atualizados.

## Por que importa
O recorte de **aplicar labels de namespace por modo** ajuda a definir guardrails padronizados contra configurações inseguras de pods no momento da admissão. A equipe registra risco, evidência e responsável.

## Como funciona
Para **aplicar labels de namespace por modo**, labels de namespace selecionam nível, modo enforce/audit/warn e versão do padrão que o admission verifica. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Ative warn e audit em namespace piloto antes de escolher enforce para aplicações existentes. Teste em staging autorizado.

## Limites e trade-offs
Label mal escrita ou aplicada ao namespace errado deixa proteção diferente da esperada. Exceções exigem responsável e prazo.

## Como verificar
Leia labels efetivas e envie um pod canário que viole o nível selecionado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[pod-security-admission-fixar-versao-do-padrao]] — Complementa o tópico com kubernetes pod security admission: fixar versão do padrão.

## Fontes
- [Kubernetes — Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) — guia oficial do admission controller, labels, modos e exceções; consultado em 2026-10-04.
- [Kubernetes — Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) — definições oficiais dos níveis privileged, baseline e restricted; consultado em 2026-10-04.
