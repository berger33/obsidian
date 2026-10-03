---
id: software.devops.tranche20.001918
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

# trust-manager Montagem em Pods: atualização automática de `ConfigMap` pelo `kubelet` vs armadilha de `volumeMounts.subPath`

## Em uma frase
Quando uma aplicação monta o `ConfigMap` (ou `Secret`) gerenciado pelo `trust-manager` como um volume no Pod, a forma como o `volumeMount` é declarado determina se o arquivo de certificados dentro do container será atualizado automaticamente pelo `kubelet` quando o `Bundle` mudar.

## Por que importa
No Kubernetes, se um container montar uma chave individual usando **`subPath`** (ex.: `mountPath: /etc/ssl/certs/ca-certificates.crt` com `subPath: ca-certificates.crt`), o `kubelet` **nunca** atualiza esse arquivo em execução quando o `ConfigMap` é modificado, exigindo reiniciar o Pod.

## Como funciona
Para receber atualizações automáticas de certificados em tempo de execução sem reiniciar o Pod, monte o diretório inteiro (por exemplo em `mountPath: /etc/pki/trust-bundle`) **sem `subPath`** e aponte a variável de ambiente da aplicação (`SSL_CERT_FILE=/etc/pki/trust-bundle/ca-bundle.pem` ou `NODE_EXTRA_CA_CERTS`) para o caminho dentro do diretório montado.

## Exemplo
```yaml
env:
  - name: SSL_CERT_FILE
    value: /etc/pki/trust-bundle/ca-bundle.pem
  - name: NODE_EXTRA_CA_CERTS
    value: /etc/pki/trust-bundle/ca-bundle.pem
volumeMounts:
  - name: ca-trust
    mountPath: /etc/pki/trust-bundle
    readOnly: true
volumes:
  - name: ca-trust
    configMap:
      name: corp-ca-bundle
```

## Limites e trade-offs
Se a aplicação ler o arquivo de certificados apenas uma única vez na inicialização do processo e mantiver o pool em memória sem recarregar do disco, combine a montagem com um controlador de reload (como Reloader) ou recarregamento por inotify.

## Como verificar
Inspecione os `volumeMounts` dos seus Deployments com `kubectl get deploy -o yaml` e certifique-se de que o volume do `Bundle` não utiliza `subPath` se você espera atualização dinâmica.

## Conexões
- [[trustmanager-integracao-cert-manager-ca-issuer-linkerd-istio-mtls]] — Veja também: trust-manager com `cert-manager` e Service Mesh: distribuição automática da CA raiz de mTLS para Linkerd, Istio e Pods.
- [[trustmanager-condicoes-status-synced-validacao-webhook-bundle]] — Veja também: trust-manager Status Conditions e Webhook de Validação: diagnóstico de `Synced: True` vs erros de fonte ausente.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://cert-manager.io/docs/trust/trust-manager/) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
