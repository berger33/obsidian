---
id: software.devops.tranche18.001765
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

# Kopf: hierarquia de objetos filhos, propagação de labels e Garbage Collection com `kopf.adopt`

## Em uma frase
Para vincular recursos filhos (como `Pods`, `Services` ou `PersistentVolumeClaims` criados via cliente `kubernetes` ou `pykube-ng`) ao Custom Resource pai, o Kopf oferece as funções auxiliares **`kopf.adopt(data)`**, `kopf.label(data)` e `kopf.harmonize_naming(data)`.

## Por que importa
Se o handler Python criar um `PersistentVolumeClaim` ou `Deployment` filho sem preencher `metadata.ownerReferences` apontando para o UID do Custom Resource pai, deletar o CR pai deixará os PVCs e Deployments filhos órfãos consumindo recursos eternamente no cluster.

## Como funciona
Antes de enviar o dicionário/manifesto YAML do objeto filho para a API do Kubernetes (`CoreV1Api().create_namespaced_persistent_volume_claim`), chamar `kopf.adopt(data)` dentro de um handler injeta automaticamente no objeto filho o `namespace` do pai, a entrada `ownerReferences` completa (habilitando o Garbage Collector em cascata do Kubernetes) e propaga os labels de identificação.

## Exemplo
```python
import kopf
import kubernetes
import yaml

@kopf.on.create('ephemeralvolumeclaims')
def create_fn(spec, name, namespace, logger, **kwargs):
    data = yaml.safe_load(f"""
        apiVersion: v1
        kind: PersistentVolumeClaim
        spec:
          accessModes: [ReadWriteOnce]
          resources:
            requests:
              storage: {spec['size']}
    """)
    kopf.adopt(data)
    api = kubernetes.client.CoreV1Api()
    obj = api.create_namespaced_persistent_volume_claim(namespace=namespace, body=data)
    logger.info(f"PVC filho criado e adotado: {obj.metadata.name}")
```

## Limites e trade-offs
O Kopf é deliberadamente agnóstico à biblioteca cliente HTTP do Kubernetes: você pode usar `kubernetes` oficial, `pykube-ng`, `kr8s`, `lightkube` ou `aiohttp` dentro dos handlers junto com `kopf.adopt(data)`.

## Como verificar
Crie o CR pai, verifique com `kubectl get pvc <nome> -o yaml` a presença de `metadata.ownerReferences`, delete o CR pai e confirme a remoção automática do PVC filho.

## Conexões
- [[kopf-tratamento-erros-retries-temporaryerror-permanenterror-persistencia]] — Veja também: Kopf: consistência eventual, retentativas com `TemporaryError` vs `PermanentError` e persistência de progresso.
- [[kopf-filtragem-eventos-labels-annotations-when-callbacks-stealth]] — Veja também: Kopf: filtragem declarativa de recursos por `labels`, `annotations`, `field` e predicados `when` em modo *stealth*.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
