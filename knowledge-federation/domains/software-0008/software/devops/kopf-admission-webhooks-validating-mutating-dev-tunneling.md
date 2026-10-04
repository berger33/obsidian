---
id: software.devops.tranche18.001767
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

# Kopf: implementação de Validating e Mutating Admission Webhooks com `@kopf.on.validate` e `@kopf.on.mutate`

## Em uma frase
O Kopf permite implementar **Validating Admission Webhooks** (`@kopf.on.validate`) e **Mutating Admission Webhooks** (`@kopf.on.mutate`) no mesmo script Python dos handlers de reconciliação, incluindo suporte a tunelamento automático para desenvolvimento fora do cluster.

## Por que importa
Sem um Admission Webhook síncrono, um erro de configuração em um Custom Resource só é descoberto segundos depois nos logs assíncronos do controlador, em vez de rejeitar o comando `kubectl apply` imediatamente no terminal do usuário.

## Como funciona
Em `@kopf.on.validate`, levantar `kopf.AdmissionError("mensagem")` rejeita a requisição na API do Kubernetes com o motivo informado; em `@kopf.on.mutate`, modificar o dicionário `patch` recebido nos `kwargs` aplica um JSONPatch mutante no objeto antes de ser salvo no `etcd`.

## Exemplo
```python
import kopf

@kopf.on.validate('ephemeralvolumeclaims')
def validate_size(spec, warnings, **kwargs):
    size = spec.get('size', '')
    if not size.endswith(('M', 'G', 'Gi', 'Mi')):
        raise kopf.AdmissionError("spec.size deve terminar com M, Mi, G ou Gi.")
    if size.endswith('T'):
        warnings.append("Volumes em Terabytes exigem aprovação de cota.")
```

## Limites e trade-offs
A lista mutável `warnings` injetada nos `kwargs` dos admission handlers permite devolver avisos (`Warning:`) diretamente na saída do `kubectl apply` do usuário mesmo quando a requisição é aprovada.

## Como verificar
Teste o envio de um manifesto inválido para um webhook `@kopf.on.validate` e confirme que o `kubectl apply` falha sincronamente exibindo a mensagem do `AdmissionError`.

## Conexões
- [[kopf-filtragem-eventos-labels-annotations-when-callbacks-stealth]] — Veja também: Kopf: filtragem declarativa de recursos por `labels`, `annotations`, `field` e predicados `when` em modo *stealth*.
- [[kopf-indexacao-em-memoria-kopf-index-queries-cross-resource]] — Veja também: Kopf `@kopf.index`: indexação em memória em tempo real para consultas cruzadas entre recursos sem chamadas de API.

## Fontes
- [Kopf GitHub — README.md (Kubernetes Operator Pythonic Framework, Declarative Decorators, Daemons, Timers, Indexing, Webhooks & Peering)](https://raw.githubusercontent.com/nolar/kopf/main/README.md) — README oficial do nolar/kopf detalhando handlers síncronos/assíncronos, persistência de progresso, retentativas, indexação em memória e coordenação de peering; consultado em 2026-10-03.
- [Kopf Official Documentation — Walkthrough: Creating the Objects (Handlers, Spec Parsing, PermanentError & Kubernetes Client Integration)](https://kopf.readthedocs.io/en/stable/walkthrough/creation/) — Guia oficial do Kopf demonstrando a criação de recursos filhos, validação com PermanentError e publicação automática de logs e eventos; consultado em 2026-10-03.
- [Kopf — Official GitHub Repository](https://github.com/nolar/kopf) — Repositório oficial do Kubernetes Operator Pythonic Framework (Kopf); consultado em 2026-10-03.
