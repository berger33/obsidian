---
id: software.seguranca.tranche17.001642
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

# Open Policy Agent (OPA): Separação entre input e data

## Em uma frase
**Open Policy Agent (OPA) — Separação entre input e data:** O input representa a requisição avaliada, enquanto data pode carregar fatos e estruturas disponibilizados à política.

## Por que importa
O recorte de **separação entre input e data** ajuda a separar regras de autorização e conformidade da lógica de aplicação e testá-las de forma reproduzível. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separação entre input e data**, a aplicação fornece input e dados de contexto; regras Rego produzem uma decisão que o consumidor precisa interpretar e aplicar. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Passe identidade e ação no input e mantenha catálogo de papéis em data em um exemplo de teste. Teste em staging autorizado.

## Limites e trade-offs
Misturar request transitório e dados de referência dificulta auditoria e pode introduzir estado desatualizado. Exceções exigem responsável e prazo.

## Como verificar
Valide schema e origem de cada documento e teste atualizações no conjunto de data. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[opa-consulta-local-com-opa-eval]] — Complementa o tópico com open policy agent (opa): consulta local com `opa eval`.

## Fontes
- [Open Policy Agent — Documentation](https://www.openpolicyagent.org/docs/latest/) — documentação oficial do motor e das integrações de política; consultado em 2026-10-04.
- [Open Policy Agent — Policy Language](https://www.openpolicyagent.org/docs/latest/policy-language/) — referência oficial sobre módulos, regras e linguagem Rego; consultado em 2026-10-04.
