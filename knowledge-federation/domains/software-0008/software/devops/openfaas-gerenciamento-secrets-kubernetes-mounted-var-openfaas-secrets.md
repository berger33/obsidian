---
id: software.devops.tranche19.001807
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
fontes: ["https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS Secrets: gerenciamento declarativo de segredos montados como arquivos em `/var/openfaas/secrets/`

## Em uma frase
Em vez de expor chaves de API, senhas de banco de dados ou tokens de webhook em variáveis de ambiente em texto claro (`environment:`), o OpenFaaS monta `Secrets` do Kubernetes (no namespace `openfaas-fn`) como arquivos somente leitura dentro de **`/var/openfaas/secrets/<secret-name>`** no container da função.

## Por que importa
Variáveis de ambiente vazam facilmente em dumps de processo, relatórios de crash ou inspeções `kubectl describe pod`; arquivos montados via tmpfs em `/var/openfaas/secrets/` são isolados e restritos às funções que os declaram explicitamente.

## Como funciona
O operador cria o segredo com `faas-cli secret create api-token --from-file=token.txt` (ou `kubectl create secret generic -n openfaas-fn`) e referencia o nome na lista `secrets:` da função em `stack.yaml`. O código da função apenas lê `/var/openfaas/secrets/api-token` da memória na inicialização.

## Exemplo
```bash
faas-cli secret create stripe-signing-key --from-literal="whsec_example123"
faas-cli secret list
```

## Limites e trade-offs
Um `Secret` referenciado por uma função precisa existir obrigatoriamente no namespace das funções (`openfaas-fn` por padrão), e não no namespace de infraestrutura `openfaas`.

## Como verificar
Crie um segredo com `faas-cli secret create`, referencie-o na seção `secrets:` da função e verifique a montagem em `/var/openfaas/secrets/` dentro do Pod.

## Conexões
- [[openfaas-autoscaling-prometheus-alertmanager-scale-min-max-zero]] — Veja também: OpenFaaS Auto-Scaling: escalonamento horizontal por RPS/capacidade (`com.openfaas.scale.min`/`max`) e *scale-to-zero*.
- [[openfaas-profiles-crd-afinidadade-tolerations-pod-security-context]] — Veja também: OpenFaaS `Profile` CRD: aplicação reutilizável de `affinity`, `tolerations`, `runtimeClassName` e `podSecurityContext`.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
