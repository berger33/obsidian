---
id: software.devops.tranche18.001777
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://metacontroller.github.io/metacontroller/concepts.html", "https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md", "https://github.com/metacontroller/metacontroller"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Metacontroller: estratégias de atualização de recursos filhos (`OnDelete`, `Recreate`, `InPlace`, `RollingRecreate`, `RollingInPlace`)

## Em uma frase
Para cada tipo de recurso filho (`childResources` ou `attachments`), o Metacontroller exige declarar uma `updateStrategy.method` explícita (`OnDelete`, `Recreate`, `InPlace`, `RollingRecreate` ou `RollingInPlace`) que define como alterações retornadas pelo webhook serão aplicadas.

## Por que importa
Certos objetos Kubernetes permitem atualização in-place via merge patch (`Deployment`, `Service`), enquanto outros possuem campos imutáveis que exigem deletar e recriar o objeto (`Job`, `Pod`) ou precisam de atualização gradual respeitando verificações de saúde (`statusChecks`).

## Como funciona
Por padrão, se nenhuma estratégia for informada, o Metacontroller usa `OnDelete` (não modifica filhos existentes até serem deletados). Ao configurar `method: InPlace`, o Metacontroller aplica um patch direto no objeto existente; ao configurar `method: Recreate`, ele deleta e recria o filho quando o template desejado difere do estado atual.

## Exemplo
```yaml
  childResources:
    - apiVersion: batch/v1
      resource: jobs
      updateStrategy:
        method: Recreate
    - apiVersion: v1
      resource: configmaps
      updateStrategy:
        method: InPlace
```

## Limites e trade-offs
Esquecer de definir `updateStrategy: {method: InPlace}` em um recurso filho como `Deployment` ou `ConfigMap` é a armadilha mais comum ao iniciar com Metacontroller, pois no padrão `OnDelete` mudanças no pai não atualizarão o filho existente.

## Como verificar
Verifique a seção `childResources` do seu `CompositeController` e confirme que todos os recursos mutáveis possuem `method: InPlace` (ou `Recreate` para Jobs/Pods).

## Conexões
- [[metacontroller-customize-hook-related-resources-contexto-adicional]] — Veja também: Metacontroller `customize` hook: busca declarativa de `relatedResources` para enriquecer o contexto do `sync`.
- [[metacontroller-generateselector-labelselector-adopt-orphan-semantics]] — Veja também: Metacontroller: seleção de filhos com `generateSelector: true` vs `labelSelector` customizado e semântica de adoção.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://metacontroller.github.io/metacontroller/concepts.html) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
