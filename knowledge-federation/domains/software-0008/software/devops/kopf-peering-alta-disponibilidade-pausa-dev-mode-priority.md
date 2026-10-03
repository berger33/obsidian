---
id: software.devops.tranche18.001769
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

# Kopf Peering: coordenação multi-réplica (`KopfPeering`) e pausa automática do operador de cluster durante desenvolvimento local

## Em uma frase
O mecanismo de **Peering** do Kopf coordena múltiplas instâncias do mesmo operador usando objetos `ClusterKopfPeering` ou `KopfPeering` (`kopf.dev/v1`), evitando processamento duplicado e permitindo que um operador rodando na máquina do desenvolvedor (`--priority`) pause temporariamente o operador implantado no cluster.

## Por que importa
Quando um desenvolvedor conecta seu laptop a um cluster de staging para depurar um novo handler com `kopf run --dev`, o Deployment do operador que já está rodando dentro do cluster competiria pelos mesmos eventos e sobrescreveria o teste local.

## Como funciona
Com o recurso de peering ativo (`kopf run --peering=my-operator`), as instâncias trocam heartbeats e respeitam a maior prioridade (`--priority=666` ou `--dev`). Enquanto a instância de maior prioridade do desenvolvedor estiver ativa, os Pods de menor prioridade (`priority=0`) no cluster entram automaticamente em pausa silenciosa, retomando o trabalho assim que o desenvolvedor encerra o processo local.

## Exemplo
```bash
# No cluster (prioridade padrão 0):
kopf run handlers.py --peering=my-operator-peering --priority=0

# Na máquina de desenvolvimento (prioridade superior via --dev):
kopf run handlers.py --peering=my-operator-peering --dev
```

## Limites e trade-offs
Quando há dois operadores Kopf completamente diferentes que observam o mesmo `Kind` no mesmo cluster, atribua identidades de armazenamento distintas em `settings.persistence.progress_storage` para que suas anotações de estado não colidam.

## Como verificar
Verifique o objeto `kubectl get kopfpeerings` (ou `clusterkopfpeerings`) enquanto roda uma instância com `--dev` e confirme a transição de liderança.

## Conexões
- [[kopf-indexacao-em-memoria-kopf-index-queries-cross-resource]] — Veja também: Kopf `@kopf.index`: indexação em memória em tempo real para consultas cruzadas entre recursos sem chamadas de API.
- [[kopf-subhandlers-dinamicos-memo-containers-liveness-testing-runner]] — Veja também: Kopf: sub-handlers dinâmicos (`kopf.subhandler`), memória por recurso (`memo`), probe `--liveness` e `KopfRunner`.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
