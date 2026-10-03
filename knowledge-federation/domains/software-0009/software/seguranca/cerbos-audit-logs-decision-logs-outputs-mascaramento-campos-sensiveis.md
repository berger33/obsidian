---
id: software.seguranca.tranche01.000089
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos Decision Audit Logs e Policy Outputs: trilha de auditoria de decisões e retorno de obrigações/máscaras para a aplicação

## Em uma frase
O Cerbos possui dois recursos fundamentais para governança, conformidade (SOC 2, ISO 27001, HIPAA) e controle fino na aplicação: **Audit Logs** (`audit:` no `.cerbos.yaml`, que registra `accessLogs` e `decisionLogs` completos de quem pediu o quê, com quais atributos e qual regra decidiu) e **Policy Outputs (`output:`)** (expressões CEL que retornam dados estruturados junto com a decisão).

## Por que importa
Às vezes uma regra não é apenas binária (`ALLOW`/`DENY`): por exemplo, "permita `view` no registro do funcionário, mas retorne um `output` instruindo o backend a mascarar o campo `salary`, ou informe ao frontend exatamente o motivo pelo qual a aprovação foi negada".

## Como funciona
No bloco `output.when` de uma regra (`ruleActivated` ou `conditionNotMet`), você define uma expressão CEL cujos resultados são devolvidos no array `outputs[]` da resposta do `CheckResources`, enquanto o subsistema `audit` grava os logs de decisão em `file`, `local` (BadgerDB) ou `kafka` com suporte a exclusão de campos sensíveis (`excludeKeys`).

## Exemplo
```yaml
audit:
  enabled: true
  accessLogsEnabled: true
  decisionLogsEnabled: true
  backend: file
  file:
    path: stdout
```

## Limites e trade-offs
Use a opção de filtragem de campos do Audit Log para excluir tokens ou dados pessoais sensíveis de `auxData` antes de enviar os `decisionLogs` para o SIEM.

## Como verificar
Verifique no JSON de saída do `CheckResources` o array `outputs` quando uma regra com `output:` é acionada.

## Conexões
- [[cerbos-auxdata-jwt-verificacao-claims-contexto-criptografico]] — Veja também: Cerbos `auxData` e Verificação Nativa de JWT: uso de claims autenticadas do token diretamente nas expressões de política.
- [[cerbos-implantacao-kubernetes-sidecar-vs-service-storage-git-blob-disk]] — Veja também: Cerbos Topologias de Deploy e Storage Drivers: `sidecar` vs `service` no Kubernetes e sincronização via `git`, `blob` ou `disk`.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
