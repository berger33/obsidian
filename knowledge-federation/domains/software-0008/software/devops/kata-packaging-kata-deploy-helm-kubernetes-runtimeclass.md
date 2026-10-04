---
id: software.devops.tranche08.000706
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md", "https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md", "https://github.com/kata-containers/kata-containers"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kata Containers: empacotamento de binários e implantação em Kubernetes com o Helm chart kata-deploy e RuntimeClass

## Em uma frase
O Kata Containers fornece scripts de empacotamento (`tools/packaging`), tarballs de release e o Helm chart oficial `kata-deploy` para instalar automaticamente os binários, hipervisores, kernels e objetos `RuntimeClass` nos nós de um cluster Kubernetes.

## Por que importa
Instalar manualmente binários de hipervisores, kernels guest, imagens `rootfs`, shims `containerd-shim-kata-v2` e editar `/etc/containerd/config.toml` em dezenas de nós workers de um cluster Kubernetes gerenciado é trabalhoso e propenso a desvios de configuração durante o auto-scaling de nós. Segundo a seção `Packaging and releases` do README oficial do Kata Containers, o Helm chart `kata-deploy` automatiza todo esse provisionamento em clusters Kubernetes.

## Como funciona
O diretório `tools/packaging` contém os metadados e scripts que produzem os pacotes estáticos e tarballs de release contendo todos os artefatos necessários (runtimes, hipervisores, kernel guest e rootfs). Quando implantado no Kubernetes via Helm chart `kata-deploy`, um DaemonSet privilegiado copia os artefatos autocontidos do Kata para o sistema de arquivos do nó hospedeiro (tipicamente sob `/opt/kata`), registra dinamicamente os handlers de runtime no `containerd` ou `CRI-O` do nó e cria os objetos `RuntimeClass` na API do Kubernetes (como `kata-qemu`, `kata-clh`, `kata-fc`, `kata-dragonball`). A partir daí, qualquer Pod que especifique `spec.runtimeClassName: kata-qemu` é agendado e isolado automaticamente em uma VM Kata.

## Exemplo
```yaml
# Exemplo de Pod Kubernetes solicitando isolamento em VM leve via RuntimeClass do Kata Containers
apiVersion: v1
kind: Pod
metadata:
  name: workload-isolado-kata
spec:
  runtimeClassName: kata-qemu
  containers:
    - name: app
      image: nginx:alpine
```

## Limites e trade-offs
Ao desinstalar ou atualizar o `kata-deploy` em um cluster Kubernetes ativo, os nós onde já existem Pods rodando com `runtimeClassName: kata-*` precisam ser drenados (`kubectl drain`) antes de remover os binários de `/opt/kata` e reconfigurar o `containerd`, caso contrário os shims das VMs em execução perderão seus binários e configurações de suporte.

## Como verificar
Execute `kubectl get runtimeclasses` para listar as classes criadas pelo `kata-deploy` e rode `kubectl exec workload-isolado-kata -- uname -r` comparando com o `uname -r` do nó worker para comprovar que o Pod enxerga o kernel guest isolado da VM Kata.

## Conexões
- [[kata-kernel-guest-osbuilder-mini-os-rootfs-initrd]] — Veja também: Kata Containers: construção de kernel guest e imagens mini-OS (rootfs e initrd) com osbuilder.
- [[kata-ferramentas-diagnostico-kata-ctl-agent-ctl-debug-trace]] — Veja também: Kata Containers: ferramentas de diagnóstico e depuração (kata-ctl, agent-ctl, kata-debug e trace-forwarder).
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-webhook-admissao-mutacao-pods-runtimeclass]] — Referência cruzada direta com kata-webhook-admissao-mutacao-pods-runtimeclass.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
