---
id: software.seguranca.tranche10.000999
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

# Peirates: Uso da Biblioteca **`kubectl` Embutida (`90`)**, Cliente HTTP **`curl` (`91`)** e Comandos de Sistema de Arquivos (`cd`, `ls`, `cat`, `shell`)

## Em uma frase
Um detalhe brilhante da implementação do Peirates em Go (visível em `go.mod`: `k8s.io/kubectl v0.36.1` e `k8s.io/client-go v0.36.1`) é que **ele compila a biblioteca oficial do próprio `kubectl` diretamente dentro do binário `peirates`**!

## Por que importa
Isso significa que mesmo dentro de um container mínimo onde o executável `/usr/local/bin/kubectl` não existe, o comando **`kubectl` (`90`)** do Peirates permite rodar comandos completos do `kubectl` (`get`, `describe`, `auth can-i`, `apply`, `delete`, `exec`, `logs`) autenticados automaticamente com a `ServiceAccount` ou Certificado selecionado no menu do Peirates!

## Como funciona
Da mesma forma, o comando **`curl` (`91`)** oferece um cliente HTTP embutido, e os comandos internos **`cd`, `pwd`, `ls`, `cat`** permitem navegar pelo sistema de arquivos e ler arquivos mesmo em containers *distroless* que não possuem `/bin/ls` nem `/bin/cat`!

## Exemplo
```text
# Dentro do Peirates: usar a biblioteca kubectl embutida (90) para verificar todas as permissoes RBAC da ServiceAccount atual
[peirates]# kubectl auth can-i --list
[peirates]# kubectl get pods -A
```

## Limites e trade-offs
Como toda chamada feita pelo `kubectl` embutido do Peirates (assim como pelo `kubectl-try-all` e `cdk kcurl`) passa pelo **Kubernetes API Server**, uma regra simples de detecção no **Kubernetes Audit Log** (monitorada por **Falco**, **Datadog**, **Splunk** ou **Paralus**) identifica o comportamento: alerte imediatamente sempre que uma `ServiceAccount` de um Pod de aplicação executar `SelfSubjectRulesReview` (`auth can-i --list`), listar `secrets` fora do seu funcionamento normal ou gerar múltiplos códigos `403 Forbidden` consecutivos!

## Como verificar
Personalize ou monitore também o cabeçalho `User-Agent` registrado nos eventos de `AuditLog` do `kube-apiserver` (`userAgent`).

## Conexões
- [[peirates-descoberta-interna-pods-mounts-tcpscan-enumerate-dns]] — Veja também: Peirates: Reconhecimento Interno de Cluster com **`dump-pod-info` (`4`)**, **`find-volume-mounts` (`5`)**, **`tcpscan` (`93`)** e **`enumerate-dns` (`94`)**.
- [[peirates-matriz-defesa-profundidade-kubernetes-pss-rbac-imds-ebpf]] — Veja também: Matriz de Defesa em Profundidade Kubernetes (Marco **1.000/2.000** do Lote `software-seguranca-2000-0003`): Como Neutralizar **Peirates & CDK** do Código ao Kernel.
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac]] — Referência cruzada direta com peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
