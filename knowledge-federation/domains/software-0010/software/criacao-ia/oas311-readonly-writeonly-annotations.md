---
id: software.criacao_ia.tranche03.000300
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#validating-readonly-and-writeonly", "https://json-schema.org/draft/2020-12/json-schema-validation"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: validar readOnly e writeOnly conforme direção da mensagem

## Em uma frase
Em OAS 3.1.1, `readOnly` e `writeOnly` são annotations; JSON Schema não sabe por si só se está validando request ou response.

## Por que importa
Reusar um único modelo para entrada e saída é comum, mas um validador JSON Schema puro não tem contexto da direção HTTP para aplicar essas anotações. Tratar `readOnly` como exclusão automática do schema ou `writeOnly` como erro universal pode divergir entre geradores, clients e servidores.

## Como funciona
OAS 3.1.1 permite validação estendida que considera annotation, direção de leitura/escrita e valor atual. A autoridade do recurso pode ignorar um campo read-only ou tratá-lo como erro; a especificação observa que essa semântica difere da versão 3.0. Mantenha constraints estruturais em JSON Schema e implemente regra direcional explicitamente no validador de request/response quando ela for requisito.

## Exemplo
Um campo de auditoria marcado `readOnly: true` pode aparecer em resposta e ser ignorado ou rejeitado numa request PUT, conforme regra da API. Um schema reutilizado não deve levar um validator sem contexto a remover a propriedade silenciosamente antes de comparar o payload.

## Limites e trade-offs
`readOnly` e `writeOnly` não garantem criptografia, ocultação de dados nem remoção pelo servidor. Diferentes consumers podem mostrar as annotations na documentação sem usá-las durante runtime; valide os comportamentos das ferramentas escolhidas.

## Como verificar
Teste o mesmo payload nos fluxos de request e response, com readOnly e writeOnly, em gerador, validator e implementação. Confirme a política de campo obrigatório em cada direção e documente se o serviço ignora, rejeita ou emite o valor.

## Conexões
- [[oas311-path-item-ref-conflitos]] — OAS 3.1.1 Path Item `$ref`: não sobrepor fields com o alvo.

## Fontes
- [OpenAPI Specification v3.1.1 — Validating readOnly and writeOnly](https://spec.openapis.org/oas/v3.1.1.html#validating-readonly-and-writeonly) — define keywords como annotations, validação opcional contextual e diferença em relação a 3.0 Consulta: 2026-10-04.
- [JSON Schema Validation Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation) — define readOnly/writeOnly no vocabulário de validation e o papel de annotations Consulta: 2026-10-04.
