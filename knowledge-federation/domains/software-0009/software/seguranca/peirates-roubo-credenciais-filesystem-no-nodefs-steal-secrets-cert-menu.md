---
id: software.seguranca.tranche10.000997
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/inguardians/peirates/main/README.md", "https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md", "https://raw.githubusercontent.com/inguardians/peirates/main/go.mod"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Peirates Pós-Escape: Coleta Automatizada de Credenciais do Nó (**`nodefs-steal-secrets` `30`**) e Contextos de Certificados TLS (**`cert-menu` `9`**)

## Em uma frase
Quando um pentester consegue escapar de um container para o sistema de arquivos de um nó Worker (ou monta o disco do nó via `hostPath` em `/host`), qual é o próximo passo para escalar de um **Nó Worker isolado** para o controle de **Todo o Cluster (`cluster-admin`)**?

## Por que importa
Em vez de procurar arquivos manualmente pelo disco do nó, o comando **`nodefs-steal-secrets` (`30`)** do Peirates varre sistematicamente o sistema de arquivos do nó Worker em busca de duas minas de ouro de credenciais Kubernetes: **(1) Os tokens de `ServiceAccount` de TODOS os outros Pods que estão rodando naquele mesmo nó** (armazenados nos volumes `tmpfs` de `/var/lib/kubelet/pods/<pod-uid>/volumes/kubernetes.io~projected/.../token`!) e **(2) A credencial e certificado de cliente X.509 do próprio `kubelet` do nó (`/etc/kubernetes/kubelet.conf` e `/var/lib/kubelet/pki/kubelet-client-current.pem`)**!

## Como funciona
Todos os tokens de ServiceAccount encontrados nos outros Pods do nó são importados automaticamente para o **`sa-menu` (`1`)**, e os certificados X.509 de cliente (`client-certificate-data` / `client-key-data`) são importados para o **`cert-menu` (`9`)** do Peirates!

## Exemplo
```bash
# Auditar em um no Kubernetes quais tokens de ServiceAccount de Pods estao montados sob /var/lib/kubelet/pods/
find /var/lib/kubelet/pods/ -path "*/kubernetes.io~projected/*" -name "token" 2>/dev/null
```

## Limites e trade-offs
Entenda a implicação arquitetural de segurança revelada pelo `nodefs-steal-secrets` (`30`): **qualquer atacante que comprometa o root de UM único nó Worker ganha acesso imediato aos tokens de ServiceAccount de TODOS os Pods agendados naquele nó**! Por isso, você **jamais** deve agendar Pods altamente privilegiados (como controladores de CI/CD, ArgoCD, Vault ou operadores com permissões `cluster-admin`) nos mesmos nós Worker compartilhados onde rodam aplicações expostas à internet (use **Node Taints & Tolerations** dedicados para isolar workloads críticos)!

## Como verificar
Ative também o admission controller **`NodeRestriction`** no `kube-apiserver` para garantir que o certificado `system:node:<nome>` do Kubelet de um nó comprometido só possa modificar objetos `Node` e `Pod` vinculados àquele próprio nó.

## Conexões
- [[peirates-escapes-avancados-core-pattern-ptrace-hostlog-symlink]] — Veja também: Peirates: Técnicas Avançadas de Escape (**`hostproc-core-pattern-breakout` `29`**, **`hostpid-ptrace-breakout` `32`** e **`hostlog-symlink-read` `33`**).
- [[peirates-descoberta-interna-pods-mounts-tcpscan-enumerate-dns]] — Veja também: Peirates: Reconhecimento Interno de Cluster com **`dump-pod-info` (`4`)**, **`find-volume-mounts` (`5`)**, **`tcpscan` (`93`)** e **`enumerate-dns` (`94`)**.
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac]] — Referência cruzada direta com peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
