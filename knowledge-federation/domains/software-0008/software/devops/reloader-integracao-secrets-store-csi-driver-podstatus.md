---
id: software.devops.tranche11.001035
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
fontes: ["https://raw.githubusercontent.com/stakater/Reloader/master/README.md", "https://docs.stakater.com/reloader/latest/", "https://github.com/stakater/Reloader"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte do Reloader ao Secrets Store CSI Driver (SecretProviderClassPodStatus e --enable-csi-integration)

## Em uma frase
Quando habilitado com **`--enable-csi-integration=true`** (`reloader.enableCSIIntegration: true`), o Reloader monitora recursos **`SecretProviderClassPodStatus`** gerados pelo Secrets Store CSI Driver e reinicia automaticamente workloads cujos segredos montados diretamente via CSI (sem objeto Kubernetes `Secret`) tiveram suas versões atualizadas no cofre externo.

## Por que importa
Equipes de segurança frequentemente utilizam o Secrets Store CSI Driver para montar segredos do AWS Secrets Manager, Azure Key Vault ou HashiCorp Vault diretamente como arquivos tmpfs nos pods **sem criar objetos `Secret` no etcd**. Como não há um objeto Kubernetes `Secret` mudando e aplicações legadas não relêem arquivos do disco sozinhas, os pods continuariam usando a versão antiga do segredo após a rotação se o Reloader não monitorasse o status do CSI.

## Como funciona
Conforme a seção *CSI Secret Provider Support* do README oficial: (1) o Secrets Store CSI Driver deve estar instalado no cluster com a rotação de segredos habilitada; (2) quando um segredo rotaciona no cofre externo, o CSI driver atualiza o recurso `SecretProviderClassPodStatus` refletindo as novas versões de segredos montadas no pod; e (3) o Reloader (com `--enable-csi-integration=true`) observa o `SecretProviderClassPodStatus` no nível de cada segredo individual e dispara o rollout dos workloads anotados com `reloader.stakater.com/auto: "true"`, `secretproviderclass.reloader.stakater.com/auto: "true"` ou `secretproviderclass.reloader.stakater.com/reload: "meu-secretproviderclass"`.

## Exemplo
```yaml
# Deployment utilizando descoberta específica de SecretProviderClass (CSI Driver) no Reloader
apiVersion: apps/v1
kind: Deployment
metadata:
  name: servico-financeiro
  annotations:
    secretproviderclass.reloader.stakater.com/reload: "vault-db-creds"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: servico-financeiro
  template:
    metadata:
      labels:
        app: servico-financeiro
    spec:
      containers:
        - name: app
          image: ghcr.io/exemplo/financeiro:v2.1.0
          volumeMounts:
            - name: secrets-store-inline
              mountPath: "/mnt/secrets-store"
              readOnly: true
      volumes:
        - name: secrets-store-inline
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: "vault-db-creds"
```

## Limites e trade-offs
A detecção via CSI depende de a rotação periódica (`enableSecretRotation`) estar habilitada no Secrets Store CSI Driver para que os objetos `SecretProviderClassPodStatus` sejam atualizados quando o segredo muda no provedor de nuvem ou Vault.

## Como verificar
Verifique que o controlador do Reloader foi iniciado com `--enable-csi-integration=true` e inspecione `kubectl get secretproviderclasspodstatus` no namespace do workload após rotacionar o segredo no cofre.

## Conexões
- [[reloader-integracao-gitops-argocd-argo-rollouts-estrategias]] — Veja também: Reloader com GitOps (Argo CD / Flux) e Argo Rollouts: reload-strategy annotations e rollout-strategy restart.
- [[reloader-pausa-deployments-pause-period-alertas-webhook]] — Veja também: Estabilidade operacional no Reloader: janela de pausa (pause-period) e alertas de reload (Slack, Teams, Google Chat e Webhook).
- [[reloader-controlador-kubernetes-rollout-configmaps-secrets]] — Referência cruzada direta com reloader-controlador-kubernetes-rollout-configmaps-secrets.
- [[vault-integracao-kubernetes-auth-injector-csi-eso]] — Referência cruzada direta com vault-integracao-kubernetes-auth-injector-csi-eso.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.

## Fontes
- [Stakater Reloader GitHub — README.md (Reloader v2 Operator SDK, Annotations, Search/Match, Argo Rollouts, Pause & CSI Support)](https://raw.githubusercontent.com/stakater/Reloader/master/README.md) — README oficial do stakater/Reloader detalhando anotações auto/named/search+match/ignore, estratégia restart para Argo Rollouts, alertas webhook, pause-period e integração com Secrets Store CSI Driver; consultado em 2026-10-03.
- [Stakater Reloader Official Documentation — Overview & Mechanics (Watch API, SHA1 Data Check, Workloads & GitOps)](https://docs.stakater.com/reloader/latest/) — Documentação oficial do Reloader explicando a detecção de mudança de dados reais via watch API, patch SHA1 no pod template, workloads suportados e integração com ESO, Sealed Secrets, cert-manager e Argo CD; consultado em 2026-10-03.
- [Stakater Reloader — Official GitHub Repository](https://github.com/stakater/Reloader) — Repositório oficial Apache-2.0 do Stakater Reloader; consultado em 2026-10-03.
