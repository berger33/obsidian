---
id: software.devops.tranche18.001770
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

# Kopf: sub-handlers dinâmicos (`kopf.subhandler`), memória por recurso (`memo`), probe `--liveness` e `KopfRunner`

## Em uma frase
Para fluxos avançados de produção, o Kopf oferece **sub-handlers dinâmicos** (`kopf.execute` / `@kopf.subhandler`), contêineres de memória por recurso (`memo`), endpoint HTTP de liveness probe (`--liveness`) e o gerenciador de contexto de testes **`KopfRunner`** (`kopf.testing`).

## Por que importa
Quando a criação de um recurso envolve criar dinamicamente $N$ shards (onde cada shard deve ter seu próprio rastreamento individual de retentativa e sucesso) ou guardar um objeto Python não serializável (como um pool de conexões ou `asyncio.Lock`) associado àquele recurso em memória, handlers planos não bastam.

## Como funciona
Dentro de um handler principal, `kopf.subhandler` permite registrar passos filhos dinamicamente; o objeto `memo` injetado nos `kwargs` guarda atributos arbitrários em memória durante toda a vida daquele recurso no processo; `--liveness=http://0.0.0.0:8080/healthz` expõe saúde para o `kubelet`; e `with KopfRunner(['run', '-A', 'handlers.py']):` permite testar o operador em suítes `pytest`.

## Exemplo
```python
from kopf.testing import KopfRunner

def test_operator_lifecycle():
    with KopfRunner(['run', '-A', '--standalone', 'handlers.py']) as runner:
        # Execute comandos kubectl ou chamadas client aqui
        assert runner.exit_code is None
```

## Limites e trade-offs
Ao empacotar o operador em produção para Kubernetes, use `--standalone` se houver apenas 1 réplica (sem CRD `KopfPeering`) e configure `livenessProbe` HTTP apontando para a porta definida em `--liveness`.

## Como verificar
Execute `kopf run handlers.py --standalone --liveness=http://0.0.0.0:8080/healthz` e valide o retorno JSON de `curl http://localhost:8080/healthz`.

## Conexões
- [[kopf-peering-alta-disponibilidade-pausa-dev-mode-priority]] — Veja também: Kopf Peering: coordenação multi-réplica (`KopfPeering`) e pausa automática do operador de cluster durante desenvolvimento local.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
