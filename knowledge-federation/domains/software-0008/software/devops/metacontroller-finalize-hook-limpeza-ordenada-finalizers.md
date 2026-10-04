---
id: software.devops.tranche18.001775
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

# Metacontroller `finalize` hook: gerenciamento declarativo de Finalizers e limpeza antes da exclusão

## Em uma frase
Tanto o `CompositeController` quanto o `DecoratorController` suportam o hook **`finalize`** (`spec.hooks.finalize`), que adiciona automaticamente um `finalizer` do Metacontroller nos objetos gerenciados e chama o seu webhook durante o processo de exclusão até que o hook retorne `"finalized": true`.

## Por que importa
Às vezes, apagar os recursos filhos via Garbage Collection padrão do Kubernetes não basta: é preciso desregistrar o nó de um balanceador externo, esvaziar um bucket ou deletar os filhos em uma ordem estrita (primeiro os `Pods`, e só quando não restar nenhum Pod deletar o `ConfigMap`).

## Como funciona
Quando um objeto pai possui `hooks.finalize` configurado e recebe `kubectl delete` (ganhando `metadata.deletionTimestamp`), o Metacontroller passa a invocar o webhook `finalize` (ou o próprio `sync` com `"finalizing": true`). O webhook pode retornar estados intermediários de `children` para desligar recursos em etapas e, quando a limpeza terminar, retorna `{"finalized": true}`, momento em que o Metacontroller remove o finalizer.

## Exemplo
```yaml
  hooks:
    sync:
      webhook:
        url: http://my-controller.metacontroller/sync
    finalize:
      webhook:
        url: http://my-controller.metacontroller/finalize
```

## Limites e trade-offs
Enquanto o webhook `finalize` retornar `"finalized": false` (ou falhar com erro HTTP), o objeto permanecerá em estado `Terminating` protegido contra remoção do `etcd`.

## Como verificar
Delete um recurso gerenciado por um controlador com hook `finalize` e confirme nos logs que o finalizer só é removido após o retorno de `"finalized": true`.

## Conexões
- [[metacontroller-contrato-sync-webhook-request-response-json]] — Veja também: Metacontroller: contrato JSON de entrada e saída do webhook `sync` para reconciliação declarativa.
- [[metacontroller-customize-hook-related-resources-contexto-adicional]] — Veja também: Metacontroller `customize` hook: busca declarativa de `relatedResources` para enriquecer o contexto do `sync`.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://metacontroller.github.io/metacontroller/concepts.html) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
