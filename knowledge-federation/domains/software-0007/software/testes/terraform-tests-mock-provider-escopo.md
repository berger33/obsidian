---
id: software.testes.tranche08.000191
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developer.hashicorp.com/terraform/language/tests/mocking", "https://developer.hashicorp.com/terraform/language/tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terraform: delimitar mocks de provider

## Em uma frase
Use mock_provider para verificar composição e assertions sem provisionar cloud, mas não trate valores simulados como prova de comportamento real.

## Por que importa
Mocks reduzem custo e tornam testes determinísticos, enquanto diferenças de API, permissões e valores calculados podem existir no provider real.

## Como funciona
Defina valores mockados necessários e mantenha fixtures pequenas. Reserve integração controlada para invariantes que dependem do provider, API ou estado de infraestrutura.

## Exemplo
Um módulo verifica que output deriva de inputs esperados com provider mockado; pipeline separada confirma criação em sandbox quando requisito envolve API real.

## Limites e trade-offs
Mocks podem atribuir atributos que provider real não retornaria ou não validar schema externo; evite fixtures irreais e claims de compatibilidade.

## Como verificar
Compare campos mockados com documentação do provider e execute um cenário real em ambiente isolado para contratos críticos.

## Conexões
- [[terraform-data-sources-outputs-mock-real]] — Veja também: Terraform: testar data sources e outputs calculados.
- [[terraform-test-run-apply-cleanup]] — Veja também: Terraform: isolar testes que aplicam infraestrutura.

## Fontes
- [Terraform — Mocking](https://developer.hashicorp.com/terraform/language/tests/mocking) — mock_provider, valores computados e overrides; consultado em 2026-10-02.
- [Terraform — Tests](https://developer.hashicorp.com/terraform/language/tests) — run blocks, asserts, plan/apply e provider configuration; consultado em 2026-10-02.
