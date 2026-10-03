---
id: software.seguranca.tranche01.000082
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
fontes: ["https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos Taxonomia das 6 Políticas: `Resource Policies`, `Derived Roles`, `Principal Policies`, `Role Policies`, `Exported Variables` e `Constants`

## Em uma frase
Conforme documentado na página oficial *Cerbos policies* (`docs.cerbos.dev/cerbos/latest/policies/`), o Cerbos organiza o controle de acesso em **seis tipos de políticas YAML**: **Resource policies**, **Derived roles**, **Principal policies**, **Role policies**, **Exported variables** e **Exported constants**.

## Por que importa
Tentar expressar todas as regras da empresa em um único formato rígido mistura regras gerais de recursos com exceções temporárias de usuários específicos e constantes compartilhadas.

## Como funciona
Cada um dos 6 tipos resolve uma necessidade precisa: 1) **`resourcePolicy`** define as regras para ações (`view`, `edit`, `delete`) sobre um tipo de recurso (`album:object`, `expense:report`); 2) **`derivedRoles`** amplia papéis amplos de RBAC com contexto em tempo de execução (ex.: `manager` -> `manager_of_scranton_branch`); 3) **`principalPolicy`** define overrides específicos para um único usuário/bot; 4) **`rolePolicy`** define listas de ações permitidas para um papel específico; e 5) **`exportVariables`** / 6) **`exportConstants`** centralizam expressões e constantes reutilizáveis entre múltiplas políticas!

## Exemplo
```yaml
apiVersion: api.cerbos.dev/v1
exportVariables:
  name: common_checks
  definitions:
    is_same_department: request.principal.attr.department == request.resource.attr.department
```

## Limites e trade-offs
Importe variáveis e constantes compartilhadas usando `importVariables` e `importConstants` nas suas `resourcePolicy` para evitar repetição de expressões CEL em dezenas de arquivos.

## Como verificar
Valide todos os 6 tipos de política do diretório executando `cerbos compile ./policies`.

## Conexões
- [[cerbos-arquitetura-stateless-pdp-pbac-abac-rbac-cloud-native]] — Veja também: Cerbos: arquitetura do Policy Decision Point (`PDP`) stateless para autorização PBAC/ABAC/RBAC declarativa em YAML.
- [[cerbos-derived-roles-evolucao-rbac-para-abac-condicoes-cel]] — Veja também: Cerbos `Derived Roles`: evolução limpa de RBAC estático para ABAC contextual usando expressões CEL.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
