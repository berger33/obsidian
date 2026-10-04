---
id: software.devops.tranche18.001762
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

# Kopf: handlers de causa de mudança (`@kopf.on.create`, `update`, `delete`, `resume`, `field`) e inspeção de `diff`

## Em uma frase
O Kopf oferece decoradores de alto nível para as causas reais de mudança no ciclo de vida de um recurso (`@kopf.on.create`, `@kopf.on.update`, `@kopf.on.delete`, `@kopf.on.resume`) e permite filtrar mudanças em um único campo específico (`@kopf.on.field('...', field='spec.size')`) entregando a lista exata de diferenças (`diff`, `old`, `new`) nos argumentos `kwargs`.

## Por que importa
Em um watcher bruto da API do Kubernetes, uma atualização de `status` ou de uma `annotation` interna dispara o mesmo evento `MODIFIED` que uma alteração real em `spec`; o Kopf calcula o diff contra a última configuração processada e invoca `@kopf.on.update` apenas quando há mudança efetiva nos campos relevantes.

## Como funciona
Nos handlers de atualização, o argumento `diff` recebe uma tupla de operações `(op, field_path, old_val, new_val)` (como `('change', ('spec', 'size'), '1G', '5G')`). Além disso, `@kopf.on.delete` gerencia automaticamente a adição e remoção de `finalizers` no objeto Kubernetes para garantir que o handler de limpeza rode antes que o objeto suma do `etcd`.

## Exemplo
```python
import kopf

@kopf.on.field('ephemeralvolumeclaims', field='spec.size')
def resize_pvc(old, new, name, namespace, logger, **kwargs):
    logger.info(f"Redimensionando PVC {namespace}/{name} de {old} para {new}")
```

## Limites e trade-offs
Se você precisar que a exclusão de um objeto nunca seja bloqueada por finalizer mesmo que o operador esteja desligado, passe `optional=True` em `@kopf.on.delete(..., optional=True)`.

## Como verificar
Altere um campo do `spec` de um recurso existente com `kubectl patch` e verifique nos logs do Kopf os valores exatos de `old`, `new` e `diff` recebidos pelo handler.

## Conexões
- [[kopf-arquitetura-kubernetes-operator-pythonic-framework-ddd]] — Veja também: Kopf (*Kubernetes Operator Pythonic Framework*): arquitetura de operadores Kubernetes em Python com decoradores declarativos.
- [[kopf-daemons-timers-tarefas-background-continuas-stopped-flag]] — Veja também: Kopf `@kopf.daemon` e `@kopf.timer`: execução de tarefas contínuas e periódicas vinculadas ao tempo de vida do recurso.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
