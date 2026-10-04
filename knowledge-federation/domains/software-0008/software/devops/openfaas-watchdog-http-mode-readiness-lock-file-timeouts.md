---
id: software.devops.tranche19.001804
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

# OpenFaaS `of-watchdog` e Probes de Saúde: gerenciamento do arquivo `.lock` de readiness e timeouts de leitura/escrita

## Em uma frase
No OpenFaaS, a verificação de prontidão (*readiness*) e vivacidade (*liveness*) dos Pods de função no Kubernetes baseia-se no binário `of-watchdog`, que cria um arquivo `.lock` no diretório temporário padrão (`/tmp/.lock`) e expõe o endpoint `/_/health` (quando `httpProbe: true`).

## Por que importa
Se o `kubelet` enviasse tráfego para um Pod de função antes do runtime inicializar ou continuasse roteando requisições para uma função que entrou em deadlock, chamadas HTTP síncronas e eventos de fila falhariam.

## Como funciona
O `faas-netes` configura por padrão `httpProbe: true`, `read_timeout: 60s` e `write_timeout: 60s`. Enquanto o arquivo `/tmp/.lock` existir dentro do container da função, a probe de readiness tem sucesso; se a função ou o operador remover `/tmp/.lock`, o Pod sai imediatamente dos `Endpoints` do Service e é reagendado.

## Exemplo
```bash
# Testando o mecanismo de readiness lock file em um Pod de função em execução:
kubectl get pods -n openfaas-fn
kubectl exec -n openfaas-fn deploy/nodeinfo -- ls -la /tmp/.lock
```

## Limites e trade-offs
Funções que processam payloads grandes ou inferências demoradas acima de 60 segundos devem ajustar `read_timeout`, `write_timeout` e `exec_timeout` tanto nas variáveis de ambiente da função quanto na configuração do `gateway` e do `faas-netes`/`queue-worker`.

## Como verificar
Verifique as probes configuradas no Deployment da função com `kubectl describe deploy <func-name> -n openfaas-fn`.

## Conexões
- [[openfaas-faas-netes-modos-operacao-controller-vs-operator-function-crd]] — Veja também: OpenFaaS `faas-netes`: comparação entre o modo Controller e o modo Operator com o CRD `Function` (`openfaas.com/v1`).
- [[openfaas-invocacao-assincrona-function-routes-nats-queue-worker-callback]] — Veja também: OpenFaaS Invocação Assíncrona: processamento em background via `/async-function/<name>`, NATS e `X-Callback-Url`.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
