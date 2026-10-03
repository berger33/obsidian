---
id: software.devops.tranche16.001518
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
fontes: ["https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: políticas de propriedade (`kapp.k14s.io/exists` e `kapp.k14s.io/noop`) para recursos compartilhados

## Em uma frase
O `kapp` protege contra conflitos de propriedade entre múltiplas aplicações no mesmo cluster e oferece as anotações `kapp.k14s.io/exists` e `kapp.k14s.io/noop` para lidar com recursos compartilhados (como um `Namespace` comum ou CRDs globais).

## Por que importa
Se duas aplicações gerenciadas pelo `kapp` incluírem a definição do mesmo `Namespace` ou do mesmo `CustomResourceDefinition`, a segunda aplicação falhará por padrão ao detectar que o recurso já pertence ao label da primeira aplicação (E se uma delas for deletada com `kapp delete`, ela tentaria apagar o recurso compartilhado).

## Como funciona
A anotação `kapp.k14s.io/exists: ""` instrui o `kapp` a criar o recurso apenas se ele ainda não existir no cluster e a não assumir propriedade exclusiva sobre ele (exibindo `exists` na coluna `Op` da tabela de diff), além de combiná-la com `kapp.k14s.io/delete-strategy: orphan` para nunca removê-lo no `kapp delete`. Já `kapp.k14s.io/noop: ""` faz o `kapp` ignorar completamente o recurso durante o deploy.

## Exemplo
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: shared-platform
  annotations:
    kapp.k14s.io/exists: ""
    kapp.k14s.io/delete-strategy: orphan
```

## Limites e trade-offs
Sem `kapp.k14s.io/delete-strategy: orphan`, deletar a aplicação que originalmente criou o `Namespace` compartilhado acionaria a exclusão em cascata de todos os recursos de outras equipes dentro daquele namespace.

## Como verificar
Execute `kapp deploy -a app-a -f ns.yml --diff-run` contra um namespace já existente e confirme que a operação planejada na coluna `Op` é `exists` (ou vazia) sem erro de conflito de ownership.

## Conexões
- [[carvel-kapp-update-strategies-fallback-on-replace-always-replace]] — Veja também: Carvel kapp: estratégias de atualização (`update-strategy`) para campos imutáveis em Jobs e Services.
- [[carvel-kapp-operacao-sem-privilegios-admin-single-namespace-rbac]] — Veja também: Carvel kapp: operação sem privilégios de cluster-admin e escopo de namespace único (`-n`).

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
