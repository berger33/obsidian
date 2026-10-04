---
id: software.devops.tranche11.001040
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://docs.stakater.com/reloader/latest/", "https://raw.githubusercontent.com/stakater/Reloader/master/README.md", "https://github.com/stakater/Reloader"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração do Reloader com a pilha de segredos: External Secrets Operator, Sealed Secrets, cert-manager e Vault

## Em uma frase
Sendo agnóstico à ferramenta geradora, o Reloader completa o ciclo de rotação de segredos em conjunto com **External Secrets Operator (ESO)**, **Bitnami Sealed Secrets**, **cert-manager** (`Certificate`) e **Secrets Store CSI Driver**, garantindo que a renovação de um segredo ou certificado no Kubernetes reflita imediatamente nos pods em execução.

## Por que importa
Ferramentas como o ESO e o cert-manager resolvem a primeira metade do problema de rotação de credenciais: elas buscam a nova senha no Vault/AWS ou renovam o certificado X.509 na Let's Encrypt e atualizam o objeto `Secret` no Kubernetes. Porém, para aplicações que carregam o certificado TLS ou a senha do banco apenas na inicialização do processo, a rotação falha silenciosamente sem o Reloader para acionar a segunda metade (o rolling restart dos pods).

## Como funciona
Conforme o diagrama arquitetural do README oficial e a seção *Works with your secrets stack* (`docs.stakater.com/reloader/latest/`): (1) fontes como `ExternalSecret` (ESO), `SealedSecret` (Bitnami) ou `Certificate` (`cert-manager`) criam e atualizam objetos `Secret` nativos no Kubernetes; (2) o Reloader observa esses objetos `Secret` (ou `SecretProviderClassPodStatus` no caso do CSI Driver); e (3) assim que o ESO sincroniza uma nova versão da senha do cofre ou o cert-manager grava o novo `tls.crt`/`tls.key`, o Reloader detecta a alteração no `data` do `Secret` e dispara o rolling restart do `Deployment`, `StatefulSet` ou `DaemonSet` consumidor.

## Exemplo
```yaml
# Combinação de ExternalSecret (ESO) com Deployment anotado pelo Reloader para rotação ponta a ponta de credenciais
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: db-credentials-sync
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: db-credentials
  data:
    - secretKey: password
      remoteRef:
        key: secret/data/prod/db
        property: password
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-app
  annotations:
    secret.reloader.stakater.com/reload: "db-credentials"
```

## Limites e trade-offs
Ao rotacionar uma senha de banco de dados no cofre externo, use estratégias de credenciais duplas (*dual-account* ou período de graça onde tanto a senha antiga quanto a nova permanecem válidas durante alguns minutos), pois o `refreshInterval` do ESO e o `RollingUpdate` acionado pelo Reloader levam alguns segundos/minutos até substituir todos os pods antigos.

## Como verificar
Force a sincronização do `ExternalSecret` após alterar o segredo no cofre e acompanhe os eventos do Deployment (`kubectl describe deployment backend-app`) para verificar o rollout disparado pelo Reloader.

## Conexões
- [[reloader-mecanismo-deteccao-dados-sha1-patch-pod-template]] — Veja também: Mecânica interna do Reloader: comparação de dados reais (SHA1) versus metadados e estratégias de patch no Pod Template.
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://docs.stakater.com/reloader/latest/) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
