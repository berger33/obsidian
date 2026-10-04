---
id: software.devops.tranche20.001919
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://cert-manager.io/docs/trust/trust-manager/", "https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md", "https://github.com/cert-manager/trust-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# trust-manager Status Conditions e Webhook de Validação: diagnóstico de `Synced: True` vs erros de fonte ausente

## Em uma frase
O controlador e o webhook de admissão do `trust-manager` validam a sintaxe dos recursos `Bundle` na criação/atualização e reportam o estado detalhado da reconciliação em **`status.conditions`** (especificamente a condição **`Synced`**) e **`status.defaultCAPackageVersion`**.

## Por que importa
Se um engenheiro referenciar em `spec.sources` o nome de um `Secret` que ainda não foi criado no *Trust Namespace* ou que contém dados PEM corrompidos, saber diagnosticar rapidamente por que o `ConfigMap` não foi atualizado evita horas de troubleshooting de TLS.

## Como funciona
Quando todas as fontes são lidas e todos os namespaces selecionados estão sincronizados, o `Bundle` reporta `Synced: True` (`Reason: Synced`). Se alguma fonte `secret` ou `configMap` nomeada não for encontrada no *Trust Namespace*, o controlador interrompe a atualização para não sobrescrever os pacotes existentes com um bundle incompleto e reporta `Synced: False` (`Reason: SourceNotFound`).

## Exemplo
```bash
# Verificando o status de sincronização e a versão do pacote de CAs padrão de todos os Bundles:
kubectl get bundles
kubectl describe bundle corp-ca-bundle
```

## Limites e trade-offs
Esse comportamento *fail-safe* quando uma fonte nomeada desaparece acidentalmente protege os aplicativos em produção de perderem subitamente suas CAs confiáveis.

## Como verificar
Execute `kubectl get bundle <nome> -o jsonpath='{.status.conditions}'` para auditar o estado `Synced` em pipelines de deploy.

## Conexões
- [[trustmanager-montagem-volumes-pods-subpath-armadilha-atualizacao-kubelet]] — Veja também: trust-manager Montagem em Pods: atualização automática de `ConfigMap` pelo `kubelet` vs armadilha de `volumeMounts.subPath`.
- [[trustmanager-testes-unit-integration-smoke-kind-operacao-producao]] — Veja também: trust-manager Qualidade e Operação: suítes `test-unit`, `test-integration`, `test-smoke` em Kind e métricas Prometheus.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
