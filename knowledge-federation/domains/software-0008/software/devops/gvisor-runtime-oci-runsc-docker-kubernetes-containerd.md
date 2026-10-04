---
id: software.devops.tranche08.000723
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

# Google gVisor: integração do runtime OCI runsc e containerd-shim-runsc-v1 com Docker e Kubernetes

## Em uma frase
O gVisor distribui o binário compatível com OCI `runsc`, o shim `containerd-shim-runsc-v1` e binários auxiliares (`gvisor-bin/`) que se integram diretamente ao Docker (`--runtime=runsc`) e ao Kubernetes (via `RuntimeClass`).

## Por que importa
Adotar um kernel de aplicação para isolar cargas multi-tenant não seria prático se exigisse reescrever imagens de container ou abandonar o Docker e o Kubernetes. Segundo o README oficial e o guia de introdução do gVisor, o `runsc` implementa a especificação Open Container Initiative (OCI), permitindo executar containers em sandbox simplesmente selecionando o runtime na criação do container ou Pod.

## Como funciona
Quando compilado ou instalado a partir do tarball de release (`gvisor.tar.bz2`), o pacote instala em `/usr/local/bin` o binário `runsc`, o `containerd-shim-runsc-v1` e um diretório `gvisor-bin/` ao lado dele contendo binários sidecar que o `runsc` espera encontrar. No Docker, após registrar o runtime no `daemon.json`, basta rodar `docker run --runtime=runsc ...`, onde o `runsc` mapeia apenas os volumes estritamente definidos na configuração OCI e executa `pivot_root(2)` para isolar o host. No Kubernetes, registra-se o handler `runsc` (`io.containerd.runsc.v1`) no `containerd` e cria-se um objeto `RuntimeClass` (ex.: `gvisor`) para que Pods com `runtimeClassName: gvisor` rodem dentro de sandboxes gVisor.

## Exemplo
```bash
# Construir o tarball de release contendo runsc, containerd-shim-runsc-v1 e gvisor-bin/ e instalar em /usr/local/bin
make release-tarball DESTINATION=bin/
sudo tar -C /usr/local/bin -xf bin/gvisor.tar.bz2

# Testar um container isolado no Docker mapeando apenas o diretório /tmp/vol
sudo docker run --rm --runtime=runsc -it -v /tmp/vol:/vol ubuntu /bin/bash
```

## Limites e trade-offs
Conforme alerta explicitamente a documentação oficial (`How can I test gVisor?`), o subcomando de conveniência `runsc do <cmd>` concede ao sandbox acesso somente-leitura a **todo o sistema de arquivos do host** por padrão para facilitar testes rápidos; portanto, ao avaliar o gVisor do ponto de vista de segurança ou em produção, nunca use `runsc do`, utilizando sempre o `runsc` como runtime OCI real via Docker ou Kubernetes (`containerd`).

## Como verificar
Dentro de um container iniciado com `docker run --rm --runtime=runsc alpine dmesg`, verifique a saída característica do kernel gVisor e execute `ps aux` no host para confirmar que os processos internos do container não aparecem como processos diretos na tabela do host.

## Conexões
- [[gvisor-plataformas-interceptacao-systrap-kvm]] — Veja também: Google gVisor: plataformas de interceptação de syscalls e page faults (Systrap padrão e KVM).
- [[gvisor-defesa-profundidade-limites-protecao-runtime-monitoring]] — Veja também: Google gVisor: modelo de defesa em profundidade, fronteiras do que o gVisor não protege e Runtime Monitoring.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[kata-packaging-kata-deploy-helm-kubernetes-runtimeclass]] — Referência cruzada direta com kata-packaging-kata-deploy-helm-kubernetes-runtimeclass.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
