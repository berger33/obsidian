---
id: software.seguranca.tranche10.000998
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

# Peirates: Reconhecimento Interno de Cluster com **`dump-pod-info` (`4`)**, **`find-volume-mounts` (`5`)**, **`tcpscan` (`93`)** e **`enumerate-dns` (`94`)**

## Em uma frase
Ao cair dentro de um Pod desconhecido no início de um exercício de Red Team / Pentest Kubernetes, os quatro comandos de reconhecimento interno do Peirates mapeiam o ambiente sem precisar instalar ferramentas externas:

## Por que importa
Primeiro, **`dump-pod-info` (`4`)** e **`find-volume-mounts` (`5`)** inspecionam os detalhes do Pod atual e todas as montagens de volumes presentes (`/proc/mounts`), destacando volumes `hostPath`, `emptyDir`, `projected`, `secret` e `configMap` que podem conter dados sensíveis ou vetores de escape.

## Como funciona
Segundo, **`enumerate-dns` (`94`)** interroga o servidor **CoreDNS (`kube-dns`)** do cluster para descobrir automaticamente nomes de `Services` e endpoints ativos (`*.svc.cluster.local`), enquanto **`tcpscan` (`93`)** realiza varredura de portas TCP sobre os IPs de serviços e nós descobertos!

## Exemplo
```bash
# Executar em modo one-shot (-m) o mapeamento de montagens de volumes do container e a enumeracao de servicos via DNS interno
peirates -m 'find-volume-mounts'
peirates -m 'enumerate-dns'
```

## Limites e trade-offs
Por que a enumeração DNS interna (`enumerate-dns` no Peirates e `DNS-Based Service Discovery` no CDK) é tão eficaz em clusters Kubernetes? Porque o CoreDNS suporta registros `SRV` e resolução reversa (`PTR`) para os IPs da CIDR de `Services` (`10.96.0.0/12`), revelando rapidamente serviços internos como `redis-master.prod.svc.cluster.local`, `postgres.finance.svc.cluster.local` ou `vault.security.svc.cluster.local`!

## Como verificar
Restrinja a comunicação L3/L4 entre namespaces usando **Kubernetes NetworkPolicies** (ou `CiliumNetworkPolicy` com filtragem DNS L7!) para que um Pod comprometido no namespace `frontend` não consiga resolver nem conectar em serviços do namespace `finance`.

## Conexões
- [[peirates-roubo-credenciais-filesystem-no-nodefs-steal-secrets-cert-menu]] — Veja também: Peirates Pós-Escape: Coleta Automatizada de Credenciais do Nó (**`nodefs-steal-secrets` `30`**) e Contextos de Certificados TLS (**`cert-menu` `9`**).
- [[peirates-execucao-kubectl-embutido-curl-shell-interativo]] — Veja também: Peirates: Uso da Biblioteca **`kubectl` Embutida (`90`)**, Cliente HTTP **`curl` (`91`)** e Comandos de Sistema de Arquivos (`cd`, `ls`, `cat`, `shell`).
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[cdk-ferramentas-embutidas-net-tools-ps-netstat-ifconfig-probe-nc-vi]] — Referência cruzada direta com cdk-ferramentas-embutidas-net-tools-ps-netstat-ifconfig-probe-nc-vi.
- [[dnsx-descoberta-servicos-internos-srv-kerberos-ldap-sip-autodiscover]] — Referência cruzada direta com dnsx-descoberta-servicos-internos-srv-kerberos-ldap-sip-autodiscover.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
