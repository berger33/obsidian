---
id: software.devops.tranche18.001764
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
fontes: ["https://kopf.readthedocs.io/en/stable/walkthrough/creation/", "https://raw.githubusercontent.com/nolar/kopf/main/README.md", "https://github.com/nolar/kopf"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kopf: consistência eventual, retentativas com `TemporaryError` vs `PermanentError` e persistência de progresso

## Em uma frase
O Kopf implementa consistência eventual automática: qualquer exceção arbitrária lançada dentro de um handler faz o framework agendar uma nova tentativa (*retry*), enquanto as exceções especiais **`kopf.TemporaryError`** (retentar após `delay`) e **`kopf.PermanentError`** (abortar imediatamente sem retentar) dão controle fino sobre falhas.

## Por que importa
Se uma API externa estiver temporariamente indisponível, o handler deve retentar daqui a 30 segundos; porém, se o usuário informou um valor inválido em `spec.size` que jamais funcionará sem edição humana, ficar retentando em loop infinito apenas polui os logs e sobrecarrega o cluster.

## Como funciona
Nos decoradores de handler, parâmetros como `backoff=30`, `retries=10` e `timeout=3600` limitam o número de tentativas ou o tempo total. O Kopf persiste implicitamente o progresso de cada handler nas anotações/status do recurso para que, mesmo que o Pod do operador reinicie no meio de uma sequência de sub-handlers, os passos já concluídos com sucesso não sejam reexecutados.

## Exemplo
```python
import kopf

@kopf.on.create('ephemeralvolumeclaims', retries=5, backoff=15.0)
def create_pvc(spec, **kwargs):
    size = spec.get('size')
    if not size:
        raise kopf.PermanentError("O campo spec.size é obrigatório.")
    if not storage_backend_ready():
        raise kopf.TemporaryError("Backend ocupado; tentando novamente em 15s.", delay=15)
```

## Limites e trade-offs
Para registrar eventos nativos do Kubernetes (`kubectl describe <recurso>`) associados ao objeto reconciliado, basta usar o objeto `logger` injetado nos `kwargs` (`logger.info(...)`, `logger.warning(...)`, `logger.error(...)`) ou `kopf.info(body, reason=..., message=...)`.

## Como verificar
Aplique um CR sem o campo obrigatório para acionar `kopf.PermanentError` e verifique em `kubectl describe` o evento de erro definitivo e a ausência de novas tentativas.

## Conexões
- [[kopf-daemons-timers-tarefas-background-continuas-stopped-flag]] — Veja também: Kopf `@kopf.daemon` e `@kopf.timer`: execução de tarefas contínuas e periódicas vinculadas ao tempo de vida do recurso.
- [[kopf-hierarquia-objetos-adopt-label-owner-references-garbage-collection]] — Veja também: Kopf: hierarquia de objetos filhos, propagação de labels e Garbage Collection com `kopf.adopt`.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
