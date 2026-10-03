---
id: software.devops.tranche18.001766
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

# Kopf: filtragem declarativa de recursos por `labels`, `annotations`, `field` e predicados `when` em modo *stealth*

## Em uma frase
Todos os decoradores de recursos do Kopf suportam filtros declarativos por `labels={...}`, `annotations={...}`, valores especiais `kopf.PRESENT` / `kopf.ABSENT`, filtros de `field=` e funções de predicado `when=callable` (incluindo operação silenciosa sem geração de logs de eventos).

## Por que importa
Em clusters compartilhados ou com milhares de `Pods` e `ConfigMaps`, um operador que observa recursos nativos não deve processar todos os Pods do cluster, mas apenas aqueles marcados com uma anotação ou label específico (ex.: `auto-backup: "enabled"`).

## Como funciona
Quando os filtros são declarados no decorador (`@kopf.on.create('pods', annotations={'backup.corp.io/enabled': 'true'}, when=lambda spec, **_: ...)`), o Kopf avalia as condições antes mesmo de iniciar o ciclo de persistência de estado ou emitir logs, ignorando completamente em modo *stealth* os objetos que não atendem aos critérios.

## Exemplo
```python
import kopf

@kopf.on.create(
    'pods',
    labels={'tier': 'backend', 'managed-by': kopf.PRESENT},
    annotations={'legacy-skip': kopf.ABSENT},
)
def handle_backend_pod(name, namespace, **kwargs):
    print(f"Pod gerenciado detectado: {namespace}/{name}")
```

## Limites e trade-offs
Ao observar recursos nativos do Kubernetes (como `pods`, `services` ou `secrets`), combine sempre filtros de `labels`/`annotations` com `kopf.PRESENT` para evitar que o Kopf grave anotações de rastreamento em objetos do sistema aos quais o operador não pertence.

## Como verificar
Aplique dois Pods (um com o label `tier=backend,managed-by=kopf` e outro sem) e confirme que apenas o primeiro aciona o handler.

## Conexões
- [[kopf-hierarquia-objetos-adopt-label-owner-references-garbage-collection]] — Veja também: Kopf: hierarquia de objetos filhos, propagação de labels e Garbage Collection com `kopf.adopt`.
- [[kopf-admission-webhooks-validating-mutating-dev-tunneling]] — Veja também: Kopf: implementação de Validating e Mutating Admission Webhooks com `@kopf.on.validate` e `@kopf.on.mutate`.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
