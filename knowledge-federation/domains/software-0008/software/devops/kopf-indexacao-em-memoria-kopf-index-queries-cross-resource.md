---
id: software.devops.tranche18.001768
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
fontes: ["https://raw.githubusercontent.com/nolar/kopf/main/README.md", "https://kopf.readthedocs.io/en/stable/walkthrough/creation/", "https://github.com/nolar/kopf"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kopf `@kopf.index`: indexação em memória em tempo real para consultas cruzadas entre recursos sem chamadas de API

## Em uma frase
O decorador **`@kopf.index`** do Kopf constrói e mantém atualizado em tempo real um índice em memória (`kopf.Index`) de qualquer recurso do cluster, injetando esse índice diretamente como um argumento `kwargs` em todos os outros handlers, timers e webhooks.

## Por que importa
Se o handler de reconciliação de um `Pod` precisar consultar informações de todas as `NetworkPolicies` ou `Tenants` do cluster fazendo uma chamada HTTP `LIST` ao `kube-apiserver` a cada evento, o operador sofrerá *client-side throttling* rapidamente.

## Como funciona
Uma função decorada com `@kopf.index('tenants')` retorna o valor (ou chave-valor) que deve ser indexado para cada `Tenant`. O Kopf atualiza automaticamente o dicionário em memória quando qualquer `Tenant` é criado, modificado ou deletado, e qualquer outro handler recebe o índice pronto apenas declarando o nome da função de índice na sua assinatura.

## Exemplo
```python
import kopf

@kopf.index('ephemeralvolumeclaims')
def evcs_by_ns(namespace, name, spec, **kwargs):
    return {(namespace, name): spec.get('size')}

@kopf.on.create('pods')
def check_pod_volumes(namespace, evcs_by_ns: kopf.Index, **kwargs):
    known = list(evcs_by_ns.get((namespace, 'my-claim'), []))
    print(f"Tamanhos conhecidos em memória: {known}")
```

## Limites e trade-offs
Os índices `@kopf.index` são populados integralmente na inicialização do operador antes que os handlers de eventos e timers comecem a processar objetos, garantindo consistência desde o primeiro evento.

## Como verificar
Declare um `@kopf.index` em seu operador e inspecione o objeto `kopf.Index` injetado em um `@kopf.on.create` sem realizar chamadas extras ao `kubernetes.client`.

## Conexões
- [[kopf-admission-webhooks-validating-mutating-dev-tunneling]] — Veja também: Kopf: implementação de Validating e Mutating Admission Webhooks com `@kopf.on.validate` e `@kopf.on.mutate`.
- [[kopf-peering-alta-disponibilidade-pausa-dev-mode-priority]] — Veja também: Kopf Peering: coordenação multi-réplica (`KopfPeering`) e pausa automática do operador de cluster durante desenvolvimento local.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
