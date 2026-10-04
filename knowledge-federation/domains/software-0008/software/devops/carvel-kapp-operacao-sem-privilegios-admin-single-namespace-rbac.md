---
id: software.devops.tranche16.001519
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: operação sem privilégios de cluster-admin e escopo de namespace único (`-n`)

## Em uma frase
O `kapp` opera inteiramente como cliente usando as credenciais RBAC do próprio usuário, sem exigir CRDs administrativos nem controladores privilegiados instalados no cluster.

## Por que importa
Em ambientes corporativos multi-tenant, equipes de desenvolvimento recebem apenas uma `RoleBinding` restrita ao seu próprio namespace e não têm permissão para instalar operadores globais nem ler recursos fora de seu escopo.

## Como funciona
Ao passar `-n <meu-namespace>` para `kapp deploy -a minha-app -f manifestos.yml`, o `kapp` grava o `ConfigMap` de estado (`<minha-app>.apps.k14s.io`) dentro daquele namespace específico e restringe as buscas de recursos órfãos aos tipos de API permitidos para aquela conta de serviço (ou ajustados via `--scope-to-ns`).

## Exemplo
```bash
kapp deploy -n team-alpha -a checkout-service -f manifests/ --scope-to-ns --yes
kapp app-change list -n team-alpha -a checkout-service
```

## Limites e trade-offs
Se a aplicação incluir apenas recursos `namespaced` e o usuário não tiver permissão RBAC para listar recursos `cluster-scoped` (como `Node` ou `ClusterRole`), a flag `--scope-to-ns` evita que o `kapp` tente consultar endpoints globais durante a descoberta de recursos.

## Como verificar
Execute `kapp app-change list -n team-alpha -a checkout-service` usando um `kubeconfig` restrito ao namespace `team-alpha` e valide o registro completo de auditoria dos deploys.

## Conexões
- [[carvel-kapp-ownership-exists-noop-compartilhamento-recursos]] — Veja também: Carvel kapp: políticas de propriedade (`kapp.k14s.io/exists` e `kapp.k14s.io/noop`) para recursos compartilhados.
- [[carvel-kapp-app-group-deploy-gitops-inspecao-label-arbitrario]] — Veja também: Carvel kapp: implantação em lote via `app-group` e inspeção de recursos existentes por seletor `label:`.

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
