---
id: software.seguranca.tranche05.000495
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md", "https://github.com/SELinuxProject/selinux/wiki", "https://github.com/SELinuxProject/selinux/wiki/Tools"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SELinux: Isolamento Multi-Tenant de Containers e Pods Kubernetes com **MCS** (`s0:cX,cY`), `container_t`, `container_file_t` e Montagens `:z` / `:Z`

## Em uma frase
Em hosts de containers (Podman, CRI-O, Docker, OpenShift e Kubernetes em RHEL/Fedora CoreOS), o SELinux combina *Type Enforcement* (confinando todos os processos de containers no tipo **`container_t`** / `svirt_lxc_net_t` e os volumes em **`container_file_t`**) com **Multi-Category Security (MCS)**.

## Por que importa
Mesmo que dois containers de clientes diferentes rodem como `root` (UID 0) no mesmo nó e uma vulnerabilidade no runtime permita escapar do namespace de montagem, o MCS atribui um par único de categorias aleatórias a cada container (ex.: Container A recebe `s0:c12,c45` e Container B recebe `s0:c88,c102`), impedindo que o Container A leia ou ataque processos e volumes do Container B.

## Como funciona
Ao montar um diretório do host em um container (Podman/Docker), o sufixo **`:Z`** (maiúsculo) re-rotula o diretório como `container_file_t` com o par MCS **privado exclusivo** daquele container, enquanto **`:z`** (minúsculo) aplica `container_file_t:s0` compartilhado entre múltiplos containers. No Kubernetes, define-se `securityContext.seLinuxOptions`.

## Exemplo
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: isolated-tenant-pod
  namespace: tenant-alpha
spec:
  securityContext:
    seLinuxOptions:
      level: "s0:c120,c240"
  containers:
    - name: app
      image: registry.internal.corp/tenant/app@sha256:9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

## Limites e trade-offs
Nunca passe `:Z` ou `:z` ao montar diretórios críticos do sistema operacional do host (como `/etc`, `/usr` ou `/var/log`) dentro de um container, pois o runtime re-rotulará recursivamente os arquivos do sistema para `container_file_t` e quebrará os serviços do próprio host! Para containers que precisam de políticas customizadas além do `container_t`, use o gerador **`udica`**.

## Como verificar
Execute `ps -eZ | grep container_t` no nó de containers e confirme que cada container possui seu próprio par exclusivo de categorias MCS `s0:cX,cY`.

## Conexões
- [[selinux-gerenciamento-portas-rede-semanage-port-http-ssh]] — Veja também: SELinux: Controle de Acesso a Portas TCP/UDP com `semanage port` (`http_port_t`, `ssh_port_t`, `mysqld_port_t`).
- [[selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert]] — Veja também: SELinux: Diagnóstico Forense de Negativas `AVC` com `ausearch -m AVC`, `audit2why` e `sealert`.
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.
- [[selinux-compilacao-modulos-customizados-te-cil-udica-semodule]] — Referência cruzada direta com selinux-compilacao-modulos-customizados-te-cil-udica-semodule.
- [[apparmor-integracao-containers-docker-kubernetes-securitycontext]] — Referência cruzada direta com apparmor-integracao-containers-docker-kubernetes-securitycontext.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
