---
id: software.devops.tranche18.001763
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

# Kopf `@kopf.daemon` e `@kopf.timer`: execução de tarefas contínuas e periódicas vinculadas ao tempo de vida do recurso

## Em uma frase
Além de handlers orientados a eventos pontuais, o Kopf fornece os decoradores **`@kopf.daemon`** (que inicia uma thread ou task `asyncio` contínua para cada recurso existente enquanto ele existir) e **`@kopf.timer`** (que dispara uma função periodicamente a cada `interval` segundos para cada recurso).

## Por que importa
Monitorar uma fila externa, manter um túnel aberto ou verificar a saúde de um banco de dados provisionado a cada 30 segundos enquanto um Custom Resource existir exigiria gerenciar pools de threads e cancelamentos manuais se o framework só suportasse callbacks de criação/atualização.

## Como funciona
No `@kopf.daemon`, o Kopf injeta o argumento `stopped` (`kopf.DaemonStopped`): o loop `while not stopped:` roda em background (em asyncio nativo se a função for `async def` ou em thread se for `def`) e é sinalizado automaticamente para encerrar assim que o recurso Kubernetes é deletado. Já `@kopf.timer(..., interval=60.0, idle=10.0)` executa a função em intervalos regulares sem precisar manter um loop manual.

## Exemplo
```python
import time
import kopf

@kopf.daemon('kopfexamples', cancellation_timeout=10.0)
def monitor_resource(spec, name, stopped, logger, **kwargs):
    while not stopped:
        logger.info(f"Monitorando {name}: {spec.get('endpoint')}")
        stopped.wait(15.0)

@kopf.timer('kopfexamples', interval=60.0)
def periodic_sync(spec, name, **kwargs):
    print(f"Tick periódico de 60s para {name}")
```

## Limites e trade-offs
Dentro de um `@kopf.daemon` síncrono, prefira usar `stopped.wait(segundos)` em vez de `time.sleep(segundos)` para que o daemon acorde e encerre instantaneamente quando o recurso for deletado no Kubernetes.

## Como verificar
Crie um recurso no cluster, observe os ticks do `@kopf.timer` e do `@kopf.daemon`, delete o recurso e confirme o encerramento imediato da task.

## Conexões
- [[kopf-handlers-ciclo-vida-create-update-delete-resume-field-diffs]] — Veja também: Kopf: handlers de causa de mudança (`@kopf.on.create`, `update`, `delete`, `resume`, `field`) e inspeção de `diff`.
- [[kopf-tratamento-erros-retries-temporaryerror-permanenterror-persistencia]] — Veja também: Kopf: consistência eventual, retentativas com `TemporaryError` vs `PermanentError` e persistência de progresso.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
