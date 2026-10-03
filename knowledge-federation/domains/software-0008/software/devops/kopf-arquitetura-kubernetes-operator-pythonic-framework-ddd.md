---
id: software.devops.tranche18.001761
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

# Kopf (*Kubernetes Operator Pythonic Framework*): arquitetura de operadores Kubernetes em Python com decoradores declarativos

## Em uma frase
O **Kopf** (*Kubernetes Operator Pythonic Framework*, originalmente iniciado em `zalando-incubator/kopf` e mantido em `nolar/kopf`, estável em SemVer v1 para Python 3.10+) é um framework e biblioteca que permite escrever operadores Kubernetes completos em poucas linhas de Python puro usando decoradores declarativos.

## Por que importa
Para equipes cujo ecossistema principal é Python (IA/ML, ciência de dados, automação de rede e plataformas internas), manter um operador em Go apenas para orquestrar `PersistentVolumeClaims`, `Jobs` de treinamento ou recursos customizados introduz atrito cognitivo e duplica bibliotecas de domínio.

## Como funciona
O Kopf traz o *Domain-Driven Design (DDD)* para o nível de infraestrutura: o Kubernetes atua como o banco de dados de objetos de domínio (Custom Resources ou recursos nativos como `Pod`/`Namespace`), enquanto o operador Python contém apenas a lógica de domínio em funções decoradas (`@kopf.on.create`, `@kopf.on.update`, `@kopf.on.delete`, `@kopf.daemon`, `@kopf.timer`), executável com `kopf run handlers.py`.

## Exemplo
```python
import kopf

@kopf.on.create('kopfexamples')
def create_fn(spec, name, meta, status, **kwargs):
    print(f"Created {name} with spec: {spec}")
    return {'message': f'Processed {name}'}
```

## Limites e trade-offs
Qualquer dicionário retornado por um handler do Kopf é automaticamente serializado e gravado dentro do sub-recurso `status` do objeto Kubernetes correspondente sob a chave com o nome da função handler.

## Como verificar
Execute `kopf run handlers.py --verbose` localmente (ou via imagem `ghcr.io/nolar/kopf`) e aplique um recurso de teste para observar o disparo do handler e a atualização de `status`.

## Conexões
- [[kopf-handlers-ciclo-vida-create-update-delete-resume-field-diffs]] — Veja também: Kopf: handlers de causa de mudança (`@kopf.on.create`, `update`, `delete`, `resume`, `field`) e inspeção de `diff`.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
