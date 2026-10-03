---
id: software.devops.tranche19.001803
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS `faas-netes`: comparação entre o modo Controller e o modo Operator com o CRD `Function` (`openfaas.com/v1`)

## Em uma frase
O provedor Kubernetes `faas-netes` possui dois modos arquiteturais de operação: o modo **Controller** (usado no OpenFaaS CE) e o modo **Operator** (suportado para produção no OpenFaaS Standard/Enterprise), que reconcilia o Custom Resource **`Function`** (`openfaas.com/v1`).

## Por que importa
Gerenciar funções exclusivamente pela API REST do Gateway sem um Custom Resource nativo impede que ferramentas GitOps (como Argo CD e Flux) e `kubectl get functions` gerenciem as funções declarativamente como recursos de primeira classe do Kubernetes.

## Como funciona
Com o modo Operator habilitado no Helm chart do OpenFaaS, cada função é representada por um objeto `Function` no namespace `openfaas-fn`, podendo ser gerada com `faas-cli generate --yaml stack.yaml` e aplicada diretamente via `kubectl apply -f` ou sincronizada pelo Argo CD.

## Exemplo
```yaml
apiVersion: openfaas.com/v1
kind: Function
metadata:
  name: nodeinfo
  namespace: openfaas-fn
spec:
  name: nodeinfo
  image: ghcr.io/openfaas/nodeinfo:latest
  labels:
    com.openfaas.scale.min: "1"
    com.openfaas.scale.max: "10"
```

## Limites e trade-offs
Conforme documentado no repositório `faas-netes`, o modo controller legado permanece disponível para a edição CE, enquanto o modo operator com CRD `Function` é o caminho suportado para cargas de produção.

## Como verificar
Execute `faas-cli generate -f stack.yaml` para converter um manifesto do `faas-cli` em um Custom Resource `Function` do Kubernetes.

## Conexões
- [[openfaas-faas-cli-stack-yaml-template-store-build-push-deploy]] — Veja também: OpenFaaS `faas-cli` e `stack.yaml`: ciclo de vida de funções (`new`, `build`, `push`, `deploy`, `up`) e Template Store.
- [[openfaas-watchdog-http-mode-readiness-lock-file-timeouts]] — Veja também: OpenFaaS `of-watchdog` e Probes de Saúde: gerenciamento do arquivo `.lock` de readiness e timeouts de leitura/escrita.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
