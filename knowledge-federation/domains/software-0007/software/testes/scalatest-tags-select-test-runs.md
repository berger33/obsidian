---
id: software.testes.tranche13.000713
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://www.scalatest.org/user_guide/tagging_your_tests", "https://www.scalatest.org/user_guide/running_your_tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ScalaTest: filtrar testes por tags declaradas

## Em uma frase
Tags classificam testes e runners permitem incluir ou excluir grupos durante a execução.

## Por que importa
Uma taxonomia consistente separa rápido, integração e acesso externo sem manter listas manuais de nomes que envelhecem.

## Como funciona
Declare tags perto do suite ou caso segundo a API, configure filtros do runner e registre no job quais categorias foram incluídas e removidas.

## Exemplo
A pipeline de PR pode excluir testes `Slow` enquanto um job noturno inclui esses casos além da categoria padrão.

## Limites e trade-offs
Filtro vazio ou rótulo digitado errado pode deixar job sem cobertura; a execução precisa conferir quantidade de testes selecionados.

## Como verificar
Teste filtros include e exclude em suite pequena e confirme no relatório quais tags efetivamente selecionaram exemplos.

## Conexões
- [[scalatest-assertion-clue]] — Veja também: ScalaTest: acrescentar contexto à falha de assertion.
- [[scalatest-runner-entrypoints]] — Veja também: ScalaTest: manter runner alinhado ao build.

## Fontes
- [ScalaTest — Tagging Tests](https://www.scalatest.org/user_guide/tagging_your_tests) — tag declarations and filtering; consultado em 2026-10-02.
- [ScalaTest — Running Tests](https://www.scalatest.org/user_guide/running_your_tests) — runner integrations and execution options; consultado em 2026-10-02.
