---
id: software.seguranca.tranche17.001650
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://www.openpolicyagent.org/docs/latest/", "https://www.openpolicyagent.org/docs/latest/policy-language/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Open Policy Agent (OPA): Cobertura de regras e cenários negativos

## Em uma frase
**Open Policy Agent (OPA) — Cobertura de regras e cenários negativos:** Cobertura mostra quais regras foram exercitadas, mas precisa ser interpretada junto a cenários de ameaça e requisitos.

## Por que importa
O recorte de **cobertura de regras e cenários negativos** ajuda a separar regras de autorização e conformidade da lógica de aplicação e testá-las de forma reproduzível. A equipe registra risco, evidência e responsável.

## Como funciona
Para **cobertura de regras e cenários negativos**, a aplicação fornece input e dados de contexto; regras Rego produzem uma decisão que o consumidor precisa interpretar e aplicar. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute a suíte com cobertura e adicione fixture que exercita cada negação crítica de acesso. Teste em staging autorizado.

## Limites e trade-offs
Linha coberta não significa que a condição seja testada em seus limites nem que a política seja segura. Exceções exigem responsável e prazo.

## Como verificar
Combine cobertura com revisão de requisitos, entradas adversariais e testes de integração. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-validacao-de-recursos-no-admission]] — Complementa o tópico com kyverno: validação de recursos no admission.

## Fontes
- [Open Policy Agent — Documentation](https://www.openpolicyagent.org/docs/latest/) — documentação oficial do motor e das integrações de política; consultado em 2026-10-04.
- [Open Policy Agent — Policy Language](https://www.openpolicyagent.org/docs/latest/policy-language/) — referência oficial sobre módulos, regras e linguagem Rego; consultado em 2026-10-04.
