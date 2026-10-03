---
id: software.devops.tranche08.000722
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
fontes: ["https://raw.githubusercontent.com/google/gvisor/master/README.md", "https://gvisor.dev/docs/architecture_guide/intro/", "https://github.com/google/gvisor"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Google gVisor: plataformas de interceptação de syscalls e page faults (Systrap padrão e KVM)

## Em uma frase
O gVisor utiliza abstrações intercambiáveis chamadas "gVisor platforms" para interceptar chamadas de sistema e page faults do workload, suportando atualmente duas plataformas: `Systrap` (o padrão baseado em `seccomp-bpf`) e `KVM` (baseada em virtualização).

## Por que importa
Para que o gVisor Sentry funcione como um kernel de aplicação em espaço de usuário, ele precisa garantir que nenhuma instrução `syscall` executada pelo código não confiável do container chegue diretamente ao kernel do host Linux, e que esse redirecionamento ocorra com o menor custo possível mesmo dentro de máquinas virtuais na nuvem onde a virtualização aninhada (`KVM`) não está disponível ou é lenta. A documentação de arquitetura do gVisor (`Introduction to gVisor security`) detalha as duas plataformas suportadas.

## Como funciona
(1) **Plataforma `Systrap` (padrão)**: utiliza o subsistema `seccomp-bpf` do Linux para **interceptação** de chamadas de sistema (em vez do uso comum de apenas filtragem) combinada a técnicas otimizadas de substituição de instruções/memória compartilhada para redirecionar o fluxo de execução ao Sentry em user-space. Como o `Systrap` não exige suporte de virtualização de hardware do host, ele é ideal para rodar **dentro** de máquinas virtuais em nuvem pública. (2) **Plataforma `KVM`**: utiliza o subsistema KVM do Linux para isolamento de espaço de endereçamento e interceptação de page faults e syscalls (onde o código do workload roda em guest ring 3); requer suporte a virtualização (`/dev/kvm`) e, embora funcione com virtualização aninhada, é geralmente mais lenta que o `Systrap` nesse modo.

## Exemplo
```bash
# Executar um container Docker sob o runtime runsc especificando explicitamente a plataforma systrap (padrão)
sudo docker run --rm --runtime=runsc -it ubuntu uname -a
```

## Limites e trade-offs
Embora as plataformas `Systrap` e `KVM` sejam transparentemente intercambiáveis do ponto de vista do administrador de sistemas (`--platform=systrap` ou `--platform=kvm`), a documentação oficial de segurança ressalta que elas diferem do ponto de vista de superfície do kernel host: o `Systrap` apoia-se no subsistema `seccomp-bpf` e gerenciamento de processos do Linux, enquanto o `KVM` apoia-se na API `ioctl` do `/dev/kvm`.

## Como verificar
Execute um container com `runsc` e inspecione os argumentos do comando ou logs de inicialização do `runsc` para confirmar qual plataforma (`systrap` ou `kvm`) está ativa no ambiente.

## Conexões
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Veja também: Google gVisor: kernel de aplicação em espaço de usuário escrito em Go (Sentry, Gofer e runsc).
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Veja também: Google gVisor: integração do runtime OCI runsc e containerd-shim-runsc-v1 com Docker e Kubernetes.
- [[gvisor-defesa-profundidade-limites-protecao-runtime-monitoring]] — Referência cruzada direta com gvisor-defesa-profundidade-limites-protecao-runtime-monitoring.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
